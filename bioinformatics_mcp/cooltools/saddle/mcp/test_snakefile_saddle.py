import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "cooler_file": test_dir / "test.mcool",
        "track_file": test_dir / "track.bed",
        "expected_file": test_dir / "expected.tsv",
        "view_file": test_dir / "view.bed",
        "output_prefix": test_dir / "output_prefix",
    }


def test_snakefile_saddle(test_paths, tmp_path, capsys):
    """Test that the saddle Snakefile is generated correctly."""
    from bioinformatics_mcp.cooltools.saddle.mcp.run_saddle import run_saddle

    run_saddle(
        cooler_file=str(test_paths["cooler_file"]),
        track_file=str(test_paths["track_file"]),
        expected_file=str(test_paths["expected_file"]),
        output_prefix=str(tmp_path / "output"),
        view_file=str(test_paths["view_file"]),
        resolution=100000,
        range="--qrange 0.01 0.99",
        extra="--fig",
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule saddle:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    assert "cooler_file=" in content, "Missing cooler_file parameter in Snakefile"
    assert "track_file=" in content, "Missing track_file parameter in Snakefile"
    assert "expected_file=" in content, "Missing expected_file parameter in Snakefile"
    assert "view_file=" in content, "Missing view_file parameter in Snakefile"
    assert "output_prefix=" in content, "Missing output_prefix parameter in Snakefile"
    assert "--qrange 0.01 0.99" in content, "Missing range parameter in Snakefile"
    assert "--fig" in content, "Missing extra parameter in Snakefile"


def test_run_saddle(test_paths, tmp_path):
    """Test the execution of the saddle tool."""
    from bioinformatics_mcp.cooltools.saddle.mcp.run_saddle import run_saddle

    temp_output = tmp_path / "output"

    result = run_saddle(
        cooler_file=str(test_paths["cooler_file"]),
        track_file=str(test_paths["track_file"]),
        expected_file=str(test_paths["expected_file"]),
        output_prefix=str(temp_output),
        view_file=str(test_paths["view_file"]),
        resolution=100000,
        range="--qrange 0.01 0.99",
        extra="--fig",
    )

    assert result.returncode == 0, "Saddle tool execution failed"
    assert temp_output.with_suffix(".npz").exists(), "Expected .npz output file not generated"
    assert temp_output.with_suffix(".bed").exists(), "Expected .bed output file not generated"
    # Additional output validations can be added here if needed.