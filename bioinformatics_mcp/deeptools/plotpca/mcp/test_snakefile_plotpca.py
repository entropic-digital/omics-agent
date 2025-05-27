import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input_matrix.gz",
        "output_plot": test_dir / "test_output_plot.png",
        "output_matrix": test_dir / "test_output_matrix.tsv",
    }


def test_snakefile_plotpca(test_paths, tmp_path, capsys):
    """Test that plotpca generates the expected Snakefile."""
    from bioinformatics_mcp.deeptools.plotpca.run_plotpca import run_plotpca

    run_plotpca(
        input_file=str(test_paths["input_file"]),
        output_plot=str(test_paths["output_plot"]),
        output_matrix=str(test_paths["output_matrix"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule plotpca:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert f'input_file="{test_paths["input_file"]}"' in content, "Missing input_file declaration"
    assert "output:" in content, "Missing output section in Snakefile"
    assert f'output_plot="{test_paths["output_plot"]}"' in content, "Missing output_plot declaration"
    assert f'output_matrix="{test_paths["output_matrix"]}"' in content, "Missing output_matrix declaration"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "file:tools/deeptools/plotpca" in content, "Wrapper path is incorrect or missing"


def test_run_plotpca(test_paths, tmp_path):
    """Test that plotpca can be run with the test files."""
    from bioinformatics_mcp.deeptools.plotpca.run_plotpca import run_plotpca

    temp_plot_path = tmp_path / "output_plot.png"
    temp_matrix_path = tmp_path / "output_matrix.tsv"

    result = run_plotpca(
        input_file=str(test_paths["input_file"]),
        output_plot=str(temp_plot_path),
        output_matrix=str(temp_matrix_path),
    )

    assert result.returncode == 0, "plotpca run failed"
    assert temp_plot_path.exists(), "Output plot file not generated"
    assert temp_matrix_path.exists(), "Output matrix file not generated"