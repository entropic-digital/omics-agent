import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "aln": test_dir / "test.aln.bam",
        "refgene": test_dir / "test.refgene.txt",
        "reads_inner_distance": test_dir / "reads_inner_distance.tsv",
        "pdf": test_dir / "output.pdf",
        "plot_r": test_dir / "plot.R",
        "freq": test_dir / "freq.txt"
    }


def test_snakefile_inner_distance(test_paths, tmp_path, capsys):
    """Test that inner_distance generates the expected Snakefile."""
    from bioinformatics_mcp.rseqc.inner_distance.run_inner_distance import run_inner_distance

    # Generate the Snakefile with print_only=True
    run_inner_distance(
        aln=str(test_paths["aln"]),
        refgene=str(test_paths["refgene"]),
        reads_inner_distance=str(test_paths["reads_inner_distance"]),
        pdf=str(test_paths["pdf"]),
        plot_r=str(test_paths["plot_r"]),
        freq=str(test_paths["freq"]),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule inner_distance:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify the input parameters
    assert "aln=" in content, "Missing aln input parameter"
    assert "refgene=" in content, "Missing refgene input parameter"

    # Verify the output parameters
    assert "reads_inner_distance=" in content, "Missing reads_inner_distance output"
    assert "pdf=" in content, "Missing pdf output"
    assert "plot_r=" in content, "Missing plot_r output"
    assert "freq=" in content, "Missing freq output"


def test_run_inner_distance(test_paths, tmp_path):
    """Test executing the inner_distance tool with test files."""
    from bioinformatics_mcp.rseqc.inner_distance.run_inner_distance import run_inner_distance

    temp_reads_inner_distance = tmp_path / "reads_inner_distance.tsv"
    temp_pdf = tmp_path / "output.pdf"
    temp_plot_r = tmp_path / "plot.R"
    temp_freq = tmp_path / "freq.txt"

    # Run the tool with test files
    result = run_inner_distance(
        aln=str(test_paths["aln"]),
        refgene=str(test_paths["refgene"]),
        reads_inner_distance=str(temp_reads_inner_distance),
        pdf=str(temp_pdf),
        plot_r=str(temp_plot_r),
        freq=str(temp_freq)
    )

    # Verify the process completed successfully
    assert result.returncode == 0, "inner_distance run failed"
    assert temp_reads_inner_distance.exists(), "Missing reads_inner_distance output file"
    assert temp_pdf.exists(), "Missing pdf output file"
    assert temp_plot_r.exists(), "Missing plot_r output file"
    assert temp_freq.exists(), "Missing freq output file"