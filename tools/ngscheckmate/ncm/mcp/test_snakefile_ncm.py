import pytest
from pathlib import Path
from tools.ngscheckmate.ncm.run_ncm import run_ncm


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "samples": test_dir / "samples_list.txt",
        "bed": test_dir / "regions.bed",
        "pt": test_dir / "pattern_file.txt",
        "pdf": test_dir / "output.pdf",
        "matched": test_dir / "matched_samples.tsv",
        "txt": test_dir / "description.txt",
        "matrix": test_dir / "metrics_matrix.tsv",
    }


def test_snakefile_ncm(test_paths, tmp_path, capsys):
    """Test that the ncm Snakefile is correctly generated with required rules and structure."""
    run_ncm(
        samples=str(test_paths["samples"]),
        bed=str(test_paths["bed"]),
        pt=str(test_paths["pt"]),
        pdf=str(test_paths["pdf"]),
        matched=str(test_paths["matched"]),
        txt=str(test_paths["txt"]),
        matrix=str(test_paths["matrix"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    snakefile_content = captured.out

    assert "rule ncm:" in snakefile_content, "Missing rule definition for ncm"
    assert "input:" in snakefile_content, "Missing input section"
    assert "output:" in snakefile_content, "Missing output section"
    assert "params:" in snakefile_content, "Missing params section"
    assert "wrapper:" in snakefile_content, "Missing wrapper section"
    assert "samples=" in snakefile_content, "Missing samples input in Snakefile"
    assert "pdf=" in snakefile_content, "Missing pdf output parameter in Snakefile"
    assert "matched=" in snakefile_content, "Missing matched output parameter in Snakefile"
    assert "txt=" in snakefile_content, "Missing txt output parameter in Snakefile"
    assert "matrix=" in snakefile_content, "Missing matrix output parameter in Snakefile"
    assert "bed=" in snakefile_content or "bed=None" in snakefile_content, "Missing or optional bed input in Snakefile"
    assert "pt=" in snakefile_content or "pt=None" in snakefile_content, "Missing or optional pt input in Snakefile"


def test_run_ncm(test_paths, tmp_path):
    """Test running the ncm tool with test files to ensure successful execution."""
    pdf_output = tmp_path / "output.pdf"
    matched_output = tmp_path / "matched_samples.tsv"
    txt_output = tmp_path / "description.txt"
    matrix_output = tmp_path / "metrics_matrix.tsv"

    result = run_ncm(
        samples=str(test_paths["samples"]),
        bed=str(test_paths["bed"]),
        pt=str(test_paths["pt"]),
        pdf=str(pdf_output),
        matched=str(matched_output),
        txt=str(txt_output),
        matrix=str(matrix_output),
    )

    assert result.returncode == 0, "ncm tool execution failed"
    assert pdf_output.exists(), "PDF output file was not created"
    assert matched_output.exists(), "Matched samples output file was not created"
    assert txt_output.exists(), "Description output file was not created"
    assert matrix_output.exists(), "Metrics matrix output file was not created"