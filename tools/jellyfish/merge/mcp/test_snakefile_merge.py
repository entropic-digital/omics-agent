"""Test suite for the jellyfish_merge tool."""

import pytest
from pathlib import Path
from tools.jellyfish.merge.run_merge import jellyfish_merge


@pytest.fixture
def test_paths():
    """Set up test paths for the jellyfish_merge tool."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input1": test_dir / "test_input1.jf",
        "input2": test_dir / "test_input2.jf",
        "output_file": test_dir / "test_output.jf",
    }


def test_snakefile_merge(test_paths, tmp_path, capsys):
    """Test that jellyfish_merge generates the expected Snakefile."""
    temp_output = tmp_path / "merged_output.jf"

    # Generate the Snakefile with print_only=True
    jellyfish_merge(
        input_files=[str(test_paths["input1"]), str(test_paths["input2"])],
        output_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile components
    assert "rule jellyfish_merge:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper definition in Snakefile"
    # Check for all input parameters in Snakefile
    assert test_paths["input1"].name in content, "Missing input1 in Snakefile"
    assert test_paths["input2"].name in content, "Missing input2 in Snakefile"
    # Check for output parameters in Snakefile
    assert "merged_output.jf" in content, "Missing output parameter in Snakefile"


def test_run_merge(test_paths, tmp_path):
    """Test that jellyfish_merge successfully runs with test files."""
    temp_output = tmp_path / "merged_output.jf"

    # Run the merge tool with input and output test files
    result = jellyfish_merge(
        input_files=[str(test_paths["input1"]), str(test_paths["input2"])],
        output_file=str(temp_output),
    )

    # Verify the process completed successfully
    assert result.returncode == 0, "jellyfish_merge run failed"
    # Verify the output file is created
    assert temp_output.exists(), "Output file was not created"
