import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test_data"  # Adjust as needed
    return {
        "intervals": test_dir / "test_intervals.interval_list",
        "output_dir": test_dir / "test_output",
        "expected_snakefile": test_dir / "expected_Snakefile"
    }


def test_snakefile_splitintervals(test_paths, tmp_path, capsys):
    """Test that splitintervals generates the expected Snakefile."""
    from tools.gatk.splitintervals.run_splitintervals import run_splitintervals

    temp_output = tmp_path / "output"
    temp_output.mkdir()

    # Generate the Snakefile with print_only=True to capture the content
    run_splitintervals(
        intervals=str(test_paths["intervals"]),
        output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements
    assert "rule splitintervals:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Validate against expected inputs and outputs
    assert "intervals=" in content, "Missing intervals input parameter"
    assert f'"{test_paths["intervals"]}"' in content, "Incorrect intervals input"
    assert "output=" in content, "Missing output parameter"
    assert f'"{str(temp_output)}"' in content, "Incorrect output path"


def test_run_splitintervals(test_paths, tmp_path):
    """Test that splitintervals can be run with the test files."""
    from tools.gatk.splitintervals.run_splitintervals import run_splitintervals

    temp_output = tmp_path / "output"
    temp_output.mkdir()

    # Run the tool with test input and capture the result
    result = run_splitintervals(
        intervals=str(test_paths["intervals"]),
        output=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "splitintervals run failed"
    assert temp_output.exists(), "Output directory was not created"
    assert any(temp_output.iterdir()), "No output files were generated"

    # Verify expected output files exist
    output_files = list(temp_output.glob("*.interval_list"))
    assert len(output_files) > 0, "No interval files generated in output"