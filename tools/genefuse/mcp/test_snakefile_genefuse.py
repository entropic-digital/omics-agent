import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fastq_files": test_dir / "test.fastq",
        "gene_fuse_settings": test_dir / "genefuse_settings.json",
        "reference_genome": test_dir / "reference_genome.fa",
        "txt_fusions": test_dir / "fusions.txt",
        "html_report": test_dir / "report.html",
        "json_report": test_dir / "report.json",
    }


def test_snakefile_genefuse(test_paths, tmp_path, capsys):
    """Test that genefuse generates the expected Snakefile."""
    from tools.genefuse.mcp.run_genefuse import run_genefuse

    run_genefuse(
        fastq_files=str(test_paths["fastq_files"]),
        gene_fuse_settings=str(test_paths["gene_fuse_settings"]),
        reference_genome=str(test_paths["reference_genome"]),
        txt_fusions=str(test_paths["txt_fusions"]),
        html_report=str(test_paths["html_report"]),
        json_report=str(test_paths["json_report"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule genefuse:" in content, "Missing rule definition."
    assert "input:" in content, "Missing input section."
    assert "output:" in content, "Missing output section."
    assert "params:" in content, "Missing params section."
    assert "wrapper:" in content, "Missing wrapper section."
    assert "fastq_files=" in content, "Missing fastq_files parameter."
    assert "gene_fuse_settings=" in content, "Missing gene_fuse_settings parameter."
    assert "reference_genome=" in content, "Missing reference_genome parameter."
    assert "txt_fusions=" in content, "Missing txt_fusions output."
    assert "html_report=" in content, "Missing html_report output."
    assert "json_report=" in content, "Missing json_report output."


def test_run_genefuse(test_paths, tmp_path):
    """Test that genefuse can be run with the test files."""
    from tools.genefuse.mcp.run_genefuse import run_genefuse

    txt_fusions = tmp_path / "fusions.txt"
    html_report = tmp_path / "report.html"
    json_report = tmp_path / "report.json"

    result = run_genefuse(
        fastq_files=str(test_paths["fastq_files"]),
        gene_fuse_settings=str(test_paths["gene_fuse_settings"]),
        reference_genome=str(test_paths["reference_genome"]),
        txt_fusions=str(txt_fusions),
        html_report=str(html_report),
        json_report=str(json_report),
    )

    assert result.returncode == 0, "genefuse run failed."
    assert txt_fusions.exists(), "TXT fusions output file missing."
    assert html_report.exists(), "HTML report output file missing."
    assert json_report.exists(), "JSON report output file missing."