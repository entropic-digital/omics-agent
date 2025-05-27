import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "input.bam",
        "reference": test_dir / "reference.fasta",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_collectduplexseqmetrics(test_paths, tmp_path, capsys):
    """Test that collectduplexseqmetrics generates the expected Snakefile."""
    from bioinformatics_mcp.fgbio.collectduplexseqmetrics.mcp.run_collectduplexseqmetrics import run_collectduplexseqmetrics
    temp_output_txt = tmp_path / "output.txt"
    temp_output_metrics = tmp_path / "output.metrics"

    run_collectduplexseqmetrics(
        input_bam=str(test_paths["input_bam"]),
        output_txt=str(temp_output_txt),
        output_metrics=str(temp_output_metrics),
        reference=str(test_paths["reference"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule collectduplexseqmetrics:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    assert "input_bam=" in content, "Missing input_bam parameter"
    assert "output_txt=" in content, "Missing output_txt parameter"
    assert "output_metrics=" in content, "Missing output_metrics parameter"
    assert "reference=" in content, "Missing reference parameter"
    assert "min_base_quality=10" in content, "Missing min_base_quality parameter"
    assert "min_mapping_quality=30" in content, "Missing min_mapping_quality parameter"
    assert "collapse_duplex=True" in content, "Missing collapse_duplex parameter"


def test_run_collectduplexseqmetrics(test_paths, tmp_path):
    """Test that collectduplexseqmetrics can be run with test files."""
    from bioinformatics_mcp.fgbio.collectduplexseqmetrics.mcp.run_collectduplexseqmetrics import run_collectduplexseqmetrics
    temp_output_txt = tmp_path / "output.txt"
    temp_output_metrics = tmp_path / "output.metrics"

    result = run_collectduplexseqmetrics(
        input_bam=str(test_paths["input_bam"]),
        output_txt=str(temp_output_txt),
        output_metrics=str(temp_output_metrics),
        reference=str(test_paths["reference"]),
    )

    assert result.returncode == 0, "collectduplexseqmetrics run failed"
    assert temp_output_txt.exists(), "Output TXT file was not created"
    assert temp_output_metrics.exists(), "Output metrics file was not created"