import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.sam",
        "expected_snakefile": test_dir / "expected_snakefile",
        "output_file": test_dir / "test_output.bam",
    }


def test_snakefile_sortsam(test_paths, tmp_path, capsys):
    """Test that sortsam generates the expected Snakefile."""
    from tools.picard.sortsam.run_sortsam import run_sortsam

    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_sortsam(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in Snakefile content
    assert "rule sortsam:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    # Additional checks for required parameters
    assert f"input_file='{str(test_paths['input_file'])}'" in content, (
        "Missing input_file parameter"
    )
    assert f"output_file='{str(temp_output)}'" in content, (
        "Missing output_file parameter"
    )


def test_run_sortsam(test_paths, tmp_path):
    """Test that sortsam can be run with the test files."""
    from tools.picard.sortsam.run_sortsam import run_sortsam

    temp_output = tmp_path / "output.bam"

    # Run the tool with required test inputs and outputs
    result = run_sortsam(
        input_file=str(test_paths["input_file"]), output_file=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "sortsam tool execution failed"
    assert temp_output.exists(), "Output file was not created"
