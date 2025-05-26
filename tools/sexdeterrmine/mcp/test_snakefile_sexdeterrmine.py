import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "depth": test_dir / "test_depth.txt",
        "expected_output": test_dir / "expected_output.txt",
    }


def test_snakefile_sexdeterrmine(test_paths, tmp_path, capsys):
    """Test that sexdeterrmine generates the expected Snakefile."""
    from tools.sexdeterrmine.mcp.run_sexdeterrmine import run_sexdeterrmine

    temp_output = tmp_path / "output.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_sexdeterrmine(
        depth=str(test_paths["depth"]),
        output=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule sexdeterrmine:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "depth=" in content, "Missing 'depth' input parameter in Snakefile"
    assert "output=" in content, "Missing 'output' output parameter in Snakefile"


def test_run_sexdeterrmine(test_paths, tmp_path):
    """Test that sexdeterrmine can be run successfully with test files."""
    from tools.sexdeterrmine.mcp.run_sexdeterrmine import run_sexdeterrmine

    temp_output = tmp_path / "output.txt"

    # Run the tool with the provided inputs and outputs
    result = run_sexdeterrmine(
        depth=str(test_paths["depth"]),
        output=str(temp_output),
    )

    # Verify that the tool runs successfully
    assert result.returncode == 0, "sexdeterrmine run failed"

    # Verify that the output file is created
    assert temp_output.exists(), "Output file was not created"

    # Optionally verify the content of the output file
