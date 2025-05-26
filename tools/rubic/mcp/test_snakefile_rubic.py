import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test file paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test" / "rubic"
    output_dir = base_dir / "output"
    return {
        "seg": test_dir / "test.seg",
        "markers": test_dir / "test.markers",
        "genefile": test_dir / "test.genefile",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "out_gains": output_dir / "out_gains.txt",
        "out_losses": output_dir / "out_losses.txt",
        "out_plots": output_dir / "plots"
    }

def test_snakefile_rubic(test_paths, tmp_path, capsys):
    """Test Snakefile generation for rubic."""
    from tools.rubic.mcp.run_rubic import run_rubic

    run_rubic(
        seg=str(test_paths["seg"]),
        markers=str(test_paths["markers"]),
        genefile=str(test_paths["genefile"]),
        out_gains=str(tmp_path / "out_gains.txt"),
        out_losses=str(tmp_path / "out_losses.txt"),
        out_plots=str(tmp_path / "plots"),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule rubic:" in content, "Missing 'rubic' rule definition"
    assert "input:" in content, "Missing `input` section in Snakefile"
    assert "output:" in content, "Missing `output` section in Snakefile"
    assert "params:" in content, "Missing `params` section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper directive in Snakefile"
    assert "seg=" in content, "Missing 'seg' input parameter in Snakefile"
    assert "markers=" in content, "Missing 'markers' input parameter in Snakefile"
    assert "genefile=" in content, "Missing 'genefile' input parameter in Snakefile"
    assert "out_gains=" in content, "Missing 'out_gains' output in Snakefile"
    assert "out_losses=" in content, "Missing 'out_losses' output in Snakefile"
    assert "out_plots=" in content, "Missing 'out_plots' output in Snakefile"

def test_run_rubic(test_paths, tmp_path):
    """Test execution of rubic tool."""
    from tools.rubic.mcp.run_rubic import run_rubic

    out_gains = tmp_path / "out_gains.txt"
    out_losses = tmp_path / "out_losses.txt"
    out_plots = tmp_path / "plots"

    result = run_rubic(
        seg=str(test_paths["seg"]),
        markers=str(test_paths["markers"]),
        genefile=str(test_paths["genefile"]),
        out_gains=str(out_gains),
        out_losses=str(out_losses),
        out_plots=str(out_plots)
    )

    assert result.returncode == 0, "RUBIC execution failed"
    assert out_gains.exists(), "Expected output file for gains is missing"
    assert out_losses.exists(), "Expected output file for losses is missing"
    assert out_plots.exists() and out_plots.is_dir(), "Expected output plots directory is missing or invalid"