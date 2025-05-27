import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test" / "data"
    return {
        "bam_file": test_dir / "test.bam",
        "reference_genome": test_dir / "reference.fa",
        "bed_file": test_dir / "regions.bed",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_manta(test_paths, tmp_path, capsys):
    """Test that manta generates the expected Snakefile."""
    from bioinformatics_mcp.manta.mcp.run_manta import run_manta

    # Generate the Snakefile with print_only=True to capture the content
    run_manta(
        bam_files=[str(test_paths["bam_file"])],
        reference_genome=str(test_paths["reference_genome"]),
        bed_file=str(test_paths["bed_file"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    snakefile_content = captured.out

    # Verify essential rule elements and parameters in Snakefile
    assert "rule manta:" in snakefile_content, "Missing rule definition in Snakefile"
    assert "input:" in snakefile_content, "Missing input section in Snakefile"
    assert "output:" in snakefile_content, "Missing output section in Snakefile"
    assert "wrapper:" in snakefile_content, "Missing wrapper directive in Snakefile"

    # Validate required inputs from meta.yaml
    assert "bam_files=" in snakefile_content, "Missing bam_files parameter in Snakefile"
    assert "reference_genome=" in snakefile_content, (
        "Missing reference_genome parameter in Snakefile"
    )
    assert "bed_file=" in snakefile_content, "Missing bed_file parameter in Snakefile"

    # Validate required outputs from meta.yaml
    assert "diploidSV.vcf.gz" in snakefile_content, (
        "Missing diploidSV.vcf.gz output in Snakefile"
    )
    assert "candidateSV.vcf.gz" in snakefile_content, (
        "Missing candidateSV.vcf.gz output in Snakefile"
    )
    assert "candidateSmallIndels.vcf.gz" in snakefile_content, (
        "Missing candidateSmallIndels.vcf.gz output in Snakefile"
    )


def test_run_manta(test_paths, tmp_path):
    """Test that manta can be executed with the test files."""
    from bioinformatics_mcp.manta.mcp.run_manta import run_manta

    output_dir = tmp_path / "manta_output"
    output_dir.mkdir()

    # Execute the manta tool
    result = run_manta(
        bam_files=[str(test_paths["bam_file"])],
        reference_genome=str(test_paths["reference_genome"]),
        bed_file=str(test_paths["bed_file"]),
        output_dir=str(output_dir),
    )

    # Verify tool execution was successful
    assert result.returncode == 0, "manta tool execution failed"

    # Verify expected output files are generated in the output directory
    expected_outputs = [
        output_dir / "results" / "variants" / "diploidSV.vcf.gz",
        output_dir / "results" / "variants" / "candidateSV.vcf.gz",
        output_dir / "results" / "variants" / "candidateSmallIndels.vcf.gz",
    ]

    for output_file in expected_outputs:
        assert output_file.exists(), f"Missing expected output file: {output_file}"
