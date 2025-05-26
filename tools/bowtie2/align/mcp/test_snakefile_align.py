import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "sample": test_dir / "sample.fastq",
        "idx": test_dir / "reference_index",
        "ref": test_dir / "reference.fasta",
        "ref_fai": test_dir / "reference.fasta.fai",
        "sam_bam_cram": test_dir / "output.bam",
        "idx_out": test_dir / "output.bam.bai",
        "metrics": test_dir / "metrics.txt",
        "unaligned": test_dir / "unaligned.fastq",
        "unpaired": test_dir / "unpaired.fastq",
        "unconcordant": test_dir / "unconcordant.fastq",
        "concordant": test_dir / "concordant.fastq",
    }


def test_snakefile_align(test_paths, tmp_path, capsys):
    """Test that align generates the expected Snakefile."""
    from tools.bowtie2.align.run_align import run_align

    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_align(
        sample=str(test_paths["sample"]),
        idx=str(test_paths["idx"]),
        sam_bam_cram=str(temp_output),
        ref=str(test_paths["ref"]),
        ref_fai=str(test_paths["ref_fai"]),
        idx_out=str(test_paths["idx_out"]),
        metrics=str(test_paths["metrics"]),
        unaligned=str(test_paths["unaligned"]),
        unpaired=str(test_paths["unpaired"]),
        unconcordant=str(test_paths["unconcordant"]),
        concordant=str(test_paths["concordant"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements of the Snakefile
    assert "rule align:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify all required inputs are present
    assert "sample=" in content, "Missing input parameter: sample"
    assert "idx=" in content, "Missing input parameter: idx"
    assert "ref=" in content, "Missing input parameter: ref"
    assert "ref_fai=" in content, "Missing input parameter: ref_fai"

    # Verify all required outputs are present
    assert "sam_bam_cram=" in content, "Missing output parameter: sam_bam_cram"
    assert "idx=" in content, "Missing output parameter: idx"
    assert "metrics=" in content, "Missing output parameter: metrics"
    assert "unaligned=" in content, "Missing output parameter: unaligned"
    assert "unpaired=" in content, "Missing output parameter: unpaired"
    assert "unconcordant=" in content, "Missing output parameter: unconcordant"
    assert "concordant=" in content, "Missing output parameter: concordant"


def test_run_align(test_paths, tmp_path):
    """Test that align can be run with the test files."""
    from tools.bowtie2.align.run_align import run_align

    temp_output = tmp_path / "output.bam"

    result = run_align(
        sample=str(test_paths["sample"]),
        idx=str(test_paths["idx"]),
        sam_bam_cram=str(temp_output),
        ref=str(test_paths["ref"]),
        ref_fai=str(test_paths["ref_fai"]),
        idx_out=str(test_paths["idx_out"]),
        metrics=str(test_paths["metrics"]),
        unaligned=str(test_paths["unaligned"]),
        unpaired=str(test_paths["unpaired"]),
        unconcordant=str(test_paths["unconcordant"]),
        concordant=str(test_paths["concordant"]),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "align run failed"
    assert temp_output.exists(), "Output file was not created"