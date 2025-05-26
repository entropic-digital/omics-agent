import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "vcf_file": test_dir / "input.vcf",
        "bam_file": test_dir / "input.bam",
        "reference_genome": test_dir / "reference.fasta",
        "known_variation_vcf": test_dir / "known_variants.vcf",
        "expected_annotated_vcf": test_dir / "expected_output.vcf",
    }


def test_snakefile_variantannotator(test_paths, tmp_path, capsys):
    """Test that variantannotator generates the expected Snakefile."""
    from tools.gatk.variantannotator.run_variantannotator import run_variantannotator
    temp_output = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_variantannotator(
        vcf_file=str(test_paths["vcf_file"]),
        bam_file=str(test_paths["bam_file"]),
        reference_genome=str(test_paths["reference_genome"]),
        known_variation_vcf=str(test_paths["known_variation_vcf"]),
        annotated_vcf=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements in the Snakefile
    assert "rule variantannotator:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify all required inputs are present
    assert "vcf_file=" in content, "Missing vcf_file parameter"
    assert "bam_file=" in content, "Missing bam_file parameter"
    assert "reference_genome=" in content, "Missing reference_genome parameter"
    assert "known_variation_vcf=" in content, "Missing known_variation_vcf parameter"

    # Verify the output parameter is present
    assert "annotated_vcf=" in content, "Missing annotated_vcf parameter"


def test_run_variantannotator(test_paths, tmp_path):
    """Test that variantannotator can be run with the test files."""
    from tools.gatk.variantannotator.run_variantannotator import run_variantannotator
    temp_output = tmp_path / "output.vcf"

    result = run_variantannotator(
        vcf_file=str(test_paths["vcf_file"]),
        bam_file=str(test_paths["bam_file"]),
        reference_genome=str(test_paths["reference_genome"]),
        known_variation_vcf=str(test_paths["known_variation_vcf"]),
        annotated_vcf=str(temp_output),
    )

    # Verify that the Snakemake run is successful
    assert result.returncode == 0, "variantannotator run failed"
    assert temp_output.exists(), "Output VCF file was not created"
    assert temp_output.stat().st_size > 0, "Output VCF file is empty"
