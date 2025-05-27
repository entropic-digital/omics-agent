import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "left": test_dir / "input_left.bed",
        "right": test_dir / "input_right.bed",
        "output": test_dir / "output.bed",
    }

def test_snakefile_intersect(test_paths, tmp_path, capsys):
    """Test that intersect generates the expected Snakefile."""
    from bioinformatics_mcp.bedtools.intersect.run_intersect import run_intersect
    temp_output = tmp_path / "output.bed"

    # Generate the Snakefile with print_only=True to capture the content
    run_intersect(
        left=str(test_paths["left"]),
        right=str(test_paths["right"]),
        output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule intersect:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"left='{test_paths['left']}'" in content, "Missing left input file"
    assert f"right='{test_paths['right']}'" in content, "Missing right input file"
    assert f"output='{temp_output}'" in content, "Missing output file"

def test_run_intersect(test_paths, tmp_path):
    """Test that intersect can be run with the test files."""
    from bioinformatics_mcp.bedtools.intersect.run_intersect import run_intersect
    temp_output = tmp_path / "output.bed"

    result = run_intersect(
        left=str(test_paths["left"]),
        right=str(test_paths["right"]),
        output=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "intersect run failed"
    # Verify that output file is created
    assert temp_output.exists(), "Output file was not created"
    # Optional: Check if the output length or content is as expected
    assert temp_output.stat().st_size > 0, "Output file is empty"