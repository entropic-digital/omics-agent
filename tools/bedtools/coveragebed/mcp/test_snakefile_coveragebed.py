import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "feature_file": test_dir / "test_a.bed",
        "comparison_files": [test_dir / "test_b1.bed", test_dir / "test_b2.bed"],
        "expected_output": test_dir / "expected_output.bed",
    }


def test_snakefile_coveragebed(test_paths, tmp_path, capsys):
    """Test that coveragebed generates the expected Snakefile."""
    from tools.coveragebed.mcp.run_coveragebed import run_coveragebed
    temp_output = tmp_path / "test_output.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_coveragebed(
        a=str(test_paths["feature_file"]),
        b=[str(f) for f in test_paths["comparison_files"]],
        output=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements are present in the Snakefile
    assert "rule coveragebed:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify required inputs and outputs are correctly referenced
    assert str(test_paths["feature_file"]) in content, "Missing feature file path in Snakefile input"
    for comparison_file in test_paths["comparison_files"]:
        assert str(comparison_file) in content, f"Missing comparison file {comparison_file} in Snakefile input"
    assert str(temp_output) in content, "Missing output file path in Snakefile output"


def test_run_coveragebed(test_paths, tmp_path):
    """Test that coveragebed can be run with the test files."""
    from tools.coveragebed.mcp.run_coveragebed import run_coveragebed
    temp_output = tmp_path / "test_output.txt"

    result = run_coveragebed(
        a=str(test_paths["feature_file"]),
        b=[str(f) for f in test_paths["comparison_files"]],
        output=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "coveragebed tool execution failed"

    # Verify that the output file is created and not empty
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"