import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "transcripts": test_dir / "test_transcripts.fasta",
        "expected_orfs_peptides": test_dir / "expected_orfs_peptides.txt",
    }


def test_snakefile_longorfs(test_paths, tmp_path, capsys):
    """Test that longorfs generates the expected Snakefile."""
    from tools.transdecoder.mcp.run_longorfs import run_longorfs
    temp_output = tmp_path / "orfs_peptides.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_longorfs(
        transcripts=str(test_paths["transcripts"]),
        orfs_peptide_files=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule longorfs:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify all required inputs and outputs
    assert "transcripts=" in content, "Missing transcripts input parameter"
    assert "orfs_peptide_files=" in content, "Missing orfs_peptide_files output parameter"
    assert "params" in content and "min_length" in content, "Missing params.min_length parameter"


def test_run_longorfs(test_paths, tmp_path):
    """Test that longorfs can be run with the test files."""
    from tools.transdecoder.mcp.run_longorfs import run_longorfs
    temp_output = tmp_path / "orfs_peptides.txt"

    # Run the tool with required inputs
    result = run_longorfs(
        transcripts=str(test_paths["transcripts"]),
        orfs_peptide_files=str(temp_output),
        min_length=100,
    )

    # Verify that the run is successful
    assert result.returncode == 0, "longorfs tool execution failed"
    assert temp_output.exists(), "The expected output file was not created"
