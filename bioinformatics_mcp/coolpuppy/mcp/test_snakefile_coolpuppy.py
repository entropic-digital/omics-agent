import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "mcool_file": test_dir / "example.mcool",
        "features_file": test_dir / "features.bed",
        "expected_file": test_dir / "expected.txt",
        "view_file": test_dir / "view.bed",
        "output_file": test_dir / "output.clpy",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_coolpuppy(test_paths, tmp_path, capsys):
    """Test that coolpuppy generates the expected Snakefile."""
    from bioinformatics_mcp.coolpuppy.mcp.run_coolpuppy import run_coolpuppy
    temp_output = tmp_path / "output.clpy"

    run_coolpuppy(
        mcool_file=str(test_paths["mcool_file"]),
        features_file=str(test_paths["features_file"]),
        expected_file=str(test_paths["expected_file"]),
        view_file=str(test_paths["view_file"]),
        output_file=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule coolpuppy:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "mcool_file=" in content, "Missing mcool_file parameter"
    assert "features_file=" in content, "Missing features_file parameter"
    assert "expected_file=" in content, "Missing expected_file parameter"
    assert "view_file=" in content, "Missing view_file parameter"
    assert "output_file=" in content, "Missing output_file parameter"


def test_run_coolpuppy(test_paths, tmp_path):
    """Test that coolpuppy can be run with the test files."""
    from bioinformatics_mcp.coolpuppy.mcp.run_coolpuppy import run_coolpuppy
    temp_output = tmp_path / "output.clpy"

    result = run_coolpuppy(
        mcool_file=str(test_paths["mcool_file"]),
        features_file=str(test_paths["features_file"]),
        output_file=str(temp_output),
        expected_file=str(test_paths["expected_file"]),
        view_file=str(test_paths["view_file"]),
    )

    assert result.returncode == 0, "coolpuppy run failed"
    assert temp_output.exists(), "Output file was not created"