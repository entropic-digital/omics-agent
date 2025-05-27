import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Fixture to manage test file paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test_files" / "separate"
    return {
        "bam_file": test_dir / "test.bam",
        "fastq1": test_dir / "output_1.fastq",
        "fastq2": test_dir / "output_2.fastq",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_separate(test_paths, tmp_path, capsys):
    """Test that separate generates the expected Snakefile."""
    from bioinformatics_mcp.samtools.fastq.separate.run_separate import run_separate

    # Generate Snakefile with print_only=True
    run_separate(
        bam_file=str(test_paths["bam_file"]),
        fastq1=str(test_paths["fastq1"]),
        fastq2=str(test_paths["fastq2"]),
        print_only=True,
    )

    # Capture and inspect the generated Snakefile
    captured = capsys.readouterr()
    content = captured.out

    # Assertions to verify essential elements in the Snakefile
    assert "rule separate:" in content, "Rule definition for 'separate' is missing."
    assert "input:" in content, "Input section is missing."
    assert "output:" in content, "Output section is missing."
    assert "params:" in content, "Params section is missing."
    assert "wrapper:" in content, "Wrapper section is missing."

    # Verify correct inputs in the Snakefile
    assert f"'{test_paths['bam_file']}'" in content, "Input BAM file is missing."
    # Verify correct outputs in the Snakefile
    assert f"'{test_paths['fastq1']}'" in content, "Output FastQ1 file is missing."
    assert f"'{test_paths['fastq2']}'" in content, "Output FastQ2 file is missing."


def test_run_separate(test_paths, tmp_path):
    """Test that the separate tool runs successfully with test files."""
    from bioinformatics_mcp.samtools.fastq.separate.run_separate import run_separate

    # Create temporary output files
    fastq1_temp = tmp_path / "output_1.fastq"
    fastq2_temp = tmp_path / "output_2.fastq"

    # Run the separate tool
    result = run_separate(
        bam_file=str(test_paths["bam_file"]),
        fastq1=str(fastq1_temp),
        fastq2=str(fastq2_temp),
    )

    # Assertions to verify successful execution
    assert result.returncode == 0, "Tool execution failed with non-zero return code."

    # Verify output files are generated
    assert fastq1_temp.exists(), "Output FASTQ1 file was not created."
    assert fastq2_temp.exists(), "Output FASTQ2 file was not created."

    # (Optional) Add extra validation for file contents if necessary
