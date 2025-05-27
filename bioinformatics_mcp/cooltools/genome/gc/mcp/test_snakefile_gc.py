import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bed_file": test_dir / "test_input.bed",
        "genome_fasta": test_dir / "test_genome.fasta",
        "output_tsv": test_dir / "test_output.tsv",
    }


def test_snakefile_gc(test_paths, tmp_path, capsys):
    """Test that gc generates the expected Snakefile."""
    from bioinformatics_mcp.gc.mcp.run_gc import run_gc
    temp_output = tmp_path / "output.tsv"

    # Generate the Snakefile with print_only=True to capture the content
    run_gc(
        bed_file=str(test_paths["bed_file"]),
        genome_fasta=str(test_paths["genome_fasta"]),
        output_tsv=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the generated Snakefile
    assert "rule gc:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Add assertions for expected inputs based on meta.yaml
    assert "bed_file=" in content, "Missing bed_file input parameter"
    assert "genome_fasta=" in content, "Missing genome_fasta input parameter"
    # Add assertions for outputs based on meta.yaml
    assert "output_tsv=" in content, "Missing output_tsv parameter"


def test_run_gc(test_paths, tmp_path):
    """Test that gc can be run with the test files."""
    from bioinformatics_mcp.gc.mcp.run_gc import run_gc
    temp_output = tmp_path / "output.tsv"

    # Run the gc tool
    result = run_gc(
        bed_file=str(test_paths["bed_file"]),
        genome_fasta=str(test_paths["genome_fasta"]),
        output_tsv=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "gc run failed"

    # Verify that the output file is created
    assert temp_output.exists(), "Output file was not generated"

    # Optionally verify the output content or specific results if needed
    with temp_output.open() as f:
        lines = f.readlines()
        assert len(lines) > 0, "Output file is empty"
        assert "GC content" in lines[0], "Missing expected header in output file"