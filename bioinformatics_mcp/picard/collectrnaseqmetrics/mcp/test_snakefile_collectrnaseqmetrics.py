import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "data"
    return {
        "bam_file": base_dir / "example.bam",
        "ref_flat_file": base_dir / "example.refFlat",
        "reference_fasta": base_dir / "example.fasta",
        "expected_snakefile": base_dir / "expected_Snakefile",
    }


def test_snakefile_collectrnaseqmetrics(test_paths, tmp_path, capsys):
    """Test that collectrnaseqmetrics generates the expected Snakefile."""
    from bioinformatics_mcp.picard.collectrnaseqmetrics.run_collectrnaseqmetrics import run_collectrnaseqmetrics

    temp_output = tmp_path / "metrics.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_collectrnaseqmetrics(
        bam_file=str(test_paths["bam_file"]),
        ref_flat_file=str(test_paths["ref_flat_file"]),
        reference_fasta=str(test_paths["reference_fasta"]),
        output=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile elements
    assert "rule collectrnaseqmetrics:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Add assertions for inputs
    assert "bam_file=" in content, "Missing bam_file input"
    assert "ref_flat_file=" in content, "Missing ref_flat_file input"
    assert "reference_fasta=" in content, "Missing reference_fasta parameter"
    # Add assertion for output
    assert "metrics.txt" in content, "Missing RNA-Seq metrics output file"


def test_run_collectrnaseqmetrics(test_paths, tmp_path):
    """Test that collectrnaseqmetrics can be run with the test files."""
    from bioinformatics_mcp.picard.collectrnaseqmetrics.run_collectrnaseqmetrics import run_collectrnaseqmetrics

    temp_output = tmp_path / "metrics.txt"

    result = run_collectrnaseqmetrics(
        bam_file=str(test_paths["bam_file"]),
        ref_flat_file=str(test_paths["ref_flat_file"]),
        reference_fasta=str(test_paths["reference_fasta"]),
        output=str(temp_output),
    )

    # Verify that the tool ran successfully
    assert result.returncode == 0, "collectrnaseqmetrics run failed"

    # Verify that the expected output file was created
    assert temp_output.exists(), "Expected output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"