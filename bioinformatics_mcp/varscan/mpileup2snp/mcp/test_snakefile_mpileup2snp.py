import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "mpileup_file": test_dir / "test.mpileup",
        "expected_vcf_file": test_dir / "expected_output.vcf",
        "snakefile_content_check": test_dir / "Snakefile",
    }

def test_snakefile_mpileup2snp(test_paths, tmp_path, capsys):
    """Test that the mpileup2snp tool generates the Snakefile correctly."""
    from bioinformatics_mcp.varscan.mpileup2snp.run_mpileup2snp import run_mpileup2snp
    temp_output = tmp_path / "output.vcf"

    run_mpileup2snp(
        mpileup_file=str(test_paths["mpileup_file"]),
        vcf_file=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule mpileup2snp:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "mpileup=" in content, "Missing mpileup input parameter in Snakefile"
    assert "vcf=" in content, "Missing vcf output parameter in Snakefile"

def test_run_mpileup2snp(test_paths, tmp_path):
    """Test that the mpileup2snp tool executes correctly with test files."""
    from bioinformatics_mcp.varscan.mpileup2snp.run_mpileup2snp import run_mpileup2snp
    temp_output = tmp_path / "output.vcf"

    result = run_mpileup2snp(
        mpileup_file=str(test_paths["mpileup_file"]),
        vcf_file=str(temp_output),
    )

    assert result.returncode == 0, "mpileup2snp execution failed"
    assert temp_output.exists(), "Expected output VCF file was not created"