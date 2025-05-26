import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths for the tests."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test_data"
    return {
        "fasta_file": test_dir / "test.fasta",
        "dict_file": test_dir / "test.dict",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_createsequencedictionary(test_paths, tmp_path, capsys):
    """Test that createsequencedictionary generates the expected Snakefile."""
    from tools.picard.createsequencedictionary.run_createsequencedictionary import run_createsequencedictionary
    tmp_dict_file = tmp_path / "output.dict"

    # Generate the Snakefile with print_only=True
    run_createsequencedictionary(
        fasta_file=str(test_paths["fasta_file"]),
        dict_file=str(tmp_dict_file),
        print_only=True
    )

    # Capture the generated Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile structure and parameters
    assert "rule createsequencedictionary:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify required input and output parameters are present
    assert f"fasta={str(test_paths['fasta_file'])}" in content, "Missing fasta input parameter"
    assert f"dict={str(tmp_dict_file)}" in content, "Missing dict output parameter"
    assert "wrapper: \"file:tools/picard/createsequencedictionary\"" in content, "Missing correct wrapper path"


def test_run_createsequencedictionary(test_paths, tmp_path):
    """Test that createsequencedictionary runs successfully with test data."""
    from tools.picard.createsequencedictionary.run_createsequencedictionary import run_createsequencedictionary
    tmp_dict_file = tmp_path / "output.dict"

    result = run_createsequencedictionary(
        fasta_file=str(test_paths["fasta_file"]),
        dict_file=str(tmp_dict_file)
    )

    # Verify the execution was successful
    assert result.returncode == 0, "createsequencedictionary tool execution failed"

    # Verify the expected output file is created
    assert tmp_dict_file.exists(), "Output .dict file was not created"
    assert tmp_dict_file.stat().st_size > 0, "Output .dict file is empty"
