import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "genome_fasta": test_dir / "genome.fasta",
        "expected_snakefile": test_dir / "Snakefile",
        "output_prefix": test_dir / "output"
    }


def test_snakefile_wgsim(test_paths, tmp_path, capsys):
    """Test that wgsim generates the expected Snakefile."""
    from bioinformatics_mcp.wgsim.mcp.run_wgsim import run_wgsim

    # Generate the Snakefile with print_only=True to capture the content
    run_wgsim(
        read_length=150,
        mutation_rate=0.01,
        indel_fraction=0.001,
        coverage=20.0,
        genome_fasta=str(test_paths["genome_fasta"]),
        output_prefix=str(tmp_path / "output"),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule wgsim:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Add assertions for Snakefile parameters
    assert "genome_fasta=" in content, "Missing genome_fasta parameter in inputs"
    assert "output_prefix=" in content, "Missing output_prefix parameter in outputs"
    assert "read_length=" in content, "Missing read_length parameter in params"
    assert "mutation_rate=" in content, "Missing mutation_rate parameter in params"
    assert "indel_fraction=" in content, "Missing indel_fraction parameter in params"
    assert "coverage=" in content, "Missing coverage parameter in params"


def test_run_wgsim(test_paths, tmp_path):
    """Test that wgsim can be run with the test files."""
    from bioinformatics_mcp.wgsim.mcp.run_wgsim import run_wgsim
    output_prefix = tmp_path / "simulated_reads"

    result = run_wgsim(
        read_length=150,
        mutation_rate=0.01,
        indel_fraction=0.001,
        coverage=20.0,
        genome_fasta=str(test_paths["genome_fasta"]),
        output_prefix=str(output_prefix)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "wgsim run failed"
    # Check that the expected output files are generated
    assert (output_prefix.with_suffix(".1.fq")).exists(), "Missing output file: simulated_reads.1.fq"
    assert (output_prefix.with_suffix(".2.fq")).exists(), "Missing output file: simulated_reads.2.fq"