import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "genome": test_dir / "test_genome.fa",
        "bismark_genome_dir": test_dir / "bismark_index_dir",
    }


def test_snakefile_bismark_genome_preparation(test_paths, tmp_path, capsys):
    """Test that bismark_genome_preparation generates the expected Snakefile."""
    from tools.bismark_genome_preparation.mcp.run_bismark_genome_preparation import run_bismark_genome_preparation

    temp_output_dir = tmp_path / "bismark_index_dir"
    temp_output_dir.mkdir()

    run_bismark_genome_preparation(
        genome=str(test_paths["genome"]),
        bismark_genome_dir=str(temp_output_dir),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out.strip()

    assert "rule bismark_genome_preparation:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f'genome="{test_paths["genome"]}"' in content, "Missing correct genome input parameter"
    assert f'bismark_genome_dir="{str(temp_output_dir)}"' in content, "Missing correct output directory parameter"


def test_run_bismark_genome_preparation(test_paths, tmp_path):
    """Test that bismark_genome_preparation can be run with the test files."""
    from tools.bismark_genome_preparation.mcp.run_bismark_genome_preparation import run_bismark_genome_preparation

    temp_output_dir = tmp_path / "bismark_index_dir"
    temp_output_dir.mkdir()

    result = run_bismark_genome_preparation(
        genome=str(test_paths["genome"]),
        bismark_genome_dir=str(temp_output_dir)
    )

    assert result.returncode == 0, "bismark_genome_preparation run failed"
    assert temp_output_dir.exists(), "Bismark output directory does not exist"
    assert any(temp_output_dir.iterdir()), "Bismark output directory is empty"