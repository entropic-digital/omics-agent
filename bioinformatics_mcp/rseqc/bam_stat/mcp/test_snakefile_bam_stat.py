import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.bam",
        "expected_output": test_dir / "expected_output.txt",
        "snakefile_output": tmp_path / "Snakefile_generated",
    }


def test_snakefile_bam_stat(test_paths, tmp_path, capsys):
    """Test that bam_stat generates the expected Snakefile."""
    from bioinformatics_mcp.rseqc.bam_stat.run_bam_stat import run_bam_stat

    temp_output = tmp_path / "output_summary.txt"

    run_bam_stat(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule bam_stat:" in content, "Missing rule definition for bam_stat"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper declaration in Snakefile"
    assert "input_file=" in content, "Missing required 'input_file' parameter"
    assert "output_file=" in content, "Missing required 'output_file' parameter"


def test_run_bam_stat(test_paths, tmp_path):
    """Test that bam_stat can be run with the test files."""
    from bioinformatics_mcp.rseqc.bam_stat.run_bam_stat import run_bam_stat

    temp_output = tmp_path / "output_summary.txt"

    result = run_bam_stat(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
    )

    assert result.returncode == 0, "bam_stat execution failed"
    assert temp_output.exists(), "Output file was not created after bam_stat run"