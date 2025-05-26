import pytest
from pathlib import Path
from tools.bwa.sampe.run_sampe import run_sampe


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "input_aln_sa": test_dir / "input_aln_sa.sai",
        "input_aln_sb": test_dir / "input_aln_sb.sai",
        "input_reads_a": test_dir / "input_reads_a.fastq",
        "input_reads_b": test_dir / "input_reads_b.fastq",
        "input_reference": test_dir / "reference.fasta",
        "output_sam": test_dir / "output.sam",
    }


def test_snakefile_sampe(test_paths, tmp_path, capsys):
    """Test that sampe generates the expected Snakefile."""
    temp_output = tmp_path / "output.sam"

    run_sampe(
        input_aln_sa=str(test_paths["input_aln_sa"]),
        input_aln_sb=str(test_paths["input_aln_sb"]),
        input_reads_a=str(test_paths["input_reads_a"]),
        input_reads_b=str(test_paths["input_reads_b"]),
        input_reference=str(test_paths["input_reference"]),
        output_sam=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    snakefile_content = captured.out

    assert "rule sampe:" in snakefile_content, "Missing rule definition (sampe)."
    assert "input:" in snakefile_content, "Missing input section in Snakefile."
    assert "output:" in snakefile_content, "Missing output section in Snakefile."
    assert "wrapper:" in snakefile_content, "Missing wrapper directive in Snakefile."

    # Verify required input elements
    assert "aln_sa=" in snakefile_content, "Missing input parameter: aln_sa."
    assert "aln_sb=" in snakefile_content, "Missing input parameter: aln_sb."
    assert "reads_a=" in snakefile_content, "Missing input parameter: reads_a."
    assert "reads_b=" in snakefile_content, "Missing input parameter: reads_b."
    assert "reference=" in snakefile_content, "Missing input parameter: reference."

    # Verify required output elements
    assert "sam=" in snakefile_content, "Missing output parameter: sam."


def test_run_sampe(test_paths, tmp_path):
    """Test that sampe can be run with the test files."""
    temp_output = tmp_path / "output.sam"

    result = run_sampe(
        input_aln_sa=str(test_paths["input_aln_sa"]),
        input_aln_sb=str(test_paths["input_aln_sb"]),
        input_reads_a=str(test_paths["input_reads_a"]),
        input_reads_b=str(test_paths["input_reads_b"]),
        input_reference=str(test_paths["input_reference"]),
        output_sam=str(temp_output),
    )

    assert result.returncode == 0, "sampe tool execution failed."
    assert temp_output.exists(), "Output SAM file was not created."
