import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "mcool_file": test_dir / "test_input.mcool",
        "view_file": test_dir / "test_view.bed",
        "output_tsv": test_dir / "output_test.tsv",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_expected_trans(test_paths, tmp_path, capsys):
    """Test that the expected_trans Snakefile is generated correctly."""
    from tools.cooltools.expected_trans.mcp.run_expected_trans import run_expected_trans
    temp_output_tsv = tmp_path / "output_test.tsv"

    run_expected_trans(
        mcool_file=str(test_paths["mcool_file"]),
        output_tsv=str(temp_output_tsv),
        resolution="100000",
        view_file=str(test_paths["view_file"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements of the Snakefile
    assert "rule expected_trans:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    
    # Verify inputs
    assert "mcool_file=" in content, "Missing mcool_file parameter in Snakefile input"
    assert "view_file=" in content, "Missing optional view_file parameter in Snakefile input"
    
    # Verify outputs
    assert "output_tsv=" in content, "Missing output_tsv parameter in Snakefile output"
    
    # Verify params
    assert "resolution=" in content, "Missing resolution parameter in Snakefile params"
    assert "extra=" in content or "params:" in content, "Missing extra parameters in Snakefile params"


def test_run_expected_trans(test_paths, tmp_path):
    """Test the execution of the expected_trans tool."""
    from tools.cooltools.expected_trans.mcp.run_expected_trans import run_expected_trans
    
    temp_output_tsv = tmp_path / "output_test.tsv"

    result = run_expected_trans(
        mcool_file=str(test_paths["mcool_file"]),
        output_tsv=str(temp_output_tsv),
        resolution="100000",
        view_file=None,
    )

    # Verify execution success
    assert result.returncode == 0, "expected_trans execution failed"

    # Verify output file is created
    assert temp_output_tsv.exists(), "Output TSV file was not created"
    assert temp_output_tsv.stat().st_size > 0, "Output TSV file is empty"