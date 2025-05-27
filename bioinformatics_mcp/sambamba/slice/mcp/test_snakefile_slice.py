import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "bam_file": test_dir / "example.bam",
        "output_bam": test_dir / "output.bam",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_slice(test_paths, tmp_path, capsys):
    """Test that slice tool generates the expected Snakefile."""
    from bioinformatics_mcp.sambamba.slice.run_slice import run_slice
    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_slice(
        bam_file=str(test_paths["bam_file"]),
        output_bam=str(temp_output),
        region="chr1:1000-2000",
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule slice:" in content, "Snakefile missing 'rule slice' definition"
    assert "input:" in content, "Snakefile missing 'input' section"
    assert "output:" in content, "Snakefile missing 'output' section"
    assert "wrapper:" in content, "Snakefile missing 'wrapper' section"
    assert "bam_file=" in content, "Snakefile missing 'bam_file' input parameter"
    assert "output_bam=" in content, "Snakefile missing 'output_bam' output parameter"
    assert "params:" in content, "Snakefile missing 'params' section for region"
    assert "region=" in content, "Snakefile missing 'region' parameter"

def test_run_slice(test_paths, tmp_path):
    """Test that the slice tool can be run with the test files."""
    from bioinformatics_mcp.sambamba.slice.run_slice import run_slice
    temp_output = tmp_path / "output.bam"

    # Run the slice tool using test files
    result = run_slice(
        bam_file=str(test_paths["bam_file"]),
        output_bam=str(temp_output),
        region="chr1:1000-2000"
    )

    # Verify that the run is successful
    assert result.returncode == 0, "slice tool execution failed"
    assert temp_output.exists(), "Output BAM file was not created"
