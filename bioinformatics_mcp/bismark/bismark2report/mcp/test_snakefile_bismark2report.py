import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "alignment_report": test_dir / "alignment_report.txt",
        "nucleotide_report": test_dir / "nucleotide_report.txt",
        "dedup_report": test_dir / "deduplication_report.txt",
        "splitting_report": test_dir / "splitting_report.txt",
        "mbias_report": test_dir / "mbias_report.txt",
        "html": test_dir / "output.html",
        "html_dir": test_dir / "batch_output",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_bismark2report(test_paths, tmp_path, capsys):
    """Test that bismark2report generates the expected Snakefile."""
    from bioinformatics_mcp.bismark.bismark2report.run_bismark2report import run_bismark2report

    run_bismark2report(
        alignment_report=str(test_paths["alignment_report"]),
        nucleotide_report=str(test_paths["nucleotide_report"]),
        dedup_report=str(test_paths["dedup_report"]),
        splitting_report=str(test_paths["splitting_report"]),
        mbias_report=str(test_paths["mbias_report"]),
        html=str(test_paths["html"]),
        html_dir=str(test_paths["html_dir"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule bismark2report:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "alignment_report=" in content, "Missing alignment_report input"
    assert "nucleotide_report=" in content, "Missing nucleotide_report input"
    assert "dedup_report=" in content, "Missing dedup_report input"
    assert "splitting_report=" in content, "Missing splitting_report input"
    assert "mbias_report=" in content, "Missing mbias_report input"
    assert "html=" in content, "Missing html output"
    assert "html_dir=" in content, "Missing html_dir output"


def test_run_bismark2report(test_paths, tmp_path):
    """Test that bismark2report can be run with the test files."""
    from bioinformatics_mcp.bismark.bismark2report.run_bismark2report import run_bismark2report

    temp_output_html = tmp_path / "output.html"
    temp_output_html_dir = tmp_path / "batch_output"

    result = run_bismark2report(
        alignment_report=str(test_paths["alignment_report"]),
        nucleotide_report=str(test_paths["nucleotide_report"]),
        dedup_report=str(test_paths["dedup_report"]),
        splitting_report=str(test_paths["splitting_report"]),
        mbias_report=str(test_paths["mbias_report"]),
        html=str(temp_output_html),
        html_dir=str(temp_output_html_dir),
    )

    assert result.returncode == 0, "bismark2report execution failed"
    assert temp_output_html.exists(), "HTML output file was not generated"
    assert temp_output_html_dir.exists() and temp_output_html_dir.is_dir(), "HTML output directory was not generated"