import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.vcf",
        "output_file": test_dir / "test_output.stats",
        "expected_snakefile": test_dir / "expected_snakefile"
    }


def test_snakefile_stats(test_paths, tmp_path, capsys):
    """Test that stats generates the expected Snakefile."""
    from tools.stats.mcp.run_stats import run_stats
    temp_output = tmp_path / "output.stats"

    # Generate the Snakefile with print_only=True to capture the content
    run_stats(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule stats:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"input_file='{test_paths['input_file']}'" in content, "Missing input_file parameter"
    assert f"output_file='{temp_output}'" in content, "Missing output_file parameter"


def test_run_stats(test_paths, tmp_path):
    """Test that stats can be run with the test files."""
    from tools.stats.mcp.run_stats import run_stats
    temp_output = tmp_path / "output.stats"

    result = run_stats(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "stats run failed"

    # Verify that output file is created
    assert temp_output.exists(), "Output stats file was not created"