import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "pindel_output": test_dir / "pindel_output.txt",
        "reference": test_dir / "reference.fasta",
        "vcf_output": test_dir / "output.vcf",
        "reference_index": test_dir / "reference.fai",
    }

def test_snakefile_pindel2vcf(test_paths, tmp_path, capsys):
    """Test that pindel2vcf generates the expected Snakefile."""
    from tools.pindel2vcf.mcp.run_pindel2vcf import run_pindel2vcf

    run_pindel2vcf(
        pindel_output=str(test_paths["pindel_output"]),
        reference=str(test_paths["reference"]),
        vcf_output=str(tmp_path / "output.vcf"),
        reference_index=str(test_paths["reference_index"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule pindel2vcf:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "pindel_output=" in content, "Missing pindel_output parameter"
    assert "reference=" in content, "Missing reference parameter"
    assert "vcf_output=" in content, "Missing vcf_output parameter"
    assert "reference_index=" in content, "Missing reference_index parameter"

def test_run_pindel2vcf(test_paths, tmp_path):
    """Test that pindel2vcf can be run with the test files."""
    from tools.pindel2vcf.mcp.run_pindel2vcf import run_pindel2vcf

    temp_vcf_output = tmp_path / "output.vcf"

    result = run_pindel2vcf(
        pindel_output=str(test_paths["pindel_output"]),
        reference=str(test_paths["reference"]),
        vcf_output=str(temp_vcf_output),
        reference_index=str(test_paths["reference_index"])
    )

    assert result.returncode == 0, "pindel2vcf run failed"
    assert temp_vcf_output.exists(), "VCF output file was not created"