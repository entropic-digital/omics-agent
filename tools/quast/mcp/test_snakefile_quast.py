import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "sequences": test_dir / "test_sequences.fasta",
        "reference_genome": test_dir / "test_reference.fasta",
        "assessment_summary": test_dir / "assessment_summary.txt",
        "tab_summary": test_dir / "tab_summary.txt",
        "latex_summary": test_dir / "latex_summary.tex",
        "icarus_menu": test_dir / "icarus_menu.html",
        "pdf_report": test_dir / "report.pdf",
        "html_report": test_dir / "report.html",
        "misassemblies_report": test_dir / "misassemblies.txt",
        "unaligned_contigs_report": test_dir / "unaligned_contigs.txt",
        "kmer_metrics_report": test_dir / "kmer_metrics.txt",
        "mapped_reads_stats_report": test_dir / "mapped_reads_stats.txt",
    }


def test_snakefile_quast(test_paths, tmp_path, capsys):
    """Test that quast generates the expected Snakefile."""
    from tools.quast.mcp.run_quast import run_quast

    # Generate the Snakefile with print_only=True to capture the content
    run_quast(
        sequences=str(test_paths["sequences"]),
        assessment_summary=str(test_paths["assessment_summary"]),
        tab_summary=str(test_paths["tab_summary"]),
        latex_summary=str(test_paths["latex_summary"]),
        icarus_menu=str(test_paths["icarus_menu"]),
        pdf_report=str(test_paths["pdf_report"]),
        html_report=str(test_paths["html_report"]),
        misassemblies_report=str(test_paths["misassemblies_report"]),
        unaligned_contigs_report=str(test_paths["unaligned_contigs_report"]),
        kmer_metrics_report=str(test_paths["kmer_metrics_report"]),
        mapped_reads_stats_report=str(test_paths["mapped_reads_stats_report"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements are present
    assert "rule quast:" in content, "Missing rule definition for `quast`"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper directive in Snakefile"

    # Verify all required inputs are defined
    assert "sequences=" in content, "Missing `sequences` input"
    assert "reference_genome=" in content or "None" in content, (
        "Missing `reference_genome` input"
    )

    # Verify all required outputs are defined
    assert "assessment_summary=" in content, "Missing `assessment_summary` output"
    assert "tab_summary=" in content, "Missing `tab_summary` output"
    assert "latex_summary=" in content, "Missing `latex_summary` output"
    assert "icarus_menu=" in content, "Missing `icarus_menu` output"
    assert "pdf_report=" in content, "Missing `pdf_report` output"
    assert "html_report=" in content, "Missing `html_report` output"
    assert "misassemblies_report=" in content, "Missing `misassemblies_report` output"
    assert "unaligned_contigs_report=" in content, (
        "Missing `unaligned_contigs_report` output"
    )
    assert "kmer_metrics_report=" in content, "Missing `kmer_metrics_report` output"
    assert "mapped_reads_stats_report=" in content, (
        "Missing `mapped_reads_stats_report` output"
    )


def test_run_quast(test_paths, tmp_path):
    """Test that quast can be run with the test files."""
    from tools.quast.mcp.run_quast import run_quast

    temp_outputs = {
        "assessment_summary": tmp_path / "assessment_summary.txt",
        "tab_summary": tmp_path / "tab_summary.txt",
        "latex_summary": tmp_path / "latex_summary.tex",
        "icarus_menu": tmp_path / "icarus_menu.html",
        "pdf_report": tmp_path / "report.pdf",
        "html_report": tmp_path / "report.html",
        "misassemblies_report": tmp_path / "misassemblies.txt",
        "unaligned_contigs_report": tmp_path / "unaligned_contigs.txt",
        "kmer_metrics_report": tmp_path / "kmer_metrics.txt",
        "mapped_reads_stats_report": tmp_path / "mapped_reads_stats.txt",
    }

    # Run the quast tool
    result = run_quast(
        sequences=str(test_paths["sequences"]),
        assessment_summary=str(temp_outputs["assessment_summary"]),
        tab_summary=str(temp_outputs["tab_summary"]),
        latex_summary=str(temp_outputs["latex_summary"]),
        icarus_menu=str(temp_outputs["icarus_menu"]),
        pdf_report=str(temp_outputs["pdf_report"]),
        html_report=str(temp_outputs["html_report"]),
        misassemblies_report=str(temp_outputs["misassemblies_report"]),
        unaligned_contigs_report=str(temp_outputs["unaligned_contigs_report"]),
        kmer_metrics_report=str(temp_outputs["kmer_metrics_report"]),
        mapped_reads_stats_report=str(temp_outputs["mapped_reads_stats_report"]),
    )

    # Verify the run completed successfully
    assert result.returncode == 0, "quast execution failed"

    # Verify all outputs were generated
    for output_name, output_path in temp_outputs.items():
        assert output_path.exists(), f"Output file `{output_name}` was not generated"
