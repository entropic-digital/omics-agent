import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "vcf_files": test_dir / "test.vcf",
        "bam_cram_files": test_dir / "test.bam",
        "reference_genome": test_dir / "reference.fasta",
        "reference_dictionary": test_dir / "reference.dict",
        "known_variants_vcf": test_dir / "known_variants.vcf.gz",
        "pedigree_file": test_dir / "pedigree.ped",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_varianteval(test_paths, tmp_path, capsys):
    """Test that varianteval generates the expected Snakefile."""
    from tools.gatk.varianteval.run_varianteval import run_varianteval

    temp_output = tmp_path / "output.txt"

    run_varianteval(
        vcf_files=str(test_paths["vcf_files"]),
        bam_cram_files=str(test_paths["bam_cram_files"]),
        reference_genome=str(test_paths["reference_genome"]),
        reference_dictionary=str(test_paths["reference_dictionary"]),
        known_variants_vcf=str(test_paths["known_variants_vcf"]),
        pedigree_file=str(test_paths["pedigree_file"]),
        extra="--some-flag",
        output=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule varianteval:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "vcf_files=" in content, "Missing vcf_files input parameter"
    assert "bam_cram_files=" in content, "Missing bam_cram_files input parameter"
    assert "reference_genome=" in content, "Missing reference_genome input parameter"
    assert "reference_dictionary=" in content, "Missing reference_dictionary input parameter"
    assert "known_variants_vcf=" in content, "Missing known_variants_vcf input parameter"
    assert "pedigree_file=" in content, "Missing pedigree_file input parameter"
    assert "output=" in content, "Missing output parameter"

def test_run_varianteval(test_paths, tmp_path):
    """Test that varianteval can be run with the test files."""
    from tools.gatk.varianteval.run_varianteval import run_varianteval

    temp_output = tmp_path / "output.txt"

    result = run_varianteval(
        vcf_files=str(test_paths["vcf_files"]),
        bam_cram_files=str(test_paths["bam_cram_files"]),
        reference_genome=str(test_paths["reference_genome"]),
        reference_dictionary=str(test_paths["reference_dictionary"]),
        known_variants_vcf=str(test_paths["known_variants_vcf"]),
        pedigree_file=str(test_paths["pedigree_file"]),
        extra="--some-flag",
        output=str(temp_output)
    )

    assert result.returncode == 0, "varianteval run failed"
    assert temp_output.exists(), "Output file was not created"