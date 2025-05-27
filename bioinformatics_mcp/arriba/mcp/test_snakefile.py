"""Module that tests if the arriba Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam": test_dir / "A.bam",
        "genome": test_dir / "genome.fasta",
        "annotation": test_dir / "annotation.gtf",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_ariba(test_paths, tmp_path, capsys):
    """Test that run_arriba generates the expected Snakefile."""
    from bioinformatics_mcp.arriba.mcp.run_arriba import run_arriba

    temp_output = tmp_path / "fusions.tsv"

    # Generate the Snakefile with print_only=True to capture the content
    run_arriba(
        bam=str(test_paths["bam"]),
        genome=str(test_paths["genome"]),
        annotation=str(test_paths["annotation"]),
        fusions=str(temp_output),
        extra="-i 1,2",
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule arriba:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam=" in content, "Missing bam input"
    assert "genome=" in content, "Missing genome input"
    assert "annotation=" in content, "Missing annotation input"
    assert "fusions=" in content, "Missing fusions output"


def test_run_arriba(test_paths, tmp_path):
    """Test that arriba can be run with the test files."""
    from bioinformatics_mcp.arriba.mcp.run_arriba import run_arriba

    temp_output = tmp_path / "fusions.tsv"

    result = run_arriba(
        bam=str(test_paths["bam"]),
        genome=str(test_paths["genome"]),
        annotation=str(test_paths["annotation"]),
        fusions=str(temp_output),
        extra="-i 1,2",
    )

    # Verify that the run is successful
    assert result.returncode == 0, "Arriba run failed"
