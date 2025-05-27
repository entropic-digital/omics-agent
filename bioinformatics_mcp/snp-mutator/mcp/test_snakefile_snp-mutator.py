"""Module that tests if the snp-mutator Snakefile is rendered and runnable"""

import pytest
from pathlib import Path
from bioinformatics_mcp.snp_mutator.run_snp_mutator import run_snp_mutator


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_files"
    return {
        "reference_genome": base_dir / "reference_genome.fasta",
        "output_directory": base_dir / "output",
        "expected_snakefile": base_dir / "expected_Snakefile",
    }


def test_snakefile_snp_mutator(test_paths, tmp_path, capsys):
    """Test that snp-mutator generates the expected Snakefile."""
    # Generate the Snakefile with print_only=True
    run_snp_mutator(
        reference_genome=str(test_paths["reference_genome"]),
        output_directory=str(tmp_path / "output"),
        mutation_rate=0.01,
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify that essential elements are present
    assert "rule snp_mutator:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "reference_genome=" in content, "Missing reference genome input"
    assert "output:" in content, "Missing output section"
    assert "output_directory=" in content, "Missing output directory output"
    assert "params:" in content, "Missing params section"
    assert "mutation_rate=" in content, "Missing mutation rate in params"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "file:tools/snp-mutator" in content, "Missing correct wrapper path"


def test_run_snp_mutator(test_paths, tmp_path):
    """Test that snp-mutator can be run with the test files."""
    output_dir = tmp_path / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Run the tool
    result = run_snp_mutator(
        reference_genome=str(test_paths["reference_genome"]),
        output_directory=str(output_dir),
        mutation_rate=0.01,
    )

    # Verify the process completed successfully
    assert result.returncode == 0, "snp-mutator run failed"
    # Verify the output directory contains files
    output_files = list(output_dir.iterdir())
    assert len(output_files) > 0, "Expected output files are missing"
