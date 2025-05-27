import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bed_file": test_dir / "test.bed",
        "fasta_file": test_dir / "test.fasta",
        "output_fasta_file": test_dir / "test_output.fasta",
    }

def test_snakefile_get_seqs(test_paths, tmp_path, capsys):
    """Test that get_seqs generates the expected Snakefile."""
    from bioinformatics_mcp.purge_dups.get_seqs.mcp.run_get_seqs import run_get_seqs
    temp_output = tmp_path / "output.fasta"

    # Generate the Snakefile with print_only=True to capture the content
    run_get_seqs(
        bed_file=str(test_paths["bed_file"]),
        fasta_file=str(test_paths["fasta_file"]),
        output_fasta_file=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule get_seqs:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"bed_file='{test_paths['bed_file']}'" in content, "Missing bed_file input"
    assert f"fasta_file='{test_paths['fasta_file']}'" in content, "Missing fasta_file input"
    assert f"output_fasta_file='{temp_output}'" in content, "Missing output_fasta_file output"

def test_run_get_seqs(test_paths, tmp_path):
    """Test that get_seqs can be run with the test files."""
    from bioinformatics_mcp.purge_dups.get_seqs.mcp.run_get_seqs import run_get_seqs
    temp_output = tmp_path / "output.fasta"

    result = run_get_seqs(
        bed_file=str(test_paths["bed_file"]),
        fasta_file=str(test_paths["fasta_file"]),
        output_fasta_file=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "get_seqs run failed"
    assert temp_output.exists(), "Output file was not created"