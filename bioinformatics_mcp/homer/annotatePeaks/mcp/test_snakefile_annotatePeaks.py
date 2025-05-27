import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "peak_or_bed_file": test_dir / "peaks.bed",
        "optional_input_file": test_dir / "optional_input.gtf",
        "annotation_file": test_dir / "annotation.txt",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_annotatePeaks(test_paths, tmp_path, capsys):
    """Test that annotatePeaks generates the expected Snakefile."""
    from bioinformatics_mcp.homer.annotatePeaks.run_annotatePeaks import run_annotatePeaks
    temp_output = tmp_path / "output.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_annotatePeaks(
        peak_or_bed_file=str(test_paths["peak_or_bed_file"]),
        optional_input_file=str(test_paths["optional_input_file"]),
        annotation_file=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential Snakefile structure
    assert "rule annotatePeaks:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    # Verify required inputs
    assert f"peak_or_bed_file='{test_paths['peak_or_bed_file']}'" in content, "Missing 'peak_or_bed_file' input"
    assert f"optional_input_file='{test_paths['optional_input_file']}'" in content, "Missing 'optional_input_file' input"
    # Verify required outputs
    assert f"annotation_file='{temp_output}'" in content, "Missing 'annotation_file' output"

def test_run_annotatePeaks(test_paths, tmp_path):
    """Test that annotatePeaks can be run with the test files."""
    from bioinformatics_mcp.homer.annotatePeaks.run_annotatePeaks import run_annotatePeaks
    temp_output = tmp_path / "output.txt"

    result = run_annotatePeaks(
        peak_or_bed_file=str(test_paths["peak_or_bed_file"]),
        optional_input_file=str(test_paths["optional_input_file"]),
        annotation_file=str(temp_output)
    )

    # Verify that the process runs successfully
    assert result.returncode == 0, "annotatePeaks run failed"
    # Verify the output file is created
    assert temp_output.exists(), "Expected output file was not created"