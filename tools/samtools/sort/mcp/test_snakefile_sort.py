import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.bam",
        "output_file": test_dir / "expected_output.bam",
        "index_file": test_dir / "expected_output.bai",
        "snakefile_ref": test_dir / "Snakefile",
    }


def test_snakefile_sort(test_paths, tmp_path, capsys):
    """Test that samtools_sort generates the expected Snakefile."""
    from tools.samtools.mcp.run_sort import run_sort
    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True
    run_sort(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        index_file="",
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements in the Snakefile
    assert "rule samtools_sort:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify input and output parameters from meta.yaml
    assert "input_file=" in content, "Missing input_file parameter"
    assert "output_file=" in content, "Missing output_file parameter"
    assert "index_file" in content, "Missing index_file parameter (optional)"

    # Verify wrapper path
    assert "tools/samtools/sort" in content, "Incorrect wrapper path"


def test_run_sort(test_paths, tmp_path):
    """Test that samtools_sort runs successfully with test files."""
    from tools.samtools.mcp.run_sort import run_sort
    temp_output = tmp_path / "sorted_output.bam"
    temp_index = tmp_path / "sorted_output.bai"

    # Run the tool with test inputs
    result = run_sort(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        index_file=str(temp_index),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "samtools_sort run failed"

    # Verify output files
    assert temp_output.exists(), "Sorted output file not created"
    assert temp_index.exists(), "Index file not created"