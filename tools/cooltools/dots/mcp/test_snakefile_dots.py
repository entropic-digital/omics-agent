import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "mcool_file": test_dir / "test_file.mcool",
        "expected_file": test_dir / "expected.txt",
        "view_file": test_dir / "view.bed",
        "output_file": test_dir / "output.bedpe",
    }


def test_snakefile_dots(test_paths, tmp_path, capsys):
    """Test that dots generates the expected Snakefile."""
    from tools.cooltools.dots.run_dots import run_dots

    # Generate the Snakefile with print_only=True to capture its content
    run_dots(
        mcool_file=str(test_paths["mcool_file"]),
        expected_file=str(test_paths["expected_file"]),
        view_file=str(test_paths["view_file"]),
        output_file=str(test_paths["output_file"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule dots:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify all required inputs are present
    assert "mcool_file=" in content, "Missing mcool_file input parameter"
    assert "expected_file=" in content, "Missing expected_file input parameter"
    assert "view_file=" in content, "Optional view_file input parameter missing"

    # Verify the required output
    assert "output_file=" in content, "Missing output_file parameter"


def test_run_dots(test_paths, tmp_path):
    """Test that the dots tool executes correctly with test files."""
    from tools.cooltools.dots.run_dots import run_dots

    temp_output = tmp_path / "output.bedpe"

    # Run the tool using test files
    result = run_dots(
        mcool_file=str(test_paths["mcool_file"]),
        expected_file=str(test_paths["expected_file"]),
        view_file=str(test_paths["view_file"]),
        output_file=str(temp_output),
    )

    # Verify that the Snakemake process completed successfully
    assert result.returncode == 0, "dots tool execution failed"

    # Verify that the output file is generated
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"