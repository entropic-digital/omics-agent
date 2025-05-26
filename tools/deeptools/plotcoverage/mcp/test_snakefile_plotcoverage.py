import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths for the plotcoverage tool."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bams": test_dir / "test.bam",
        "bed": test_dir / "test.bed",
        "blacklist": test_dir / "blacklist.bed",
        "raw_counts": test_dir / "raw_counts.txt",
        "metrics": test_dir / "metrics.txt",
        "plot": test_dir / "plot.png",
    }


def test_snakefile_plotcoverage(test_paths, tmp_path, capsys):
    """Test that plotcoverage generates the expected Snakefile."""
    from tools.deeptools.plotcoverage.run_plotcoverage import run_plotcoverage

    temp_raw_counts = tmp_path / "raw_counts.txt"
    temp_metrics = tmp_path / "metrics.txt"
    temp_plot = tmp_path / "plot.png"

    # Generate the Snakefile with print_only=True to capture the content
    run_plotcoverage(
        bams=str(test_paths["bams"]),
        bed=str(test_paths["bed"]),
        blacklist=str(test_paths["blacklist"]),
        raw_counts=str(temp_raw_counts),
        metrics=str(temp_metrics),
        plot=str(temp_plot),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule structure and parameters
    assert "rule plotcoverage:" in content, "Missing rule definition for plotCoverage"
    assert "input:" in content, "Missing input section in the Snakefile"
    assert "output:" in content, "Missing output section in the Snakefile"
    assert "wrapper:" in content, "Missing wrapper directive in the Snakefile"

    # Verify required inputs are present
    assert "bams=" in content, "Missing input parameter 'bams'"
    assert "bed=" in content, "Missing input parameter 'bed'"
    assert "blacklist=" in content, "Missing input parameter 'blacklist'"

    # Verify required outputs are present
    assert "raw_counts=" in content, "Missing output parameter 'raw_counts'"
    assert "metrics=" in content, "Missing output parameter 'metrics'"
    assert "plot=" in content, "Missing output parameter 'plot'"


def test_run_plotcoverage(test_paths, tmp_path):
    """Test that plotcoverage can be run with the test files."""
    from tools.deeptools.plotcoverage.run_plotcoverage import run_plotcoverage

    temp_raw_counts = tmp_path / "raw_counts.txt"
    temp_metrics = tmp_path / "metrics.txt"
    temp_plot = tmp_path / "plot.png"

    # Run the plotCoverage tool with the test inputs
    result = run_plotcoverage(
        bams=str(test_paths["bams"]),
        bed=str(test_paths["bed"]),
        blacklist=str(test_paths["blacklist"]),
        raw_counts=str(temp_raw_counts),
        metrics=str(temp_metrics),
        plot=str(temp_plot),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "plotCoverage run failed with non-zero exit code"

    # Verify output files are created
    assert temp_raw_counts.exists(), "Raw counts output file was not created"
    assert temp_metrics.exists(), "Metrics output file was not created"
    assert temp_plot.exists(), "Plot output file was not created"