import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "test.bam",
        "qc_report": test_dir / "genome_results.txt",
        "expected_snakefile": test_dir / "Snakefile",
    }

def test_snakefile_bamqc(test_paths, tmp_path, capsys):
    """Test that bamqc generates the expected Snakefile."""
    from bioinformatics_mcp.qualimap.bamqc.run_bamqc import run_bamqc
    temp_qc_report = tmp_path / "genome_results.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_bamqc(
        bam_file=str(test_paths["bam_file"]),
        qc_report=str(temp_qc_report),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the Snakefile
    assert "rule bamqc:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "bam_file=" in content, "Missing bam_file parameter in input"
    assert "output:" in content, "Missing output section"
    assert "qc_report=" in content, "Missing qc_report parameter in output"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "tools/qualimap/bamqc" in content, "Incorrect wrapper path"

def test_run_bamqc(test_paths, tmp_path):
    """Test that bamqc can be run with the test files."""
    from bioinformatics_mcp.qualimap.bamqc.run_bamqc import run_bamqc
    temp_qc_report = tmp_path / "genome_results.txt"

    result = run_bamqc(
        bam_file=str(test_paths["bam_file"]),
        qc_report=str(temp_qc_report),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "bamqc run failed"
    assert temp_qc_report.exists(), "Expected QC report not generated"
    assert temp_qc_report.stat().st_size > 0, "Generated QC report is empty"