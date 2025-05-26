"""Module that tests if the plotheatmap Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).resolve().parent.parent
    test_dir = base_dir / "test"
    return {
        "matrix_file": test_dir / "matrix_file.gz",
        "heatmap_img": test_dir / "heatmap.png",
        "regions": test_dir / "regions.bed",
        "heatmap_matrix": test_dir / "heatmap_matrix.tab",
    }


def test_snakefile_plotheatmap(test_paths, tmp_path, capsys):
    """Test that plotheatmap generates the expected Snakefile."""
    from tools.deeptools.plotheatmap.run_plotheatmap import run_plotheatmap

    temp_heatmap_img = tmp_path / "output.png"

    # Generate the Snakefile with print_only=True to capture the content
    run_plotheatmap(
        matrix_file=str(test_paths["matrix_file"]),
        heatmap_img=str(temp_heatmap_img),
        regions=str(test_paths["regions"]),
        heatmap_matrix=str(test_paths["heatmap_matrix"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in the Snakefile
    assert "rule plotheatmap:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify all specified input parameters
    assert "matrix_file=" in content, "Missing 'matrix_file' input"
    # Verify all specified output parameters
    assert "heatmap_img=" in content, "Missing 'heatmap_img' output"
    assert "regions=" in content, "Missing 'regions' output"
    assert "heatmap_matrix=" in content, "Missing 'heatmap_matrix' output"


def test_run_plotheatmap(test_paths, tmp_path):
    """Test that plotheatmap can be run with the test files."""
    from tools.deeptools.plotheatmap.run_plotheatmap import run_plotheatmap

    temp_heatmap_img = tmp_path / "output.png"
    temp_regions = tmp_path / "output.bed"
    temp_heatmap_matrix = tmp_path / "output.tab"

    result = run_plotheatmap(
        matrix_file=str(test_paths["matrix_file"]),
        heatmap_img=str(temp_heatmap_img),
        regions=str(temp_regions),
        heatmap_matrix=str(temp_heatmap_matrix),
    )

    # Verify that the process completes successfully
    assert result.returncode == 0, "plotheatmap execution failed"

    # Verify that output files are created
    assert temp_heatmap_img.exists(), "Heatmap image was not created"
    assert temp_regions.exists(), "Regions file was not created"
    assert temp_heatmap_matrix.exists(), "Heatmap matrix file was not created"
