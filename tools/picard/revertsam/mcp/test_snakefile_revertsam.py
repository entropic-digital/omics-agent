import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths for input and expected output files."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "input.sam",  # Example test input file
        "expected_snakefile": test_dir / "expected_snakefile",
    }


def test_snakefile_revertsam(test_paths, tmp_path, capsys):
    """Test that the revertsam Snakefile is generated correctly."""
    from tools.revertsam.mcp.run_revertsam import run_revertsam

    temp_output = tmp_path / "output.sam"

    # Generate the Snakefile with print_only=True
    run_revertsam(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        print_only=True
    )

    # Capture the generated Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements of the Snakefile
    assert "rule revertsam:" in content, "Missing rule definition for revertsam"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f"input_file='{test_paths['input_file']}'" in content, "Incorrect or missing input_file definition"
    assert f"output_file='{temp_output}'" in content, "Incorrect or missing output_file definition"
    assert "wrapper: 'file:tools/picard/revertsam'" in content, "Wrapper path is missing or incorrect"


def test_run_revertsam(test_paths, tmp_path):
    """Test actual execution of the revertsam tool."""
    from tools.revertsam.mcp.run_revertsam import run_revertsam

    temp_output = tmp_path / "output.sam"

    # Run the tool with test input file
    result = run_revertsam(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output)
    )

    # Verify the command execution is successful
    assert result.returncode == 0, "revertsam execution failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"