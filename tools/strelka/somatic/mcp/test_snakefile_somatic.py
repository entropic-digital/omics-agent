import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "tumor_bam": test_dir / "tumor.bam",
        "tumor_bam_index": test_dir / "tumor.bam.bai",
        "reference_fasta": test_dir / "reference.fasta",
        "reference_fasta_index": test_dir / "reference.fasta.fai",
        "normal_bam": test_dir / "normal.bam",
        "normal_bam_index": test_dir / "normal.bam.bai",
        "output_statistics": test_dir / "statistics.txt",
        "output_variants": test_dir / "variants.vcf",
    }


def test_snakefile_somatic(test_paths, tmp_path, capsys):
    """Test that somatic generates the expected Snakefile."""
    from tools.strelka.somatic.run_somatic import run_somatic
    temp_statistics = tmp_path / "statistics.txt"
    temp_variants = tmp_path / "variants.vcf"

    run_somatic(
        tumor_bam=str(test_paths["tumor_bam"]),
        tumor_bam_index=str(test_paths["tumor_bam_index"]),
        reference_fasta=str(test_paths["reference_fasta"]),
        reference_fasta_index=str(test_paths["reference_fasta_index"]),
        normal_bam=str(test_paths["normal_bam"]),
        normal_bam_index=str(test_paths["normal_bam_index"]),
        output_statistics=str(temp_statistics),
        output_variants=str(temp_variants),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule somatic:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    assert "tumor_bam=" in content, "Missing tumor_bam input parameter"
    assert "tumor_bam_index=" in content, "Missing tumor_bam_index input parameter"
    assert "reference_fasta=" in content, "Missing reference_fasta input parameter"
    assert "reference_fasta_index=" in content, "Missing reference_fasta_index input parameter"
    assert "normal_bam=" in content, "Missing normal_bam input parameter"
    assert "normal_bam_index=" in content, "Missing normal_bam_index input parameter"

    assert "output_statistics=" in content, "Missing output_statistics output parameter"
    assert "output_variants=" in content, "Missing output_variants output parameter"


def test_run_somatic(test_paths, tmp_path):
    """Test that somatic can be run with the test files."""
    from tools.strelka.somatic.run_somatic import run_somatic
    temp_statistics = tmp_path / "statistics.txt"
    temp_variants = tmp_path / "variants.vcf"

    result = run_somatic(
        tumor_bam=str(test_paths["tumor_bam"]),
        tumor_bam_index=str(test_paths["tumor_bam_index"]),
        reference_fasta=str(test_paths["reference_fasta"]),
        reference_fasta_index=str(test_paths["reference_fasta_index"]),
        normal_bam=str(test_paths["normal_bam"]),
        normal_bam_index=str(test_paths["normal_bam_index"]),
        output_statistics=str(temp_statistics),
        output_variants=str(temp_variants),
    )

    assert result.returncode == 0, "Somatic tool execution failed"