import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test_data/mpileup2indel"
    return {
        "mpileup_file": test_dir / "test.mpileup",
        "expected_vcf_file": test_dir / "expected.vcf",
        "unexpected_vcf_file": test_dir / "unexpected.vcf",
    }


def test_snakefile_mpileup2indel(test_paths, tmp_path, capsys):
    """Test that mpileup2indel generates the expected Snakefile."""
    from bioinformatics_mcp.varscan.mpileup2indel.run_mpileup2indel import run_mpileup2indel

    temp_vcf = tmp_path / "output.vcf"

    run_mpileup2indel(
        mpileup_file=str(test_paths["mpileup_file"]),
        vcf_file=str(temp_vcf),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule mpileup2indel:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "mpileup_file=" in content, "Missing mpileup_file input"
    assert "vcf_file=" in content, "Missing vcf_file output"


def test_run_mpileup2indel(test_paths, tmp_path):
    """Test that mpileup2indel can be run with the test files."""
    from bioinformatics_mcp.varscan.mpileup2indel.run_mpileup2indel import run_mpileup2indel

    temp_vcf = tmp_path / "output.vcf"

    result = run_mpileup2indel(
        mpileup_file=str(test_paths["mpileup_file"]),
        vcf_file=str(temp_vcf),
    )

    assert result.returncode == 0, "mpileup2indel run failed"
    assert temp_vcf.exists(), "Output VCF file was not created"