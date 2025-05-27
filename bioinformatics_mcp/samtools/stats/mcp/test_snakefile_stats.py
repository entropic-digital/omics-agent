import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.bam",
        "expected_output": test_dir / "expected_output.stats",
    }


def test_snakefile_stats(test_paths, tmp_path, capsys):
    """Test that stats generates the expected Snakefile."""
    from bioinformatics_mcp.samtools.stats.run_stats import run_stats

    temp_output = tmp_path / "output.stats"

    # Generate the Snakefile with print_only=True to capture the content
    run_stats(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule stats:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f"'{test_paths['input_file']}'" in content, "Input file missing in Snakefile"
    assert f"'{temp_output}'" in content, "Output file missing in Snakefile"


def test_run_stats(test_paths, tmp_path):
    """Test that stats can be run with the test files."""
    from bioinformatics_mcp.samtools.stats.run_stats import run_stats

    temp_output = tmp_path / "output.stats"

    result = run_stats(
        input_file=str(test_paths["input_file"]), output_file=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "stats run failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"
