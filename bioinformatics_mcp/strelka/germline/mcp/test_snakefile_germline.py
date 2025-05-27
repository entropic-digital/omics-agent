import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test" / "germline"
    return {
        "reference_fasta": test_dir / "reference.fasta",
        "bam": test_dir / "sample.bam",
        "output_vcf": test_dir / "output.vcf",
        "output_tbi": test_dir / "output.vcf.tbi",
        "regions_bed": test_dir / "regions.bed",
    }


def test_snakefile_germline(test_paths, tmp_path, capsys):
    """Test that the germline Snakefile is generated correctly."""
    from bioinformatics_mcp.strelka.germline.run_germline import run_germline

    run_germline(
        reference_fasta=str(test_paths["reference_fasta"]),
        bam=str(test_paths["bam"]),
        output_vcf=str(tmp_path / "output.vcf"),
        output_tbi=str(tmp_path / "output.vcf.tbi"),
        regions_bed=str(test_paths["regions_bed"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule germline:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    assert "reference_fasta=" in content, "Missing reference_fasta parameter"
    assert "bam=" in content, "Missing bam parameter"
    assert "output_vcf=" in content, "Missing output_vcf parameter"
    assert "output_tbi=" in content, "Missing output_tbi parameter"
    assert "regions_bed=" in content, "Missing regions_bed parameter when applicable"


def test_run_germline(test_paths, tmp_path):
    """Test that the germline tool runs successfully with test input files."""
    from bioinformatics_mcp.strelka.germline.run_germline import run_germline

    temp_output_vcf = tmp_path / "output.vcf"
    temp_output_tbi = tmp_path / "output.vcf.tbi"

    result = run_germline(
        reference_fasta=str(test_paths["reference_fasta"]),
        bam=str(test_paths["bam"]),
        output_vcf=str(temp_output_vcf),
        output_tbi=str(temp_output_tbi),
        regions_bed=str(test_paths["regions_bed"]),
    )

    assert result.returncode == 0, "germline tool execution failed"
    assert temp_output_vcf.exists(), "Output VCF file was not created"
    assert temp_output_tbi.exists(), "Output TBI file was not created"