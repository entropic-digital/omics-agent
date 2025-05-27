import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam1": test_dir / "input1.bam",
        "input_bam2": test_dir / "input2.bam",
        "expected_snakefile": test_dir / "Snakefile",
        "expected_output": test_dir / "merged.bam",
    }


def test_snakefile_merge(test_paths, tmp_path, capsys):
    """Test that sambamba merge generates the expected Snakefile."""
    from bioinformatics_mcp.sambamba.merge.run_merge import run_merge
    temp_output = tmp_path / "merged_output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_merge(
        sorted_bam_files=[str(test_paths["input_bam1"]), str(test_paths["input_bam2"])],
        merged_bam_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule sambamba_merge:" in content, "Missing rule definition for sambamba_merge"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Add assertions for all required input parameters
    assert "sorted_bam_files=" in content, "Missing sorted_bam_files parameter"
    # Add assertions for all required output parameters
    assert "merged_bam_file=" in content, "Missing merged_bam_file parameter"


def test_run_merge(test_paths, tmp_path):
    """Test that sambamba merge can be run with the test files."""
    from bioinformatics_mcp.sambamba.merge.run_merge import run_merge
    temp_output = tmp_path / "merged_output.bam"

    result = run_merge(
        sorted_bam_files=[str(test_paths["input_bam1"]), str(test_paths["input_bam2"])],
        merged_bam_file=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "sambamba_merge run failed"
    # Verify that the merged file was created
    assert temp_output.exists(), "Merged BAM file was not created"
    # Optionally, you may add file content verifications if necessary