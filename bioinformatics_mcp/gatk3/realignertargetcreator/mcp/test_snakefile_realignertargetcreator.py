import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "test.bam",
        "reference_genome": test_dir / "reference.fasta",
        "target_intervals": test_dir / "expected_intervals.list",
        "bed_file": test_dir / "regions.bed",
        "vcf_files_known_variation": test_dir / "known_variants.vcf",
    }


def test_snakefile_realignertargetcreator(test_paths, tmp_path, capsys):
    """Test that realignertargetcreator generates the expected Snakefile."""
    from bioinformatics_mcp.gatk3.realignertargetcreator.run_realignertargetcreator import run_realignertargetcreator

    run_realignertargetcreator(
        bam_file=str(test_paths["bam_file"]),
        reference_genome=str(test_paths["reference_genome"]),
        target_intervals=str(tmp_path / "output_intervals.list"),
        bed_file=str(test_paths["bed_file"]),
        vcf_files_known_variation=str(test_paths["vcf_files_known_variation"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule realignertargetcreator:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam_file=" in content, "Missing bam_file parameter"
    assert "reference_genome=" in content, "Missing reference_genome parameter"
    assert "target_intervals=" in content, "Missing target_intervals parameter"
    assert "bed_file=" in content, "Missing bed_file parameter"
    assert "vcf_files_known_variation=" in content, "Missing vcf_files_known_variation parameter"


def test_run_realignertargetcreator(test_paths, tmp_path):
    """Test that realignertargetcreator can be run with the test files."""
    from bioinformatics_mcp.gatk3.realignertargetcreator.run_realignertargetcreator import run_realignertargetcreator

    target_intervals = tmp_path / "output_intervals.list"

    result = run_realignertargetcreator(
        bam_file=str(test_paths["bam_file"]),
        reference_genome=str(test_paths["reference_genome"]),
        target_intervals=str(target_intervals),
        bed_file=str(test_paths["bed_file"]),
        vcf_files_known_variation=str(test_paths["vcf_files_known_variation"]),
    )

    assert result.returncode == 0, "realignertargetcreator run failed"
    assert target_intervals.exists(), "Target intervals file not generated"