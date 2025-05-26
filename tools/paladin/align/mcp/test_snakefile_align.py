import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "nucleotide_reads": test_dir / "test_nucleotide_reads.fastq",
        "indexed_protein_fasta": test_dir / "test_indexed_protein.fasta",
        "mapped_reads": test_dir / "test_mapped_reads.sam",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_align(test_paths, tmp_path, capsys):
    """Test that the align tool generates the expected Snakefile."""
    from tools.paladin.align.run_align import run_align
    temp_output = tmp_path / "mapped_reads.sam"

    # Generate the Snakefile with print_only=True
    run_align(
        nucleotide_reads=str(test_paths["nucleotide_reads"]),
        indexed_protein_fasta=str(test_paths["indexed_protein_fasta"]),
        mapped_reads=str(temp_output),
        print_only=True,
    )

    # Capture printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile components
    assert "rule align:" in content, "Missing 'rule align:' definition"
    assert "input:" in content, "Missing 'input:' section"
    assert "output:" in content, "Missing 'output:' section"
    assert "wrapper:" in content, "Missing 'wrapper:' section"

    # Check inputs from meta.yaml
    assert "nucleotide_reads=" in content, "Missing 'nucleotide_reads' parameter in input"
    assert "indexed_protein_fasta=" in content, "Missing 'indexed_protein_fasta' parameter in input"

    # Check outputs from meta.yaml
    assert "mapped_reads=" in content, "Missing 'mapped_reads' parameter in output"


def test_run_align(test_paths, tmp_path):
    """Test that the align tool runs successfully with test files."""
    from tools.paladin.align.run_align import run_align
    temp_output = tmp_path / "test_mapped_reads.sam"

    # Run the tool with test inputs
    result = run_align(
        nucleotide_reads=str(test_paths["nucleotide_reads"]),
        indexed_protein_fasta=str(test_paths["indexed_protein_fasta"]),
        mapped_reads=str(temp_output),
    )

    # Verify the run is successful
    assert result.returncode == 0, "align tool execution failed"

    # Verify the output file is created
    assert temp_output.exists(), "Expected output file was not created"