import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fastq1": test_dir / "input1.fastq",
        "fastq2": test_dir / "input2.fastq",
        "trimmed_fastq1": test_dir / "output1_trimmed.fastq",
        "trimmed_fastq2": test_dir / "output2_trimmed.fastq",
        "json_stats": test_dir / "stats.json",
        "html_stats": test_dir / "stats.html",
    }

def test_snakefile_fastp(test_paths, tmp_path, capsys):
    """Test that fastp generates the expected Snakefile."""
    from bioinformatics_mcp.fastp.mcp.run_fastp import run_fastp
    temp_trimmed_fastq1 = str(tmp_path / "output1_trimmed.fastq")
    temp_trimmed_fastq2 = str(tmp_path / "output2_trimmed.fastq")
    temp_json_stats = str(tmp_path / "stats.json")
    temp_html_stats = str(tmp_path / "stats.html")

    run_fastp(
        fastq_files=[str(test_paths["fastq1"]), str(test_paths["fastq2"])],
        trimmed_fastq_files=[temp_trimmed_fastq1, temp_trimmed_fastq2],
        json_stats=temp_json_stats,
        html_stats=temp_html_stats,
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule fastp:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "fastq_files=" in content, "Missing fastq_files parameter"
    assert "trimmed_fastq_files=" in content, "Missing trimmed_fastq_files parameter"
    assert "json_stats=" in content, "Missing json_stats parameter"
    assert "html_stats=" in content, "Missing html_stats parameter"

def test_run_fastp(test_paths, tmp_path):
    """Test that fastp can be run with the test files."""
    from bioinformatics_mcp.fastp.mcp.run_fastp import run_fastp
    temp_trimmed_fastq1 = tmp_path / "output1_trimmed.fastq"
    temp_trimmed_fastq2 = tmp_path / "output2_trimmed.fastq"
    temp_json_stats = tmp_path / "stats.json"
    temp_html_stats = tmp_path / "stats.html"

    result = run_fastp(
        fastq_files=[str(test_paths["fastq1"]), str(test_paths["fastq2"])],
        trimmed_fastq_files=[str(temp_trimmed_fastq1), str(temp_trimmed_fastq2)],
        json_stats=str(temp_json_stats),
        html_stats=str(temp_html_stats)
    )

    assert result.returncode == 0, "fastp run failed"
    assert temp_trimmed_fastq1.exists(), "Trimmed output file 1 is missing"
    assert temp_trimmed_fastq2.exists(), "Trimmed output file 2 is missing"
    assert temp_json_stats.exists(), "JSON stats output file is missing"
    assert temp_html_stats.exists(), "HTML stats output file is missing"