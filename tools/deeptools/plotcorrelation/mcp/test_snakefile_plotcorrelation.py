import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_matrix": test_dir / "matrix.tsv.gz",
        "expected_plot": test_dir / "plot.pdf",
        "expected_matrix": test_dir / "correlation_matrix.tsv",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_plotcorrelation(test_paths, tmp_path, capsys):
    """Test that plotcorrelation generates the expected Snakefile."""
    from tools.deeptools.plotcorrelation.run_plotcorrelation import run_plotcorrelation
    temp_plot = tmp_path / "temp_plot.pdf"
    temp_matrix = tmp_path / "temp_correlation_matrix.tsv"
    
    # Generate the Snakefile with print_only=True to capture the content
    run_plotcorrelation(
        input_matrix=str(test_paths["input_matrix"]),
        output_plot=str(temp_plot),
        output_matrix=str(temp_matrix),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule structure and parameters
    assert "rule plotcorrelation:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "matrix=" in content, "Missing input matrix parameter"
    assert "plot=" in content, "Missing output plot parameter"
    assert "correlation=" in content, "Missing correlation parameter"
    assert "plot=heatmap" in content, "Default plot type 'heatmap' missing"
    assert "correlation=spearman" in content, "Default correlation type 'spearman' missing"

def test_run_plotcorrelation(test_paths, tmp_path):
    """Test that plotcorrelation can be run with the test files."""
    from tools.deeptools.plotcorrelation.run_plotcorrelation import run_plotcorrelation
    temp_plot = tmp_path / "output_plot.pdf"
    temp_matrix = tmp_path / "output_correlation_matrix.tsv"

    result = run_plotcorrelation(
        input_matrix=str(test_paths["input_matrix"]),
        output_plot=str(temp_plot),
        output_matrix=str(temp_matrix)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "plotcorrelation run failed"

    # Verify that output files are generated
    assert temp_plot.exists(), "Output plot file was not created"
    assert temp_matrix.exists(), "Output correlation matrix file was not created"