import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_data_dir = base_dir / "test_data"
    return {
        "bam_file": test_data_dir / "input.bam",
        "ref_flat": test_data_dir / "input.ref_flat",
        "gc_metrics_txt": test_data_dir / "output.gc_metrics.txt",
        "gc_metrics_pdf": test_data_dir / "output.gc_metrics.pdf",
        "gc_summary_txt": test_data_dir / "output.gc_summary.txt",
    }


def test_snakefile_collectgcbiasmetrics(test_paths, tmp_path, capsys):
    """Test that collectgcbiasmetrics generates the expected Snakefile."""
    from bioinformatics_mcp.picard.collectgcbiasmetrics.run_collectgcbiasmetrics import run_collectgcbiasmetrics

    run_collectgcbiasmetrics(
        bam_file=str(test_paths["bam_file"]),
        ref_flat=str(test_paths["ref_flat"]),
        gc_metrics_txt=str(test_paths["gc_metrics_txt"]),
        gc_metrics_pdf=str(test_paths["gc_metrics_pdf"]),
        gc_summary_txt=str(test_paths["gc_summary_txt"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule collectgcbiasmetrics:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam_file=" in content, "Missing bam_file parameter in input"
    assert "ref_flat=" in content, "Missing ref_flat parameter in input"
    assert "gc_metrics_txt=" in content, "Missing gc_metrics_txt parameter in output"
    assert "gc_metrics_pdf=" in content, "Missing gc_metrics_pdf parameter in output"
    assert "gc_summary_txt=" in content, "Missing gc_summary_txt parameter in output"


def test_run_collectgcbiasmetrics(test_paths, tmp_path):
    """Test that collectgcbiasmetrics can be run with the test files."""
    from bioinformatics_mcp.picard.collectgcbiasmetrics.run_collectgcbiasmetrics import run_collectgcbiasmetrics

    temp_gc_metrics_txt = tmp_path / "output.gc_metrics.txt"
    temp_gc_metrics_pdf = tmp_path / "output.gc_metrics.pdf"
    temp_gc_summary_txt = tmp_path / "output.gc_summary.txt"

    result = run_collectgcbiasmetrics(
        bam_file=str(test_paths["bam_file"]),
        ref_flat=str(test_paths["ref_flat"]),
        gc_metrics_txt=str(temp_gc_metrics_txt),
        gc_metrics_pdf=str(temp_gc_metrics_pdf),
        gc_summary_txt=str(temp_gc_summary_txt),
    )

    assert result.returncode == 0, "collectgcbiasmetrics run failed"
    assert temp_gc_metrics_txt.exists(), "GC metrics text output file not created"
    assert temp_gc_metrics_pdf.exists(), "GC metrics PDF output file not created"
    assert temp_gc_summary_txt.exists(), "GC summary text output file not created"