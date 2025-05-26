import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fastx_files": test_dir / "test_input.fastq",
        "r1": test_dir / "test_output_r1.fastq",
        "r1_bad": test_dir / "test_output_r1_bad.fastq",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_prinseq_plus_plus(test_paths, tmp_path, capsys):
    """Test that prinseq-plus-plus generates the expected Snakefile."""
    from tools.prinseq_plus_plus.mcp.run_prinseq_plus_plus import run_prinseq_plus_plus

    run_prinseq_plus_plus(
        fastx_files=str(test_paths["fastx_files"]),
        r1=str(test_paths["r1"]),
        r1_bad=str(test_paths["r1_bad"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule prinseq_plus_plus:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "fastx_files=" in content, "Missing fastx_files parameter in input"
    assert "r1=" in content, "Missing r1 parameter in output"
    assert "r1_bad=" in content, "Missing r1_bad parameter in output"


def test_run_prinseq_plus_plus(test_paths, tmp_path):
    """Test that prinseq-plus-plus can be run with the test files."""
    from tools.prinseq_plus_plus.mcp.run_prinseq_plus_plus import run_prinseq_plus_plus

    temp_r1 = tmp_path / "output_r1.fastq"
    temp_r1_bad = tmp_path / "output_r1_bad.fastq"

    result = run_prinseq_plus_plus(
        fastx_files=str(test_paths["fastx_files"]),
        r1=str(temp_r1),
        r1_bad=str(temp_r1_bad),
    )

    assert result.returncode == 0, "prinseq-plus-plus run failed"
    assert temp_r1.exists(), "Output file R1 was not created"
    assert temp_r1_bad.exists(), "Output file R1 (bad) was not created"