import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "test_sra": test_dir / "test.sra",
        "output_dir": test_dir / "output",
        "expected_snakefile": test_dir / "expected_snakefile.txt",
    }


def test_snakefile_fasterq_dump(test_paths, tmp_path, capsys):
    """Test that fasterq-dump generates the expected Snakefile."""
    from bioinformatics_mcp.sra_tools.fasterq_dump.run_fasterq_dump import run_fasterq_dump

    temp_output_dir = tmp_path / "output"
    temp_output_dir.mkdir()

    run_fasterq_dump(
        sra_accession="SRR123456", output_dir=str(temp_output_dir), print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in the generated Snakefile
    assert "rule fasterq_dump:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "sra_accession=" in content, "Missing sra_accession input"
    assert "output_dir=" in content, "Missing output_dir parameter"


def test_run_fasterq_dump(test_paths, tmp_path):
    """Test that fasterq-dump can be executed with the test files."""
    from bioinformatics_mcp.sra_tools.fasterq_dump.run_fasterq_dump import run_fasterq_dump

    temp_output_dir = tmp_path / "output"
    temp_output_dir.mkdir()

    result = run_fasterq_dump(
        sra_accession=str(test_paths["test_sra"]), output_dir=str(temp_output_dir)
    )

    # Assert the process ran successfully
    assert result.returncode == 0, "fasterq-dump process failed"
    # Verify output directory contains expected FASTQ files
    fastq_files = list(temp_output_dir.glob("*.fastq"))
    assert len(fastq_files) > 0, "No FASTQ files produced in output directory"
    assert any(f.name.endswith("_1.fastq") for f in fastq_files), (
        "Missing R1 FASTQ file"
    )
    assert any(f.name.endswith("_2.fastq") for f in fastq_files), (
        "Missing R2 FASTQ file"
    )
