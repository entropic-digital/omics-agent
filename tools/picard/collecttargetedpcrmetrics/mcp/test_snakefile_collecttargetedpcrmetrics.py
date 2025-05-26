import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "input_bam.bam",
        "reference_sequence": test_dir / "reference_sequence.fasta",
        "target_intervals": test_dir / "target_intervals.bed",
        "output_metrics": test_dir / "output_metrics.txt",
        "amplicon_intervals": test_dir / "amplicon_intervals.bed",
    }


def test_snakefile_collecttargetedpcrmetrics(test_paths, tmp_path, capsys):
    """Test that collecttargetedpcrmetrics generates the expected Snakefile."""
    from tools.picard.mcp.run_collecttargetedpcrmetrics import run_collecttargetedpcrmetrics
    temp_output = tmp_path / "temp_output_metrics.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_collecttargetedpcrmetrics(
        input_bam=str(test_paths["input_bam"]),
        reference_sequence=str(test_paths["reference_sequence"]),
        target_intervals=str(test_paths["target_intervals"]),
        output_metrics=str(temp_output),
        amplicon_intervals=str(test_paths["amplicon_intervals"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule collecttargetedpcrmetrics:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "input_bam=" in content, "Missing input_bam parameter"
    assert "reference_sequence=" in content, "Missing reference_sequence parameter"
    assert "target_intervals=" in content, "Missing target_intervals parameter"
    assert "output_metrics=" in content, "Missing output_metrics parameter"
    assert "amplicon_intervals=" in content, "Missing amplicon_intervals parameter"


def test_run_collecttargetedpcrmetrics(test_paths, tmp_path):
    """Test that collecttargetedpcrmetrics can be run with the test files."""
    from tools.picard.mcp.run_collecttargetedpcrmetrics import run_collecttargetedpcrmetrics
    temp_output = tmp_path / "output_metrics.txt"

    result = run_collecttargetedpcrmetrics(
        input_bam=str(test_paths["input_bam"]),
        reference_sequence=str(test_paths["reference_sequence"]),
        target_intervals=str(test_paths["target_intervals"]),
        output_metrics=str(temp_output),
        amplicon_intervals=str(test_paths["amplicon_intervals"]),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "collecttargetedpcrmetrics run failed"
    assert temp_output.exists(), "Output metrics file was not created"