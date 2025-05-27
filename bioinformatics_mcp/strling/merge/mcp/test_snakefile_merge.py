"""Module that tests if the strling merge Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "input_files": test_dir / "input_files.txt",
        "sample_names": test_dir / "sample_names.txt",
        "regions_bed": test_dir / "regions.bed",
        "expected_snakefile": test_dir / "Snakefile",
        "output_file": test_dir / "output.txt",
    }


def test_snakefile_merge(test_paths, tmp_path, capsys):
    """Test that strling merge generates the expected Snakefile."""
    from run_merge import run_merge

    temp_output = tmp_path / "output.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_merge(
        input_files=str(test_paths["input_files"]),
        output_file=str(temp_output),
        min_evidence=10,
        sample_names=str(test_paths["sample_names"]),
        regions_bed=str(test_paths["regions_bed"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the Snakefile
    assert "rule merge:" in content, "Missing rule definition for 'merge'"
    assert "input:" in content, "Missing input section in the Snakefile"
    assert "output:" in content, "Missing output section in the Snakefile"
    assert "params:" in content, "Missing params section in the Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in the Snakefile"

    # Assert required input parameters are present
    assert "input_files=" in content, "Missing 'input_files' parameter in Snakefile"
    assert "sample_names=" in content, "Missing 'sample_names' parameter in Snakefile"
    assert "regions_bed=" in content, "Missing 'regions_bed' parameter in Snakefile"

    # Assert required output parameter is present
    assert "output_file=" in content, "Missing 'output_file' parameter in Snakefile"

    # Assert required params are present
    assert "min_evidence=" in content, "Missing 'min_evidence' parameter in Snakefile"


def test_run_merge(test_paths, tmp_path):
    """Test that strling merge runs successfully with test data."""
    from run_merge import run_merge

    temp_output = tmp_path / "output.txt"

    result = run_merge(
        input_files=str(test_paths["input_files"]),
        output_file=str(temp_output),
        min_evidence=10,
        sample_names=str(test_paths["sample_names"]),
        regions_bed=str(test_paths["regions_bed"]),
    )

    # Verify that the run is successful
    assert result.returncode == 0, (
        f"strling merge run failed with return code {result.returncode}"
    )

    # Verify that the output file is created
    assert temp_output.exists(), "Output file was not created by strling merge"
