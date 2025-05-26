import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "graph": test_dir / "test_graph.gfa",
        "expected_output": test_dir / "expected_output.gfa",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_ids(test_paths, tmp_path, capsys):
    """Test that ids generates the expected Snakefile."""
    from tools.vg.ids import run_ids
    temp_output = tmp_path / "output.gfa"

    # Generate the Snakefile with print_only=True to capture the content
    run_ids(
        graph=str(test_paths["graph"]),
        output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule ids:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "graph=" in content, "Missing graph parameter"
    assert "output=" in content, "Missing output parameter"


def test_run_ids(test_paths, tmp_path):
    """Test that ids can be run with the test files."""
    from tools.vg.ids import run_ids
    temp_output = tmp_path / "output.gfa"

    # Run the ids tool with the test inputs
    result = run_ids(
        graph=str(test_paths["graph"]),
        output=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "ids run failed"

    # Verify that the output file exists
    assert temp_output.exists(), "Output file was not created"

    # Further checks could be added here to assert output content if necessary