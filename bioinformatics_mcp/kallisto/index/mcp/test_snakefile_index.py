import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    test_dir = Path(__file__).parent / "test_data"
    return {
        "fasta": test_dir / "test.fasta",
        "index": test_dir / "test.index",
        "expected_snakefile": test_dir / "expected_snakefile.txt",
    }


def test_snakefile_kallisto_index(test_paths, tmp_path, capsys):
    """Test that kallisto index generates the expected Snakefile."""
    from run_index import run_index
    temp_output = tmp_path / "test.index"

    # Generate the Snakefile with print_only=True to capture its content
    run_index(
        fasta=str(test_paths["fasta"]),
        index=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    snakefile_content = captured.out

    # Verify the essential elements are present in the Snakefile
    assert "rule index:" in snakefile_content, "Missing rule definition in Snakefile"
    assert "input:" in snakefile_content, "Missing input section in Snakefile"
    assert "output:" in snakefile_content, "Missing output section in Snakefile"
    assert "params:" in snakefile_content, "Missing params section in Snakefile"
    assert "wrapper:" in snakefile_content, "Missing wrapper section in Snakefile"
    assert "fasta=" in snakefile_content, "Missing 'fasta' input parameter in Snakefile"
    assert "index=" in snakefile_content, "Missing 'index' output parameter in Snakefile"


def test_run_kallisto_index(test_paths, tmp_path):
    """Test that kallisto index can be run with the test files."""
    from run_index import run_index
    temp_output = tmp_path / "test.index"

    # Run the tool with provided test files
    result = run_index(
        fasta=str(test_paths["fasta"]),
        index=str(temp_output)
    )

    # Verify that the tool ran successfully and generated expected output
    assert result.returncode == 0, "Kallisto index run failed"
    assert temp_output.exists(), "Output index file was not created"
    assert temp_output.stat().st_size > 0, "Output index file is empty"