import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "test_file_id": "test_file_id",
        "expected_snakefile": test_dir / "Snakefile",
        "expected_output": test_dir / "output.format",
    }


def test_snakefile_fetch(test_paths, capsys):
    """Test that fetch generates the expected Snakefile."""
    from tools.ega.fetch.run_fetch import run_fetch

    # Generate the Snakefile with print_only=True to capture the content
    run_fetch(
        file_id=test_paths["test_file_id"],
        output_format="BAM",
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in content
    assert "rule fetch:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify the rule's parameters match the expected inputs/outputs
    assert "file_id=" in content, "Missing file_id parameter in input"
    assert "output_format=" in content, "Missing output_format parameter in params"


def test_run_fetch(test_paths, tmp_path):
    """Test that fetch can be run with test files."""
    from tools.ega.fetch.run_fetch import run_fetch

    temp_output = tmp_path / test_paths["expected_output"].name

    # Perform the tool execution
    result = run_fetch(
        file_id=test_paths["test_file_id"],
        output_format="BAM",
        output=str(temp_output)
    )

    # Verify the run is successful
    assert result.returncode == 0, "fetch tool execution failed"

    # Verify the expected output file is created
    assert temp_output.exists(), "Expected output file was not created"
