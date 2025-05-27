import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "stats_file": test_dir / "test.stats",
        "coverage_cut_offs": test_dir / "coverage_cut-offs.txt",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_split_fa(test_paths, tmp_path, capsys):
    """Test that split_fa generates the expected Snakefile."""
    from bioinformatics_mcp.purge_dups.split_fa.mcp.run_split_fa import run_split_fa

    run_split_fa(
        stats_file=str(test_paths["stats_file"]),
        coverage_cut_offs=str(test_paths["coverage_cut_offs"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule split_fa:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "stats_file=" in content, "Missing stats_file parameter"
    assert "coverage_cut_offs=" in content, "Missing coverage_cut_offs parameter"


def test_run_split_fa(test_paths, tmp_path):
    """Test that split_fa can be run with the test files."""
    from bioinformatics_mcp.purge_dups.split_fa.mcp.run_split_fa import run_split_fa
    temp_output = tmp_path / "coverage-cut-offs.txt"

    result = run_split_fa(
        stats_file=str(test_paths["stats_file"]),
        coverage_cut_offs=str(temp_output),
    )

    assert result.returncode == 0, "split_fa run failed"
    assert temp_output.exists(), "Expected output file was not created"