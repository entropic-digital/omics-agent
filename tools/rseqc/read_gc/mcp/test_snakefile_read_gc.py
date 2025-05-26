import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "test.bam",
        "expected_snakefile": test_dir / "Snakefile",
        "expected_xls": test_dir / "expected_output.xls",
        "expected_plot_r": test_dir / "expected_plot.r",
        "expected_pdf": test_dir / "expected_output.pdf"
    }

def test_snakefile_read_gc(test_paths, tmp_path, capsys):
    """Test that read_gc generates the expected Snakefile."""
    from tools.rseqc.read_gc.mcp.run_read_gc import run_read_gc
    temp_xls = tmp_path / "output.xls"
    temp_plot_r = tmp_path / "plot.r"
    temp_pdf = tmp_path / "output.pdf"

    # Generate the Snakefile with print_only=True to capture the content
    run_read_gc(
        input_file=str(test_paths["input_bam"]),
        xls=str(temp_xls),
        plot_r=str(temp_plot_r),
        pdf=str(temp_pdf),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present in the generated Snakefile
    assert "rule read_gc:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"'{test_paths['input_bam']}'" in content, "Missing input file"
    assert f"'{temp_xls}'" in content, "Missing xls output file"
    assert f"'{temp_plot_r}'" in content, "Missing plot R output file"
    assert f"'{temp_pdf}'" in content, "Missing PDF output file"

def test_run_read_gc(test_paths, tmp_path):
    """Test that read_gc can be executed with the test files."""
    from tools.rseqc.read_gc.mcp.run_read_gc import run_read_gc
    temp_xls = tmp_path / "output.xls"
    temp_plot_r = tmp_path / "plot.r"
    temp_pdf = tmp_path / "output.pdf"

    # Execute the tool with test input and temporary output paths
    result = run_read_gc(
        input_file=str(test_paths["input_bam"]),
        xls=str(temp_xls),
        plot_r=str(temp_plot_r),
        pdf=str(temp_pdf)
    )

    # Verify the process returns successfully
    assert result.returncode == 0, "read_gc process failed to run successfully"

    # Verify the files are generated
    assert temp_xls.exists(), f"Expected xls output file not generated: {temp_xls}"
    assert temp_plot_r.exists(), f"Expected plot R output file not generated: {temp_plot_r}"
    assert temp_pdf.exists(), f"Expected PDF output file not generated: {temp_pdf}"