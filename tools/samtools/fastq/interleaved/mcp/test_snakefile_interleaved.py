import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "input.bam",
        "output_fastq": test_dir / "output.fastq",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_interleaved(test_paths, tmp_path, capsys):
    """Test that interleaved generates the expected Snakefile."""
    from tools.samtools.fastq.interleaved.run_interleaved import run_interleaved
    temp_output = tmp_path / "output.fastq"

    run_interleaved(
        input_bam=str(test_paths["input_bam"]),
        output_fastq=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule interleaved:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    assert f'input_bam="{test_paths["input_bam"]}"' in content, "Missing input_bam parameter"
    assert f'output_fastq="{temp_output}"' in content, "Missing output_fastq parameter"
    assert "threads=" in content, "Missing threads parameter in Snakefile"
    assert "extra=params.extra" in content, "Missing extra params in Snakefile"


def test_run_interleaved(test_paths, tmp_path):
    """Test that interleaved can be run with the test files."""
    from tools.samtools.fastq.interleaved.run_interleaved import run_interleaved
    temp_output = tmp_path / "output.fastq"

    result = run_interleaved(
        input_bam=str(test_paths["input_bam"]),
        output_fastq=str(temp_output),
        threads=2
    )

    assert result.returncode == 0, "The interleaved tool execution failed"
    assert temp_output.exists(), "Output FASTQ file was not created"
    assert temp_output.stat().st_size > 0, "Output FASTQ file is empty"