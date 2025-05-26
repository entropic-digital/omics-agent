import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bus_file": test_dir / "input.bus",
        "expected_sorted_bus_file": test_dir / "sorted_output.bus",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_sort(test_paths, tmp_path, capsys):
    """Test that sort generates the expected Snakefile."""
    from tools.bustools.sort.run_sort import run_sort

    temp_output = tmp_path / "output.bus"

    run_sort(
        input_bus_files=str(test_paths["input_bus_file"]),
        output_bus_file=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule sort:" in content, "Missing 'rule sort:' definition in Snakefile"
    assert "input:" in content, "Missing 'input:' section in Snakefile"
    assert "output:" in content, "Missing 'output:' section in Snakefile"
    assert "wrapper:" in content, "Missing 'wrapper:' section in Snakefile"
    assert "bus_files=" in content, "Missing 'bus_files=' parameter in input section"
    assert "sorted_bus_file=" in content, "Missing 'sorted_bus_file=' parameter in output section"


def test_run_sort(test_paths, tmp_path):
    """Test that sort can be executed with test files."""
    from tools.bustools.sort.run_sort import run_sort

    temp_output = tmp_path / "output.bus"

    result = run_sort(
        input_bus_files=str(test_paths["input_bus_file"]),
        output_bus_file=str(temp_output)
    )

    assert result.returncode == 0, "Sort execution failed"
    assert temp_output.exists(), "Sorted BUS file was not created"
    assert temp_output.stat().st_size > 0, "Sorted BUS file is empty"