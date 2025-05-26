import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths for samse tests."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_alignment_file": test_dir / "test_alignment.sai",
        "input_reads_file": test_dir / "test_reads.fastq",
        "reference_sequence_file": test_dir / "test_reference.fa",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "output_file": test_dir / "output.sam"
    }


def test_snakefile_samse(test_paths, tmp_path, capsys):
    """Test that samse generates the expected Snakefile."""
    from tools.bwa.samse.run_samse import run_samse

    temp_output = tmp_path / "output.sam"

    # Generate the Snakefile with print_only=True
    run_samse(
        input_alignment_file=str(test_paths["input_alignment_file"]),
        input_reads_file=str(test_paths["input_reads_file"]),
        reference_sequence_file=str(test_paths["reference_sequence_file"]),
        output_file=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assertions to check required Snakefile elements
    assert "rule samse:" in content, "Snakefile missing 'rule samse' definition."
    assert "input:" in content, "Snakefile missing 'input:' section."
    assert "output:" in content, "Snakefile missing 'output:' section."
    assert "wrapper:" in content, "Snakefile missing 'wrapper:' section."
    assert "input_alignment_file=" in content, "Snakefile missing 'input_alignment_file' input."
    assert "input_reads_file=" in content, "Snakefile missing 'input_reads_file' input."
    assert "reference_sequence_file=" in content, "Snakefile missing 'reference_sequence_file' input."
    assert "output_file=" in content, "Snakefile missing 'output_file' output."


def test_run_samse(test_paths, tmp_path):
    """Test that samse can execute successfully with test files."""
    from tools.bwa.samse.run_samse import run_samse

    temp_output = tmp_path / "output.sam"

    # Execute the samse tool
    result = run_samse(
        input_alignment_file=str(test_paths["input_alignment_file"]),
        input_reads_file=str(test_paths["input_reads_file"]),
        reference_sequence_file=str(test_paths["reference_sequence_file"]),
        output_file=str(temp_output)
    )

    # Validate successful execution
    assert result.returncode == 0, "samse execution failed with a non-zero return code."

    # Validate output file existence
    assert temp_output.exists(), "Output SAM file was not created by samse."