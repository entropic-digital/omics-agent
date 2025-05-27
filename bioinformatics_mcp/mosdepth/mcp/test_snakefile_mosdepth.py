import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam": test_dir / "test.bam",
        "reference_genome": test_dir / "reference.fasta",
        "bed_file": test_dir / "regions.bed",
        "expected_snakefile": test_dir / "Snakefile",
        "output_prefix": "test_output",
    }


def test_snakefile_mosdepth(test_paths, tmp_path, capsys):
    """Test that mosdepth generates the expected Snakefile."""
    from bioinformatics_mcp.mosdepth.mcp.run_mosdepth import run_mosdepth

    # Generate the Snakefile with print_only=True to capture the content
    run_mosdepth(
        bam_or_cram=str(test_paths["bam"]),
        reference_genome=str(test_paths["reference_genome"]),
        bed_file=str(test_paths["bed_file"]),
        output_prefix=test_paths["output_prefix"],
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule mosdepth:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f'"{test_paths["bam"]}"' in content, "BAM/CRAM input is missing"
    assert f'"{test_paths["reference_genome"]}"' in content, (
        "Reference genome input is missing"
    )
    assert f'"{test_paths["bed_file"]}"' in content, "BED file input is missing"
    assert f'output_prefix="{test_paths["output_prefix"]}"' in content, (
        "Output prefix is missing"
    )


def test_run_mosdepth(test_paths, tmp_path):
    """Test that mosdepth can be run with the test files."""
    from bioinformatics_mcp.mosdepth.mcp.run_mosdepth import run_mosdepth

    # Define temporary paths for output files
    output_dir = tmp_path
    output_prefix = output_dir / test_paths["output_prefix"]

    # Run the mosdepth tool
    result = run_mosdepth(
        bam_or_cram=str(test_paths["bam"]),
        reference_genome=str(test_paths["reference_genome"]),
        bed_file=str(test_paths["bed_file"]),
        output_prefix=str(output_prefix),
    )

    # Verify that the Snakemake run completes successfully
    assert result.returncode == 0, "mosdepth run failed"

    # Verify that output files are created
    coverage_file = (
        output_dir / f"{test_paths['output_prefix']}.mosdepth.global.dist.txt"
    )
    assert coverage_file.exists(), (
        f"Expected output file {coverage_file} was not created"
    )
