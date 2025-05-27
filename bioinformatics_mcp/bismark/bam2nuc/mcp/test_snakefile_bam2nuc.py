import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths for bam2nuc testing."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "genome_fa": test_dir / "genome.fa",
        "bam": test_dir / "sample.bam",
        "expected_output": test_dir / "genomic_nucleotide_frequencies.txt",
    }


def test_snakefile_bam2nuc(test_paths, tmp_path, capsys):
    """Test that bam2nuc generates the expected Snakefile."""
    from bioinformatics_mcp.bam2nuc.mcp.run_bam2nuc import run_bam2nuc

    # Generate the Snakefile with print_only=True
    run_bam2nuc(
        genome_fa=str(test_paths["genome_fa"]),
        bam=str(test_paths["bam"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential elements of the Snakefile
    assert "rule bam2nuc:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "genome_fa=" in content, "Missing genome_fa input parameter"
    assert "bam=" in content, "Missing bam input parameter"
    assert "genomic_nucleotide_frequencies.txt" in content, (
        "Missing expected output file"
    )


def test_run_bam2nuc(test_paths, tmp_path):
    """Test that bam2nuc can be run with the test files."""
    from bioinformatics_mcp.bam2nuc.mcp.run_bam2nuc import run_bam2nuc

    # Define temporary output directory
    temp_output_dir = tmp_path / "output"
    temp_output_dir.mkdir()

    # Run bam2nuc tool
    result = run_bam2nuc(
        genome_fa=str(test_paths["genome_fa"]),
        bam=str(test_paths["bam"]),
        output_dir=str(temp_output_dir),
    )

    # Assert the process completed successfully
    assert result.returncode == 0, "bam2nuc run failed"

    # Check for output file generation
    output_file = temp_output_dir / "genomic_nucleotide_frequencies.txt"
    assert output_file.exists(), "Expected output file was not created"
    assert output_file.stat().st_size > 0, "Output file is empty"
