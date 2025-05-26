import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up paths for test files."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_gvcf_or_db": test_dir / "input.g.vcf",
        "reference_genome": test_dir / "reference.fasta",
        "output_vcf": test_dir / "output.vcf",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_genotypegvcfs(test_paths, tmp_path, capsys):
    """Test Snakefile generation for genotypegvcfs."""
    from tools.gatk.genotypegvcfs.run_genotypegvcfs import run_genotypegvcfs
    temp_output_vcf = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True
    run_genotypegvcfs(
        input_gvcf_or_db=str(test_paths["input_gvcf_or_db"]),
        reference_genome=str(test_paths["reference_genome"]),
        output_vcf=str(temp_output_vcf),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements in the generated Snakefile
    assert "rule genotypegvcfs:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "'input_gvcf_or_db':" in content, "Missing input_gvcf_or_db parameter"
    assert "'reference':" in content, "Missing reference parameter"
    assert "output:" in content, "Missing output section"
    assert "'vcf':" in content, "Missing vcf output parameter"
    assert "wrapper:" in content, "Missing wrapper section"

def test_run_genotypegvcfs(test_paths, tmp_path):
    """Test execution of genotypegvcfs with test files."""
    from tools.gatk.genotypegvcfs.run_genotypegvcfs import run_genotypegvcfs
    temp_output_vcf = tmp_path / "output.vcf"

    result = run_genotypegvcfs(
        input_gvcf_or_db=str(test_paths["input_gvcf_or_db"]),
        reference_genome=str(test_paths["reference_genome"]),
        output_vcf=str(temp_output_vcf),
    )

    # Verify that the tool executed successfully
    assert result.returncode == 0, "genotypegvcfs run failed"
    # Verify that the output file is created
    assert temp_output_vcf.exists(), "Output VCF file was not created"