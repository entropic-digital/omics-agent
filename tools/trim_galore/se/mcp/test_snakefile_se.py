import pytest
from pathlib import Path
import subprocess


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fastq": test_dir / "test_input.fastq",
        "trimmed_fastq": test_dir / "test_trimmed_output.fastq",
        "trimming_report": test_dir / "test_trimming_report.txt",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_se(test_paths, tmp_path, capsys):
    """Test that trim_galore-se generates the expected Snakefile."""
    from tools.trim_galore.se.run_se import run_trim_galore_se

    run_trim_galore_se(
        fastq=str(test_paths["fastq"]),
        trimmed_fastq=str(test_paths["trimmed_fastq"]),
        trimming_report=str(test_paths["trimming_report"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "fastq=" in content, "Missing fastq input parameter"
    assert "trimmed_fastq=" in content, "Missing trimmed_fastq output parameter"
    assert "trimming_report=" in content, "Missing trimming_report output parameter"


def test_run_se(test_paths, tmp_path):
    """Test that trim_galore-se runs successfully with test files."""
    from tools.trim_galore.se.run_se import run_trim_galore_se

    trimmed_fastq = tmp_path / "output_trimmed.fastq"
    trimming_report = tmp_path / "output_report.txt"

    result = run_trim_galore_se(
        fastq=str(test_paths["fastq"]),
        trimmed_fastq=str(trimmed_fastq),
        trimming_report=str(trimming_report),
    )

    assert result.returncode == 0, "trim_galore-se run failed"
    assert trimmed_fastq.exists(), "Missing trimmed_fastq output file"
    assert trimming_report.exists(), "Missing trimming_report output file"