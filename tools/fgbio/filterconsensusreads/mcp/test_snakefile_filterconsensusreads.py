"""Module that tests if the filterconsensusreads Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam": test_dir / "input.bam",
        "vcf": [test_dir / "input1.vcf", test_dir / "input2.vcf"],
        "reference_genome": test_dir / "reference.fasta",
        "filtered_bam": test_dir / "output.filtered.bam",
    }


def test_snakefile_filterconsensusreads(test_paths, tmp_path, capsys):
    """Test that filterconsensusreads generates the expected Snakefile."""
    from tools.fgbio.filterconsensusreads.mcp.run_filterconsensusreads import (
        run_filterconsensusreads,
    )

    temp_output = tmp_path / "output.filtered.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_filterconsensusreads(
        bam=str(test_paths["bam"]),
        vcf=[str(v) for v in test_paths["vcf"]],
        reference_genome=str(test_paths["reference_genome"]),
        filtered_bam=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule filterconsensusreads:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Validate inputs
    assert "bam=" in content, "Missing BAM input parameter"
    for vcf in test_paths["vcf"]:
        assert str(vcf) in content, f"Missing VCF input: {vcf} parameter"
    assert "reference_genome=" in content, "Missing reference genome parameter"

    # Validate outputs
    assert "filtered_bam=" in content, "Missing filtered BAM output parameter"

    # Validate parameters
    assert "min_base_quality=" in content, "Missing min_base_quality parameter"
    assert "min_reads=" in content, "Missing min_reads parameter"


def test_run_filterconsensusreads(test_paths, tmp_path):
    """Test that filterconsensusreads can be run with the test files."""
    from tools.fgbio.filterconsensusreads.mcp.run_filterconsensusreads import (
        run_filterconsensusreads,
    )

    temp_output = tmp_path / "output.filtered.bam"

    result = run_filterconsensusreads(
        bam=str(test_paths["bam"]),
        vcf=[str(v) for v in test_paths["vcf"]],
        reference_genome=str(test_paths["reference_genome"]),
        filtered_bam=str(temp_output),
        min_base_quality=10,
        min_reads=[5, 10, 15],
    )

    # Verify that the run is successful
    assert result.returncode == 0, "filterconsensusreads run failed"

    # Verify that the output file exists
    assert temp_output.exists(), "Filtered BAM file was not created"
