import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "test_dir": test_dir,
        "input_vcf": test_dir / "test_input.vcf",
        "expected_snakefile": test_dir / "Snakefile",
    }

def test_snakefile_ensembl_variation(test_paths, tmp_path, capsys):
    """Test that ensembl-variation generates the expected Snakefile."""
    from bioinformatics_mcp.reference.ensembl_variation.run_ensembl_variation import run_ensembl_variation

    output_vcf = tmp_path / "output.vcf.gz"
    run_ensembl_variation(
        url="ftp://ftp.ensembl.org/pub",
        output_vcf=str(output_vcf),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule ensembl_variation:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "'output_vcf':" in content, "Missing output_vcf parameter in Snakefile"
    assert "'url':" in content, "Missing url parameter in Snakefile"

def test_run_ensembl_variation(test_paths, tmp_path):
    """Test that ensembl-variation can be run with the expected test files."""
    from bioinformatics_mcp.reference.ensembl_variation.run_ensembl_variation import run_ensembl_variation

    output_vcf = tmp_path / "output.vcf.gz"

    result = run_ensembl_variation(
        url="ftp://ftp.ensembl.org/pub",
        output_vcf=str(output_vcf),
    )

    assert result.returncode == 0, "ensembl-variation run failed"
    assert output_vcf.exists(), "Output VCF file was not created"
    assert output_vcf.stat().st_size > 0, "Output VCF file is empty"