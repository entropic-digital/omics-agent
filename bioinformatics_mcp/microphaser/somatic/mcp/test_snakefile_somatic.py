import pytest
from pathlib import Path
import subprocess


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "test.bam",
        "bcf_file": test_dir / "test.bcf",
        "fasta_reference": test_dir / "test_reference.fasta",
        "gtf_annotation_file": test_dir / "test_annotation.gtf",
        "mutated_peptide_fasta": test_dir / "mutated_peptides.fasta",
        "wildtype_peptide_fasta": test_dir / "wildtype_peptides.fasta",
        "information_tsv": test_dir / "information.tsv",
    }


def test_snakefile_somatic(test_paths, tmp_path, capsys):
    """Test that somatic generates the expected Snakefile."""
    from bioinformatics_mcp.microphaser.somatic.run_somatic import run_somatic

    # Temporary output file
    temp_mutated_fasta = tmp_path / "temp_mutated_peptides.fasta"
    temp_wildtype_fasta = tmp_path / "temp_wildtype_peptides.fasta"
    temp_info_tsv = tmp_path / "temp_information.tsv"

    # Generate the Snakefile with print_only=True to capture the content
    run_somatic(
        bam_file=str(test_paths["bam_file"]),
        bcf_file=str(test_paths["bcf_file"]),
        fasta_reference=str(test_paths["fasta_reference"]),
        gtf_annotation_file=str(test_paths["gtf_annotation_file"]),
        mutated_peptide_fasta=str(temp_mutated_fasta),
        wildtype_peptide_fasta=str(temp_wildtype_fasta),
        information_tsv=str(temp_info_tsv),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential components are present in Snakefile
    assert "rule somatic:" in content, "Missing rule definition for somatic"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper declaration in Snakefile"

    # Verify all required inputs
    assert "bam_file=" in content, "Missing bam_file input in Snakefile"
    assert "bcf_file=" in content, "Missing bcf_file input in Snakefile"
    assert "fasta_reference=" in content, "Missing fasta_reference input in Snakefile"
    assert "gtf_annotation_file=" in content, (
        "Missing gtf_annotation_file input in Snakefile"
    )

    # Verify all required outputs
    assert "mutated_peptide_fasta=" in content, (
        "Missing mutated_peptide_fasta output in Snakefile"
    )
    assert "wildtype_peptide_fasta=" in content, (
        "Missing wildtype_peptide_fasta output in Snakefile"
    )
    assert "information_tsv=" in content, "Missing information_tsv output in Snakefile"


def test_run_somatic(test_paths, tmp_path):
    """Test that somatic can be run with the test files."""
    from bioinformatics_mcp.microphaser.somatic.run_somatic import run_somatic

    # Temporary output paths
    temp_mutated_fasta = tmp_path / "output_mutated_peptides.fasta"
    temp_wildtype_fasta = tmp_path / "output_wildtype_peptides.fasta"
    temp_info_tsv = tmp_path / "output_information.tsv"

    # Run the tool with test files
    result = run_somatic(
        bam_file=str(test_paths["bam_file"]),
        bcf_file=str(test_paths["bcf_file"]),
        fasta_reference=str(test_paths["fasta_reference"]),
        gtf_annotation_file=str(test_paths["gtf_annotation_file"]),
        mutated_peptide_fasta=str(temp_mutated_fasta),
        wildtype_peptide_fasta=str(temp_wildtype_fasta),
        information_tsv=str(temp_info_tsv),
    )

    # Verify the tool runs successfully
    assert result.returncode == 0, "Somatic tool execution failed"
    assert temp_mutated_fasta.exists(), "Mutated peptide FASTA file not generated"
    assert temp_wildtype_fasta.exists(), "Wildtype peptide FASTA file not generated"
    assert temp_info_tsv.exists(), "Information TSV file not generated"
