"""Module that tests if the plotfingerprint Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "test.bam",
        "bam_index_file": test_dir / "test.bam.bai",
        "expected_snakefile": test_dir / "Snakefile",
        "expected_plot_file": test_dir / "fingerprint.png",
        "expected_counts_file": test_dir / "counts.tab",
        "expected_metrics_file": test_dir / "metrics.txt",
    }


def test_snakefile_plotfingerprint(test_paths, tmp_path, capsys):
    """Test that plotfingerprint generates the expected Snakefile."""
    from tools.deeptools.plotfingerprint.run_plotfingerprint import run_plotfingerprint

    temp_plot_file = tmp_path / "fingerprint.png"

    # Generate the Snakefile with print_only=True to capture the content
    run_plotfingerprint(
        bam_files=[str(test_paths["bam_file"])],
        bam_index_files=[str(test_paths["bam_index_file"])],
        plot_file=str(temp_plot_file),
        counts_file=None,
        metrics_file=None,
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements exist
    assert "rule plotfingerprint:" in content, "Missing plotfingerprint rule definition"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "bam_files=" in content, "Missing bam_files in input section"
    assert "bam_index_files=" in content, "Missing bam_index_files in input section"
    assert "plot_file=" in content, "Missing plot_file in output section"


def test_run_plotfingerprint(test_paths, tmp_path):
    """Test that plotfingerprint runs successfully with test files."""
    from tools.deeptools.plotfingerprint.run_plotfingerprint import run_plotfingerprint

    temp_plot_file = tmp_path / "fingerprint.png"
    temp_counts_file = tmp_path / "counts.tab"
    temp_metrics_file = tmp_path / "metrics.txt"

    # Run the plotfingerprint tool
    result = run_plotfingerprint(
        bam_files=[str(test_paths["bam_file"])],
        bam_index_files=[str(test_paths["bam_index_file"])],
        plot_file=str(temp_plot_file),
        counts_file=str(temp_counts_file),
        metrics_file=str(temp_metrics_file),
    )

    # Validate that the process ran successfully
    assert result.returncode == 0, "plotfingerprint run failed"
    assert temp_plot_file.exists(), "Output plot file was not created"
    assert temp_counts_file.exists(), "Counts file was not created"
    assert temp_metrics_file.exists(), "Metrics file was not created"
