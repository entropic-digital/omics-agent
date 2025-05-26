import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths with input, output, and expected Snakefile locations."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.sam",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_map(test_paths, tmp_path, capsys):
    """Test Snakefile generation for the map tool."""
    from tools.pretext.map.run_map import run_map
    temp_output = tmp_path / "output.pretext"

    # Generate the Snakefile with print_only=True to capture its content
    run_map(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements are present
    assert "rule map:" in content, "Missing rule definition 'rule map:'"
    assert "input:" in content, "Missing input section in the Snakefile"
    assert "output:" in content, "Missing output section in the Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in the Snakefile"

    # Verify required inputs and outputs from meta.yaml
    assert "input='{}'".format(test_paths["input_file"]) in content, "Missing correct input parameter"
    assert "output='{}'".format(temp_output) in content, "Missing correct output parameter"


def test_run_map(test_paths, tmp_path):
    """Test tool execution for the map tool."""
    from tools.pretext.map.run_map import run_map
    temp_output = tmp_path / "output.pretext"

    # Run the map tool
    result = run_map(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
    )

    # Verify successful execution
    assert result.returncode == 0, "map tool execution failed"
    assert temp_output.exists(), "Output file was not created as expected"