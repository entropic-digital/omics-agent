import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.resolve()
    test_dir = base_dir / "test_files"
    return {
        "vcf": test_dir / "input.vcf",
        "reference_genome": test_dir / "reference.fasta",
        "filtered_vcf": test_dir / "filtered_output.vcf",
        "expected_snakefile": test_dir / "Snakefile_expected"
    }

def test_snakefile_variantfiltration(test_paths, capsys):
    """Test that the variantfiltration Snakefile is generated correctly."""
    from tools.gatk.variantfiltration.run_variantfiltration import run_variantfiltration
    run_variantfiltration(
        vcf=str(test_paths["vcf"]),
        reference_genome=str(test_paths["reference_genome"]),
        filtered_vcf=str(test_paths["filtered_vcf"]),
        print_only=True
    )
    captured = capsys.readouterr()
    content = captured.out
    
    assert "rule variantfiltration:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"vcf={test_paths['vcf']}" in content, "Missing VCF input parameter"
    assert f"reference_genome={test_paths['reference_genome']}" in content, "Missing reference genome input parameter"
    assert f"filtered_vcf={test_paths['filtered_vcf']}" in content, "Missing output filtered VCF parameter"

def test_run_variantfiltration(test_paths, tmp_path):
    """Test that the variantfiltration tool runs successfully."""
    from tools.gatk.variantfiltration.run_variantfiltration import run_variantfiltration
    temp_filtered_vcf = tmp_path / "filtered_output.vcf"

    result = run_variantfiltration(
        vcf=str(test_paths["vcf"]),
        reference_genome=str(test_paths["reference_genome"]),
        filtered_vcf=str(temp_filtered_vcf)
    )

    assert result.returncode == 0, "variantfiltration run failed"
    assert temp_filtered_vcf.exists(), "Filtered VCF file was not created"