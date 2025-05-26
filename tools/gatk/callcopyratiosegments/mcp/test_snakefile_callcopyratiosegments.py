import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "copy_ratio_seg": test_dir / "input.cr.seg",
        "copy_ratio_seg_out": test_dir / "expected_output.called.seg",
        "igv_seg": test_dir / "optional_output.igv.seg",
    }


def test_snakefile_callcopyratiosegments(test_paths, tmp_path, capsys):
    """Test that callcopyratiosegments generates the expected Snakefile."""
    from tools.gatk.callcopyratiosegments.mcp.run_callcopyratiosegments import run_callcopyratiosegments

    temp_output = tmp_path / "output.called.seg"
    temp_igv_output = tmp_path / "output.igv.seg"

    # Generate the Snakefile with print_only=True to capture the content
    run_callcopyratiosegments(
        copy_ratio_seg=str(test_paths["copy_ratio_seg"]),
        copy_ratio_seg_out=str(temp_output),
        igv_seg=str(temp_igv_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential parameters are present
    assert "rule callcopyratiosegments:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "copy_ratio_seg=" in content, "Missing copy_ratio_seg input parameter"
    assert "copy_ratio_seg_out=" in content, "Missing copy_ratio_seg_out output parameter"
    assert "igv_seg=" in content, "Missing igv_seg output parameter (optional)"
    assert "java_opts" in content, "Missing java_opts parameter"
    assert "extra" in content, "Missing extra parameter"


def test_run_callcopyratiosegments(test_paths, tmp_path):
    """Test that callcopyratiosegments runs successfully with test files."""
    from tools.gatk.callcopyratiosegments.mcp.run_callcopyratiosegments import run_callcopyratiosegments

    temp_output = tmp_path / "output.called.seg"
    temp_igv_output = tmp_path / "output.igv.seg"

    result = run_callcopyratiosegments(
        copy_ratio_seg=str(test_paths["copy_ratio_seg"]),
        copy_ratio_seg_out=str(temp_output),
        igv_seg=str(temp_igv_output),
    )

    # Verify that the run was successful
    assert result.returncode == 0, "callcopyratiosegments run failed"

    # Verify the output file was created
    assert temp_output.exists(), "Output file was not created"
    # Verify optional IGV output was created if specified
    if test_paths["igv_seg"]:
        assert temp_igv_output.exists(), "Optional IGV output file was not created"