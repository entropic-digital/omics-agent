import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_data"  # Adjust path as needed
    return {
        "bam_file": base_dir / "test.bam",
        "gvcf_file": base_dir / "test.g.vcf",
        "expected_snakefile": base_dir / "expected_Snakefile",
    }


def test_snakefile_haplotypecaller(test_paths, tmp_path, capsys):
    """Test that haplotypecaller generates the expected Snakefile."""
    from bioinformatics_mcp.gatk.haplotypecaller.run_haplotypecaller import run_haplotypecaller

    temp_gvcf = tmp_path / "output.g.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_haplotypecaller(
        bam_file=str(test_paths["bam_file"]),
        gvcf_file=str(temp_gvcf),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule haplotypecaller:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert f"'{test_paths['bam_file']}'" in content, "Missing BAM input file"
    assert "output:" in content, "Missing output section"
    assert f"'{temp_gvcf}'" in content, "Missing GVCF output file"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "file:tools/gatk/haplotypecaller" in content, "Missing wrapper path"
    assert "params:" in content, "Missing params section"


def test_run_haplotypecaller(test_paths, tmp_path):
    """Test that haplotypecaller can be run with the test files."""
    from bioinformatics_mcp.gatk.haplotypecaller.run_haplotypecaller import run_haplotypecaller

    temp_gvcf = tmp_path / "output.g.vcf"

    # Run the haplotypecaller tool
    result = run_haplotypecaller(
        bam_file=str(test_paths["bam_file"]),
        gvcf_file=str(temp_gvcf),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "haplotypecaller run failed"

    # Verify output file is created
    assert temp_gvcf.exists(), "Output GVCF file was not created"
    assert temp_gvcf.stat().st_size > 0, "Output GVCF file is empty"