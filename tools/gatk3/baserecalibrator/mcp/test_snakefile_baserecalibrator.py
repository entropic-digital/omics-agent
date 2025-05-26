import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test" / "baserecalibrator"
    return {
        "bam_file": test_dir / "input.bam",
        "vcf_files": test_dir / "input.vcf",
        "reference_genome": test_dir / "reference.fasta",
        "recalibration_table": test_dir / "output.recal_data.grp",
        "expected_snakefile": test_dir / "Snakefile",
    }

def test_snakefile_baserecalibrator(test_paths, tmp_path, capsys):
    """Test that baserecalibrator generates the expected Snakefile."""
    from tools.gatk3.baserecalibrator.mcp.run_baserecalibrator import run_baserecalibrator

    run_baserecalibrator(
        bam_file=str(test_paths["bam_file"]),
        vcf_files=str(test_paths["vcf_files"]),
        reference_genome=str(test_paths["reference_genome"]),
        recalibration_table=str(test_paths["recalibration_table"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule baserecalibrator:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "bam_file=" in content, "Missing bam_file in input"
    assert "vcf_files=" in content, "Missing vcf_files in input"
    assert "reference_genome=" in content, "Missing reference_genome in input"
    assert "output:" in content, "Missing output section"
    assert "recalibration_table=" in content, "Missing recalibration_table in output"
    assert "wrapper:" in content, "Missing wrapper section"

def test_run_baserecalibrator(test_paths, tmp_path):
    """Test that baserecalibrator can be run with the test files."""
    from tools.gatk3.baserecalibrator.mcp.run_baserecalibrator import run_baserecalibrator
    temp_output = tmp_path / "output.recal_data.grp"

    result = run_baserecalibrator(
        bam_file=str(test_paths["bam_file"]),
        vcf_files=str(test_paths["vcf_files"]),
        reference_genome=str(test_paths["reference_genome"]),
        recalibration_table=str(temp_output),
    )

    assert result.returncode == 0, "baserecalibrator run failed"
    assert temp_output.exists(), "Recalibration table output not generated"