import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_twoBit": test_dir / "test_input.2bit",
        "expected_fa": test_dir / "expected_output.fa",
        "expected_snakefile": test_dir / "Snakefile",
    }

def test_snakefile_twoBitToFa(test_paths, tmp_path, capsys):
    """Test that twoBitToFa generates the expected Snakefile."""
    from bioinformatics_mcp.twoBitToFa.mcp.run_twoBitToFa import run_twoBitToFa
    temp_output = tmp_path / "output.fa"

    # Generate the Snakefile with print_only=True to capture the content
    run_twoBitToFa(
        input_twoBit=str(test_paths["input_twoBit"]),
        output_fa=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements are present in the Snakefile
    assert "rule twoBitToFa:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"input_twoBit='{test_paths['input_twoBit']}'" in content, "Missing input_twoBit parameter"
    assert f"output_fa='{temp_output}'" in content, "Missing output_fa parameter"

def test_run_twoBitToFa(test_paths, tmp_path):
    """Test that twoBitToFa can be run with the test files."""
    from bioinformatics_mcp.twoBitToFa.mcp.run_twoBitToFa import run_twoBitToFa
    temp_output = tmp_path / "output.fa"

    # Run the tool with test input
    result = run_twoBitToFa(
        input_twoBit=str(test_paths["input_twoBit"]),
        output_fa=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "twoBitToFa run failed"
    assert temp_output.exists(), "Output file was not created"

    # Optionally, compare the output to the expected result
    with open(test_paths["expected_fa"], "r") as expected, open(temp_output, "r") as output:
        assert output.read() == expected.read(), "Output file content does not match expected content"