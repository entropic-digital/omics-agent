import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_cram_files": test_dir / "sample.bam",
        "reference_genome": test_dir / "reference.fasta",
        "bed_file": test_dir / "regions.bed",
        "output_vcf_bcf": test_dir / "output.vcf",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_delly(test_paths, tmp_path, capsys):
    """Test that delly generates the expected Snakefile."""
    from tools.delly.mcp.run_delly import run_delly
    temp_output = tmp_path / "output.vcf"

    run_delly(
        bam_cram_files=str(test_paths["bam_cram_files"]),
        reference_genome=str(test_paths["reference_genome"]),
        output_vcf_bcf=str(temp_output),
        bed_file=str(test_paths["bed_file"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule delly:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam_cram_files=" in content, "Missing bam_cram_files parameter"
    assert "reference_genome=" in content, "Missing reference_genome parameter"
    assert "bed_file=" in content, "Missing bed_file parameter"
    assert "output_vcf_bcf=" in content, "Missing output_vcf_bcf parameter"

def test_run_delly(test_paths, tmp_path):
    """Test that delly can be run with the test files."""
    from tools.delly.mcp.run_delly import run_delly
    temp_output = tmp_path / "output.vcf"

    result = run_delly(
        bam_cram_files=str(test_paths["bam_cram_files"]),
        reference_genome=str(test_paths["reference_genome"]),
        output_vcf_bcf=str(temp_output),
        bed_file=str(test_paths["bed_file"])
    )

    assert result.returncode == 0, "delly run failed"
    assert temp_output.exists(), "Expected output file was not generated"