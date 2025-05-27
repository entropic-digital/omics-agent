import pytest
from pathlib import Path
from bioinformatics_mcp.rnaseq.mcp.run_rnaseq import run_rnaseq


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "test.bam",
        "gtf_file": test_dir / "test.gtf",
        "expected_qc_report": test_dir / "expected_qc_report.html"
    }


def test_snakefile_rnaseq(test_paths, tmp_path, capsys):
    """Test that rnaseq generates the expected Snakefile."""
    temp_qc_report = tmp_path / "qc_report.html"

    # Generate the Snakefile with print_only=True
    run_rnaseq(
        bam_file=str(test_paths["bam_file"]),
        gtf_file=str(test_paths["gtf_file"]),
        qc_report=str(temp_qc_report),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in the Snakefile
    assert "rule rnaseq:" in content, "Missing rule definition for rnaseq"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify required inputs
    assert "bam_file=" in content, "Missing bam_file parameter"
    assert "gtf_file=" in content, "Missing gtf_file parameter"

    # Verify required outputs
    assert "qc_report=" in content, "Missing qc_report parameter"


def test_run_rnaseq(test_paths, tmp_path):
    """Test that rnaseq can be executed with the test files."""
    temp_qc_report = tmp_path / "qc_report.html"

    # Run the tool
    result = run_rnaseq(
        bam_file=str(test_paths["bam_file"]),
        gtf_file=str(test_paths["gtf_file"]),
        qc_report=str(temp_qc_report)
    )

    # Verify execution success
    assert result.returncode == 0, "rnaseq run failed"

    # Verify output file creation
    assert temp_qc_report.exists(), "Expected QC report was not created"
