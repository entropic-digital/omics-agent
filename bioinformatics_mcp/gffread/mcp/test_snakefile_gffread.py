import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fasta": test_dir / "test.fasta",
        "annotation": test_dir / "test.gtf",
        "records": test_dir / "expected_records.gff",
        "transcript_fasta": test_dir / "expected_transcripts.fasta",
        "cds_fasta": test_dir / "expected_cds.fasta",
        "protein_fasta": test_dir / "expected_proteins.fasta",
    }

def test_snakefile_gffread(test_paths, tmp_path, capsys):
    """Test that gffread generates the expected Snakefile."""
    from bioinformatics_mcp.gffread.mcp.run_gffread import run_gffread

    temp_records = tmp_path / "records.gff"
    temp_transcripts = tmp_path / "transcripts.fasta"
    temp_cds = tmp_path / "cds.fasta"
    temp_proteins = tmp_path / "proteins.fasta"

    run_gffread(
        fasta=str(test_paths["fasta"]),
        annotation=str(test_paths["annotation"]),
        records=str(temp_records),
        transcript_fasta=str(temp_transcripts),
        cds_fasta=str(temp_cds),
        protein_fasta=str(temp_proteins),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule gffread:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f'"{test_paths["fasta"]}"' in content, "Missing fasta input in Snakefile"
    assert f'"{test_paths["annotation"]}"' in content, "Missing annotation input in Snakefile"
    assert str(temp_records) in content, "Missing records output in Snakefile"
    assert str(temp_transcripts) in content, "Missing transcript_fasta output in Snakefile"
    assert str(temp_cds) in content, "Missing cds_fasta output in Snakefile"
    assert str(temp_proteins) in content, "Missing protein_fasta output in Snakefile"

def test_run_gffread(test_paths, tmp_path):
    """Test that gffread can be run with the test files."""
    from bioinformatics_mcp.gffread.mcp.run_gffread import run_gffread

    temp_records = tmp_path / "records.gff"
    temp_transcripts = tmp_path / "transcripts.fasta"
    temp_cds = tmp_path / "cds.fasta"
    temp_proteins = tmp_path / "proteins.fasta"

    result = run_gffread(
        fasta=str(test_paths["fasta"]),
        annotation=str(test_paths["annotation"]),
        records=str(temp_records),
        transcript_fasta=str(temp_transcripts),
        cds_fasta=str(temp_cds),
        protein_fasta=str(temp_proteins),
    )

    assert result.returncode == 0, "gffread run failed"
    assert temp_records.exists(), "Records output file missing after gffread run"
    assert temp_transcripts.exists(), "Transcript fasta file missing after gffread run"
    assert temp_cds.exists(), "CDS fasta file missing after gffread run"
    assert temp_proteins.exists(), "Protein fasta file missing after gffread run"