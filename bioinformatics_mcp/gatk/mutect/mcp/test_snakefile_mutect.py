import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "map": test_dir / "test_map.bam",
        "fasta": test_dir / "test_reference.fasta",
        "vcf": test_dir / "test_output.vcf",
        "intervals": test_dir / "test_intervals.bed",
        "pon": test_dir / "test_pon.vcf",
        "germline": test_dir / "test_germline.vcf",
        "bam": test_dir / "test_output.bam",
        "f1r2": test_dir / "test_f1r2.txt",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_mutect(test_paths, tmp_path, capsys):
    """Test that GATK Mutect generates the expected Snakefile."""
    from bioinformatics_mcp.gatk.mutect.run_mutect import run_mutect
    temp_output = tmp_path / "output.vcf"

    run_mutect(
        map=str(test_paths["map"]),
        fasta=str(test_paths["fasta"]),
        vcf=str(temp_output),
        intervals=str(test_paths["intervals"]),
        pon=str(test_paths["pon"]),
        germline=str(test_paths["germline"]),
        bam=str(test_paths["bam"]),
        f1r2=str(test_paths["f1r2"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    snakefile_content = captured.out

    assert "rule mutect:" in snakefile_content, "Missing rule definition in Snakefile"
    assert "input:" in snakefile_content, "Missing input section in Snakefile"
    assert "output:" in snakefile_content, "Missing output section in Snakefile"
    assert "wrapper:" in snakefile_content, "Missing wrapper section in Snakefile"

    assert "map=" in snakefile_content, "Missing 'map' input in Snakefile"
    assert "fasta=" in snakefile_content, "Missing 'fasta' input in Snakefile"
    assert "intervals=" in snakefile_content, "Missing 'intervals' input in Snakefile"
    assert "pon=" in snakefile_content, "Missing 'pon' input in Snakefile"
    assert "germline=" in snakefile_content, "Missing 'germline' input in Snakefile"
    assert "vcf=" in snakefile_content, "Missing 'vcf' output in Snakefile"
    assert "bam=" in snakefile_content, "Missing 'bam' output in Snakefile"
    assert "f1r2=" in snakefile_content, "Missing 'f1r2' output in Snakefile"


def test_run_mutect(test_paths, tmp_path):
    """Test that GATK Mutect can successfully run with test files."""
    from bioinformatics_mcp.gatk.mutect.run_mutect import run_mutect
    temp_output_vcf = tmp_path / "output.vcf"
    temp_output_bam = tmp_path / "output.bam"
    temp_output_f1r2 = tmp_path / "output_f1r2.txt"

    result = run_mutect(
        map=str(test_paths["map"]),
        fasta=str(test_paths["fasta"]),
        vcf=str(temp_output_vcf),
        intervals=str(test_paths["intervals"]),
        pon=str(test_paths["pon"]),
        germline=str(test_paths["germline"]),
        bam=str(temp_output_bam),
        f1r2=str(temp_output_f1r2),
    )

    assert result.returncode == 0, "Mutect tool run failed"
    assert temp_output_vcf.exists(), "VCF output file was not created"
    assert temp_output_bam.exists(), "BAM output file was not created"
    assert temp_output_f1r2.exists(), "F1R2 output file was not created"