import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "mapped_reads": test_dir / "test_mapped_reads.paf",
        "coverage": test_dir / "test_coverage.txt",
        "stats": test_dir / "test_stats.txt",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_pbcstat(test_paths, tmp_path, capsys):
    """Test that the pbcstat Snakefile is generated correctly."""
    from tools.purge_dups.mcp.run_pbcstat import run_pbcstat

    run_pbcstat(
        mapped_reads=str(test_paths["mapped_reads"]),
        coverage=str(test_paths["coverage"]),
        stats=str(test_paths["stats"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule pbcstat:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    assert f"mapped_reads='{test_paths['mapped_reads']}'" in content, "Missing mapped_reads input parameter"
    assert f"coverage='{test_paths['coverage']}'" in content, "Missing coverage output parameter"
    assert f"stats='{test_paths['stats']}'" in content, "Missing stats output parameter"


def test_run_pbcstat(test_paths, tmp_path):
    """Test that the pbcstat tool executes correctly."""
    from tools.purge_dups.mcp.run_pbcstat import run_pbcstat

    temp_coverage = tmp_path / "coverage.txt"
    temp_stats = tmp_path / "stats.txt"

    result = run_pbcstat(
        mapped_reads=str(test_paths["mapped_reads"]),
        coverage=str(temp_coverage),
        stats=str(temp_stats),
    )

    assert result.returncode == 0, "pbcstat execution failed"
    assert temp_coverage.exists(), "Coverage output file was not created"
    assert temp_stats.exists(), "Stats output file was not created"