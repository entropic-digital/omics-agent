import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths for the read_duplication tool."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_file": test_dir / "test.bam",
        "expected_pos": test_dir / "expected_pos.txt",
        "expected_seq": test_dir / "expected_seq.txt",
        "expected_plot_r": test_dir / "expected_plot.R",
        "expected_pdf": test_dir / "expected_plot.pdf",
    }


def test_snakefile_read_duplication(test_paths, tmp_path, capsys):
    """Test that read_duplication generates the expected Snakefile."""
    from bioinformatics_mcp.rseqc.read_duplication.run_read_duplication import run_read_duplication

    run_read_duplication(
        input_file=str(test_paths["input_file"]),
        pos="pos.txt",
        seq="seq.txt",
        plot_r="plot.R",
        pdf="plot.pdf",
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule read_duplication:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    assert "input_file=" in content, "Missing input_file parameter"
    assert "output.pos=" in content, "Missing output.pos parameter"
    assert "output.seq=" in content, "Missing output.seq parameter"
    assert "output.plot_r=" in content, "Missing output.plot_r parameter"
    assert "output.pdf=" in content, "Missing output.pdf parameter"


def test_run_read_duplication(test_paths, tmp_path):
    """Test that the read_duplication tool can be executed."""
    from bioinformatics_mcp.rseqc.read_duplication.run_read_duplication import run_read_duplication

    temp_pos = tmp_path / "pos.txt"
    temp_seq = tmp_path / "seq.txt"
    temp_plot_r = tmp_path / "plot.R"
    temp_pdf = tmp_path / "plot.pdf"

    result = run_read_duplication(
        input_file=str(test_paths["input_file"]),
        pos=str(temp_pos),
        seq=str(temp_seq),
        plot_r=str(temp_plot_r),
        pdf=str(temp_pdf),
    )

    assert result.returncode == 0, "read_duplication run failed"
    assert temp_pos.exists(), "Expected output file for pos was not created"
    assert temp_seq.exists(), "Expected output file for seq was not created"
    assert temp_plot_r.exists(), "Expected output R script was not created"
    assert temp_pdf.exists(), "Expected output PDF was not created"
