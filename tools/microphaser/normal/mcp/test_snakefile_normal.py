import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Fixture to manage test file paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "example.bam",
        "bcf_file": test_dir / "example.bcf",
        "fasta_reference": test_dir / "reference.fasta",
        "gtf_annotation_file": test_dir / "annotation.gtf",
        "expected_peptide_fasta": test_dir / "expected_output.fasta",
    }

def test_snakefile_normal(test_paths, tmp_path, capsys):
    """Test that the normal tool generates the correct Snakefile."""
    from tools.microphaser.normal.run_normal import run_normal

    temp_output = tmp_path / "peptides.fasta"

    # Generate the Snakefile using print_only=True
    run_normal(
        bam_file=str(test_paths["bam_file"]),
        bcf_file=str(test_paths["bcf_file"]),
        fasta_reference=str(test_paths["fasta_reference"]),
        gtf_annotation_file=str(test_paths["gtf_annotation_file"]),
        peptide_fasta=str(temp_output),
        print_only=True,
    )

    # Capture the output Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Perform assertions to verify Snakefile correctness
    assert "rule normal:" in content, "Missing 'rule normal' definition"
    assert "input:" in content, "Missing 'input' section in Snakefile"
    assert "output:" in content, "Missing 'output' section in Snakefile"
    assert "wrapper:" in content, "Missing 'wrapper' section in Snakefile"
    assert "bam_file=" in content, "Missing 'bam_file' parameter in input section"
    assert "bcf_file=" in content, "Missing 'bcf_file' parameter in input section"
    assert "fasta_reference=" in content, "Missing 'fasta_reference' parameter in input section"
    assert "gtf_annotation_file=" in content, "Missing 'gtf_annotation_file' parameter in input section"
    assert "peptide_fasta=" in content, "Missing 'peptide_fasta' parameter in output section"

def test_run_normal(test_paths, tmp_path):
    """Test that the normal tool runs successfully with the given inputs."""
    from tools.microphaser.normal.run_normal import run_normal

    temp_output = tmp_path / "peptides.fasta"

    # Execute the normal tool
    result = run_normal(
        bam_file=str(test_paths["bam_file"]),
        bcf_file=str(test_paths["bcf_file"]),
        fasta_reference=str(test_paths["fasta_reference"]),
        gtf_annotation_file=str(test_paths["gtf_annotation_file"]),
        peptide_fasta=str(temp_output),
    )

    # Assert tool execution was successful
    assert result.returncode == 0, "Tool execution failed, non-zero return code"
    assert temp_output.exists(), "Expected output file was not generated"
    assert temp_output.stat().st_size > 0, "Output file is empty"