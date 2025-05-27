import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "test.bam",
        "fasta_reference": test_dir / "test.fasta",
        "known_variants": test_dir / "test.vcf.gz",
        "recalibration_table": test_dir / "recal_data.table",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_baserecalibrator(test_paths, tmp_path, capsys):
    """Test that baserecalibrator generates the expected Snakefile."""
    from bioinformatics_mcp.gatk.baserecalibrator.run_baserecalibrator import run_baserecalibrator
    temp_output = tmp_path / "recal_data.table"

    run_baserecalibrator(
        bam_file=str(test_paths["bam_file"]),
        fasta_reference=str(test_paths["fasta_reference"]),
        known_variants=str(test_paths["known_variants"]),
        recalibration_table=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule baserecalibrator:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam_file=" in content, "Missing bam_file parameter"
    assert "fasta_reference=" in content, "Missing fasta_reference parameter"
    assert "known_variants=" in content, "Missing known_variants parameter"
    assert "recalibration_table=" in content, "Missing recalibration_table parameter"

def test_run_baserecalibrator(test_paths, tmp_path):
    """Test that baserecalibrator can be run with the test files."""
    from bioinformatics_mcp.gatk.baserecalibrator.run_baserecalibrator import run_baserecalibrator
    temp_output = tmp_path / "recal_data.table"

    result = run_baserecalibrator(
        bam_file=str(test_paths["bam_file"]),
        fasta_reference=str(test_paths["fasta_reference"]),
        known_variants=str(test_paths["known_variants"]),
        recalibration_table=str(temp_output)
    )

    assert result.returncode == 0, "baserecalibrator run failed"
    assert temp_output.exists(), "Output recalibration table was not created"