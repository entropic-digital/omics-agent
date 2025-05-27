"""Module that tests if the computematrix Snakefile is rendered and runnable"""

import pytest
from pathlib import Path
from bioinformatics_mcp.deeptools.computematrix.run_computematrix import run_computematrix


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_data"
    return {
        "bed": base_dir / "regions.bed",
        "bigwig": base_dir / "signal.bw",
        "expected_matrix_gz": base_dir / "matrix.gz",
        "expected_matrix_tab": base_dir / "matrix.tab",
        "expected_matrix_bed": base_dir / "matrix.bed",
    }


def test_snakefile_computematrix(test_paths, tmp_path, capsys):
    """Test that computematrix generates the expected Snakefile."""
    run_computematrix(
        bed=str(test_paths["bed"]),
        bigwig=str(test_paths["bigwig"]),
        matrix_gz=str(tmp_path / "matrix.gz"),
        matrix_tab=str(tmp_path / "matrix.tab"),
        matrix_bed=str(tmp_path / "matrix.bed"),
        command="scale-regions",
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule computematrix:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"bed={str(test_paths['bed'])}" in content, "Missing bed input"
    assert f"bigwig={str(test_paths['bigwig'])}" in content, "Missing bigwig input"
    assert "output.matrix_gz =" in content, "Missing matrix_gz output"
    assert "output.matrix_tab =" in content, "Missing matrix_tab output"
    assert "output.matrix_bed =" in content, "Missing matrix_bed output"
    assert "params.command = 'scale-regions'" in content, "Missing command parameter"


def test_run_computematrix(test_paths, tmp_path):
    """Test that computematrix can be run with the test files."""
    result = run_computematrix(
        bed=str(test_paths["bed"]),
        bigwig=str(test_paths["bigwig"]),
        matrix_gz=str(tmp_path / "matrix.gz"),
        matrix_tab=str(tmp_path / "matrix.tab"),
        matrix_bed=str(tmp_path / "matrix.bed"),
        command="scale-regions",
    )

    assert result.returncode == 0, "computematrix run failed"
    assert (tmp_path / "matrix.gz").exists(), "matrix.gz output file not found"
    assert (tmp_path / "matrix.tab").exists(), "matrix.tab output file not found"
    assert (tmp_path / "matrix.bed").exists(), "matrix.bed output file not found"
