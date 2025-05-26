import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "input.bam",
        "reference_fasta": test_dir / "reference.fasta",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_collectmultiplemetrics(test_paths, tmp_path, capsys):
    """Test that collectmultiplemetrics generates the expected Snakefile."""
    from tools.picard.collectmultiplemetrics.run_collectmultiplemetrics import run_collectmultiplemetrics
    temp_output_prefix = tmp_path / "output"

    # Generate the Snakefile with print_only=True to capture the content
    run_collectmultiplemetrics(
        bam_file=str(test_paths["bam_file"]),
        reference_fasta=str(test_paths["reference_fasta"]),
        output_prefix=str(temp_output_prefix),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements in the generated Snakefile
    assert "rule collectmultiplemetrics:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "bam_file=" in content, "Missing bam_file as input in Snakefile"
    assert "reference_fasta=" in content, "Missing reference_fasta as input in Snakefile"
    assert "output_prefix=" in content, "Missing output_prefix as output in Snakefile"


def test_run_collectmultiplemetrics(test_paths, tmp_path):
    """Test that collectmultiplemetrics can be run with the test files."""
    from tools.picard.collectmultiplemetrics.run_collectmultiplemetrics import run_collectmultiplemetrics
    temp_output_prefix = tmp_path / "output"

    result = run_collectmultiplemetrics(
        bam_file=str(test_paths["bam_file"]),
        reference_fasta=str(test_paths["reference_fasta"]),
        output_prefix=str(temp_output_prefix),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "collectmultiplemetrics run failed"
    # Verify the output files are created
    assert temp_output_prefix.with_suffix(".alignment_summary_metrics").exists(), "Missing .alignment_summary_metrics file"
    assert temp_output_prefix.with_suffix(".insert_size_metrics").exists(), "Missing .insert_size_metrics file"
    assert temp_output_prefix.with_suffix(".insert_size_histogram.pdf").exists(), "Missing .insert_size_histogram.pdf file"
    assert temp_output_prefix.with_suffix(".quality_distribution_metrics").exists(), "Missing .quality_distribution_metrics file"
    assert temp_output_prefix.with_suffix(".quality_distribution.pdf").exists(), "Missing .quality_distribution.pdf file"
    assert temp_output_prefix.with_suffix(".quality_by_cycle_metrics").exists(), "Missing .quality_by_cycle_metrics file"
    assert temp_output_prefix.with_suffix(".quality_by_cycle.pdf").exists(), "Missing .quality_by_cycle.pdf file"
    assert temp_output_prefix.with_suffix(".base_distribution_by_cycle_metrics").exists(), "Missing .base_distribution_by_cycle_metrics file"
    assert temp_output_prefix.with_suffix(".base_distribution_by_cycle.pdf").exists(), "Missing .base_distribution_by_cycle.pdf file"
    assert temp_output_prefix.with_suffix(".gc_bias.summary_metrics").exists(), "Missing .gc_bias.summary_metrics file"
    assert temp_output_prefix.with_suffix(".gc_bias.detail_metrics").exists(), "Missing .gc_bias.detail_metrics file"
    assert temp_output_prefix.with_suffix(".gc_bias.pdf").exists(), "Missing .gc_bias.pdf file"
    assert temp_output_prefix.with_suffix(".rna_metrics").exists(), "Missing .rna_metrics file"
    assert temp_output_prefix.with_suffix(".bait_bias_detail_metrics").exists(), "Missing .bait_bias_detail_metrics file"
    assert temp_output_prefix.with_suffix(".bait_bias_summary_metrics").exists(), "Missing .bait_bias_summary_metrics file"
    assert temp_output_prefix.with_suffix(".error_summary_metrics").exists(), "Missing .error_summary_metrics file"
    assert temp_output_prefix.with_suffix(".pre_adapter_detail_metrics").exists(), "Missing .pre_adapter_detail_metrics file"
    assert temp_output_prefix.with_suffix(".pre_adapter_summary_metrics").exists(), "Missing .pre_adapter_summary_metrics file"
    assert temp_output_prefix.with_suffix(".quality_yield_metrics").exists(), "Missing .quality_yield_metrics file"