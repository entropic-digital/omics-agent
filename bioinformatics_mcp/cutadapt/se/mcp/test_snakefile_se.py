import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test_data"
    return {
        "fastq": test_dir / "sample.fastq",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "trimmed_fastq": test_dir / "output_trimmed.fastq",
        "stats": test_dir / "output_stats.txt",
    }


def test_snakefile_se(test_paths, tmp_path, capsys):
    """Test Snakefile generation for cutadapt-se."""
    from bioinformatics_mcp.cutadapt_se.mcp.run_se import run_se

    run_se(
        fastq_file=str(test_paths["fastq"]),
        trimmed_fastq_file=tmp_path / "trimmed.fastq",
        stats_file=tmp_path / "stats.txt",
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule cutadapt_se:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper directive"
    assert "fastq=" in content, "Missing input fastq parameter"
    assert "trimmed_fastq=" in content, "Missing output trimmed_fastq parameter"
    assert "stats=" in content, "Missing output stats parameter"


def test_run_se(test_paths, tmp_path):
    """Test tool execution for cutadapt-se."""
    from bioinformatics_mcp.cutadapt_se.mcp.run_se import run_se

    trimmed_fastq = tmp_path / "trimmed.fastq"
    stats_file = tmp_path / "stats.txt"

    result = run_se(
        fastq_file=str(test_paths["fastq"]),
        trimmed_fastq_file=str(trimmed_fastq),
        stats_file=str(stats_file),
    )

    assert result.returncode == 0, "cutadapt-se run failed"
    assert trimmed_fastq.exists(), "Trimmed FASTQ file not generated"
    assert stats_file.exists(), "Statistics file not generated"