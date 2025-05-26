import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "vcf_file": test_dir / "input.vcf",
        "recalibration_file": test_dir / "recalibration.table",
        "tranches_file": test_dir / "tranches.txt",
        "expected_snakefile": test_dir / "Snakefile",
        "output_vcf": test_dir / "output.vcf"
    }

def test_snakefile_applyvqsr(test_paths, tmp_path, capsys):
    """Test that applyvqsr generates the expected Snakefile."""
    from tools.gatk.applyvqsr.run_applyvqsr import run_applyvqsr
    
    output_vcf = tmp_path / "output.vcf"

    run_applyvqsr(
        vcf_file=str(test_paths["vcf_file"]),
        recalibration_file=str(test_paths["recalibration_file"]),
        tranches_file=str(test_paths["tranches_file"]),
        output_vcf=str(output_vcf),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule applyvqsr:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    assert "vcf_file=" in content, "Missing vcf_file parameter"
    assert "recalibration_file=" in content, "Missing recalibration_file parameter"
    assert "tranches_file=" in content, "Missing tranches_file parameter"
    assert "output_vcf=" in content, "Missing output_vcf parameter"

def test_run_applyvqsr(test_paths, tmp_path):
    """Test that applyvqsr can be run with the test files."""
    from tools.gatk.applyvqsr.run_applyvqsr import run_applyvqsr
    
    output_vcf = tmp_path / "output.vcf"

    result = run_applyvqsr(
        vcf_file=str(test_paths["vcf_file"]),
        recalibration_file=str(test_paths["recalibration_file"]),
        tranches_file=str(test_paths["tranches_file"]),
        output_vcf=str(output_vcf)
    )

    assert result.returncode == 0, "applyvqsr run failed"
    assert output_vcf.exists(), "Output VCF file was not created"
