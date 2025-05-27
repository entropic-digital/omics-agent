import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "mcool_file": test_dir / "test_input.mcool",
        "features_file": test_dir / "test_features.bed",
        "expected_file": test_dir / "test_expected.txt",
        "view_file": test_dir / "test_view.bed",
        "output_file": test_dir / "test_output.npz",
        "snakefile": test_dir / "Snakefile",
    }

def test_snakefile_pileup(test_paths, tmp_path, capsys):
    """Test that pileup generates the expected Snakefile."""
    from bioinformatics_mcp.cooltools.pileup.run_pileup import run_pileup
    temp_output = tmp_path / "output.npz"

    run_pileup(
        mcool_file=str(test_paths["mcool_file"]),
        features_file=str(test_paths["features_file"]),
        output_file=str(temp_output),
        resolution=10000,
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule pileup:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "mcool_file=" in content, "Missing mcool_file parameter"
    assert "features_file=" in content, "Missing features_file parameter"
    assert "output_file=" in content, "Missing output_file parameter"

    if test_paths["expected_file"].exists():
        assert "expected_file=" in content, "Missing expected_file parameter when expected_file is provided"
    if test_paths["view_file"].exists():
        assert "view_file=" in content, "Missing view_file parameter when view_file is provided"

def test_run_pileup(test_paths, tmp_path):
    """Test that pileup can be run with the test files."""
    from bioinformatics_mcp.cooltools.pileup.run_pileup import run_pileup
    temp_output = tmp_path / "output.npz"

    result = run_pileup(
        mcool_file=str(test_paths["mcool_file"]),
        features_file=str(test_paths["features_file"]),
        output_file=str(temp_output),
        resolution=10000,
        expected_file=str(test_paths["expected_file"]),
        view_file=str(test_paths["view_file"]),
    )

    assert result.returncode == 0, "pileup run failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"