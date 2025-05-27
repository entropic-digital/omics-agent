import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "indexed_db": test_dir / "indexed_db.fasta",
        "sequences": test_dir / "sequences.fasta",
        "alignments_output": test_dir / "alignments_output.txt"
    }


def test_snakefile_lastal(test_paths, tmp_path, capsys):
    """Test that lastal generates the expected Snakefile."""
    from bioinformatics_mcp.lastal.run_lastal import run_lastal
    temp_output = tmp_path / "alignments_output.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_lastal(
        indexed_db=str(test_paths["indexed_db"]),
        sequences=str(test_paths["sequences"]),
        alignments_output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements are present in the Snakefile
    assert "rule lastal:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "indexed_db=" in content, "Missing indexed_db input parameter"
    assert "sequences=" in content, "Missing sequences input parameter"
    assert "alignments_output=" in content, "Missing alignments_output parameter"


def test_run_lastal(test_paths, tmp_path):
    """Test that lastal can be run with the test files."""
    from bioinformatics_mcp.lastal.run_lastal import run_lastal
    temp_output = tmp_path / "alignments_output.txt"

    result = run_lastal(
        indexed_db=str(test_paths["indexed_db"]),
        sequences=str(test_paths["sequences"]),
        alignments_output=str(temp_output)
    )

    # Verify that the process completed successfully
    assert result.returncode == 0, "lastal run failed"
    # Verify that the output file is created
    assert temp_output.exists(), "Output file was not created"
    # Add further checks for the file content if needed.