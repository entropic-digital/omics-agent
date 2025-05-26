"""Module that tests if the plotprofile Snakefile is rendered and runnable"""

import pytest
from pathlib import Path
from tools.deeptools.plotprofile.run_plotprofile import run_plotprofile


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "matrix_file": test_dir / "test_matrix.gz",
        "plot_img": test_dir / "output_plot.png",
        "regions": test_dir / "output_regions.bed",
        "data": test_dir / "output_data.tab",
    }


def test_snakefile_plotprofile(test_paths, tmp_path, capsys):
    """Test that plotprofile generates the expected Snakefile."""
    temp_output_plot = tmp_path / "output_plot.png"
    temp_output_regions = tmp_path / "output_regions.bed"
    temp_output_data = tmp_path / "output_data.tab"

    run_plotprofile(
        matrix_file=str(test_paths["matrix_file"]),
        plot_img=str(temp_output_plot),
        regions=str(temp_output_regions),
        data=str(temp_output_data),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule plotprofile:" in content, "Missing rule definition in the Snakefile"
    assert "input:" in content, "Missing input section in the Snakefile"
    assert "output:" in content, "Missing output section in the Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in the Snakefile"
    assert "matrix_file=" in content, (
        "Input parameter 'matrix_file' is missing in the Snakefile"
    )
    assert "plot_img=" in content, (
        "Output parameter 'plot_img' is missing in the Snakefile"
    )
    assert "regions=" in content, "Output option 'regions' is missing in the Snakefile"
    assert "data=" in content, "Output option 'data' is missing in the Snakefile"
    assert "file:tools/deeptools/plotprofile" in content, (
        "Wrapper path is incorrect or missing"
    )


def test_run_plotprofile(test_paths, tmp_path):
    """Test that plotprofile can be run with the test files."""
    temp_output_plot = tmp_path / "output_plot.png"
    temp_output_regions = tmp_path / "output_regions.bed"
    temp_output_data = tmp_path / "output_data.tab"

    result = run_plotprofile(
        matrix_file=str(test_paths["matrix_file"]),
        plot_img=str(temp_output_plot),
        regions=str(temp_output_regions),
        data=str(temp_output_data),
    )

    assert result.returncode == 0, "plotprofile execution failed"
    assert temp_output_plot.exists(), "Expected plot image was not created"
    assert temp_output_regions.exists(), "Expected regions file was not created"
    assert temp_output_data.exists(), "Expected data table was not created"
