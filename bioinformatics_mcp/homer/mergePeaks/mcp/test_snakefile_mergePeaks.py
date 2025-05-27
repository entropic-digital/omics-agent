"""Tests for the mergePeaks Snakefile and execution"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input1": test_dir / "test_peaks1.bed",
        "input2": test_dir / "test_peaks2.bed",
        "expected_output": test_dir / "expected_output.bed",
        "temp_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_mergePeaks(test_paths, tmp_path, capsys):
    """Test that mergePeaks generates the expected Snakefile."""
    from bioinformatics_mcp.homer.mergePeaks.run_mergePeaks import run_mergePeaks

    temp_output = tmp_path / "merged_peaks.bed"

    # Generate the Snakefile with print_only=True to capture the content
    run_mergePeaks(
        input_files=f"{test_paths['input1']} {test_paths['input2']}",
        output_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential elements are in the Snakefile
    assert "rule mergePeaks:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert str(test_paths["input1"]) in content, "Input file 1 missing in Snakefile"
    assert str(test_paths["input2"]) in content, "Input file 2 missing in Snakefile"
    assert str(temp_output) in content, "Output file missing in Snakefile"


def test_run_mergePeaks(test_paths, tmp_path):
    """Test that mergePeaks can be run with the test files."""
    from bioinformatics_mcp.homer.mergePeaks.run_mergePeaks import run_mergePeaks

    temp_output = tmp_path / "merged_peaks.bed"

    # Execute the mergePeaks tool
    result = run_mergePeaks(
        input_files=f"{test_paths['input1']} {test_paths['input2']}",
        output_file=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "mergePeaks run failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"
