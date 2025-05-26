import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "input.bam",
        "regions_file": test_dir / "regions.bed",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_depth(test_paths, tmp_path, capsys):
    """Test that depth generates the expected Snakefile."""
    from tools.samtools.depth.run_depth import run_depth
    temp_output = tmp_path / "output.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_depth(
        input_bam=str(test_paths["input_bam"]),
        output_file=str(temp_output),
        regions_file=str(test_paths["regions_file"]),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential params are present in the Snakefile
    assert "rule depth:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "input_bam=" in content, "Missing input_bam parameter"
    assert "output_file=" in content, "Missing output_file parameter"
    assert "regions_file=" in content or "regions_file=None" in content, "Missing or invalid regions_file parameter"


def test_run_depth(test_paths, tmp_path):
    """Test that depth can be run with the test files."""
    from tools.samtools.depth.run_depth import run_depth
    temp_output = tmp_path / "output.txt"

    result = run_depth(
        input_bam=str(test_paths["input_bam"]),
        output_file=str(temp_output),
        regions_file=str(test_paths["regions_file"]),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "depth run failed"

    # Check that the output file is created
    assert temp_output.exists(), "Output file not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"