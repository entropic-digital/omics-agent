import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "alignments": test_dir / "test.bam",
        "ref": test_dir / "reference.fasta",
        "reference_genome_index": test_dir / "reference.fai",
        "expected_snakefile": test_dir / "expected_snakefile.smk",
        "output": test_dir / "output.bcf"
    }


def test_snakefile_mpileup(test_paths, tmp_path, capsys):
    """Test that mpileup generates the expected Snakefile."""
    from bioinformatics_mcp.bcftools.mpileup.run_mpileup import run_mpileup
    
    temp_output = tmp_path / "output.bcf"

    run_mpileup(
        alignments=str(test_paths["alignments"]),
        ref=str(test_paths["ref"]),
        reference_genome_index=str(test_paths["reference_genome_index"]),
        pileup_file=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential Snakefile elements are present
    assert "rule mpileup:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper definition in Snakefile"

    # Verify required inputs and outputs are present
    assert f"'{str(test_paths['alignments'])}'" in content, "Missing alignments input in Snakefile"
    assert f"'{str(test_paths['ref'])}'" in content, "Missing reference genome input in Snakefile"
    assert f"'{str(test_paths['reference_genome_index'])}'" in content, "Missing reference genome index in Snakefile"
    assert f"'{str(temp_output)}'" in content, "Missing pileup file output in Snakefile"


def test_run_mpileup(test_paths, tmp_path):
    """Test that mpileup can be run with the test files."""
    from bioinformatics_mcp.bcftools.mpileup.run_mpileup import run_mpileup
    
    temp_output = tmp_path / "output.bcf"

    result = run_mpileup(
        alignments=str(test_paths["alignments"]),
        ref=str(test_paths["ref"]),
        reference_genome_index=str(test_paths["reference_genome_index"]),
        pileup_file=str(temp_output)
    )

    # Verify the run is successful
    assert result.returncode == 0, "mpileup tool did not run successfully"

    # Verify output file is created
    assert temp_output.exists(), "Pileup output file was not created"