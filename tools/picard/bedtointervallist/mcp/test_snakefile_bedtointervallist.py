import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "bed": test_dir / "test.bed",
        "dict": test_dir / "test.dict",
        "expected_interval_list": test_dir / "expected.interval_list",
    }


def test_snakefile_bedtointervallist(test_paths, tmp_path, capsys):
    """Test that bedtointervallist generates the expected Snakefile."""
    from tools.picard.bedtointervallist.run_bedtointervallist import run_bedtointervallist
    temp_output = tmp_path / "output.interval_list"

    # Generate the Snakefile with print_only=True to capture the content
    run_bedtointervallist(
        bed=str(test_paths["bed"]),
        dict=str(test_paths["dict"]),
        interval_list=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule bedtointervallist:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify required inputs and outputs
    assert "bed=" in content, "Missing 'bed' input parameter"
    assert "dict=" in content, "Missing 'dict' input parameter"
    assert "interval_list=" in content, "Missing 'interval_list' output parameter"


def test_run_bedtointervallist(test_paths, tmp_path):
    """Test that bedtointervallist can be run with the test files."""
    from tools.picard.bedtointervallist.run_bedtointervallist import run_bedtointervallist
    temp_output = tmp_path / "output.interval_list"

    result = run_bedtointervallist(
        bed=str(test_paths["bed"]),
        dict=str(test_paths["dict"]),
        interval_list=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "bedtointervallist run failed"

    # Verify the output file is generated
    assert temp_output.exists(), "Output interval_list file was not generated"

    # Optional: Verify the contents of the output file (if format is known)
    with open(temp_output, "r") as output, open(test_paths["expected_interval_list"], "r") as expected:
        assert output.read() == expected.read(), "Output file content does not match expected output"