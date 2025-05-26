import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "protein_sequence_file": test_dir / "example.fasta",
        "database_hmm_files": test_dir / "example.hmm",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_hmmscan(test_paths, tmp_path, capsys):
    """Test that hmmscan generates the expected Snakefile."""
    from tools.hmmscan.mcp.run_hmmscan import run_hmmscan
    temp_output = tmp_path / "output_matches.txt"

    # Generate the Snakefile with print_only=True
    run_hmmscan(
        protein_sequence_file=str(test_paths["protein_sequence_file"]),
        database_hmm_files=str(test_paths["database_hmm_files"]),
        output_matches=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    snakefile_content = captured.out

    # Assertions for core Snakefile structure
    assert "rule hmmscan:" in snakefile_content, "Missing rule definition for hmmscan"
    assert "input:" in snakefile_content, "Missing input section in Snakefile"
    assert "output:" in snakefile_content, "Missing output section in Snakefile"
    assert "wrapper:" in snakefile_content, "Missing wrapper directive in Snakefile"

    # Assertions for specific parameters from meta.yaml
    assert "protein_sequence_file=" in snakefile_content, "Missing protein_sequence_file parameter"
    assert "database_hmm_files=" in snakefile_content, "Missing database_hmm_files parameter"
    assert "output_matches=" in snakefile_content, "Missing output_matches parameter"


def test_run_hmmscan(test_paths, tmp_path):
    """Test that hmmscan can be run with the test files."""
    from tools.hmmscan.mcp.run_hmmscan import run_hmmscan
    temp_output = tmp_path / "output_matches.txt"

    # Run the hmmscan tool
    result = run_hmmscan(
        protein_sequence_file=str(test_paths["protein_sequence_file"]),
        database_hmm_files=str(test_paths["database_hmm_files"]),
        output_matches=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "hmmscan run failed with non-zero exit code"

    # Verify that the output file is created and not empty
    assert temp_output.exists(), "Output matches file was not created"
    assert temp_output.stat().st_size > 0, "Output matches file is empty"