import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "input_fastq1": test_dir / "input_1.fastq",
        "input_fastq2": test_dir / "input_2.fastq",
        "output_trimmed_fastq1": test_dir / "output_trimmed_1.fastq",
        "output_trimmed_fastq2": test_dir / "output_trimmed_2.fastq",
        "output_stats": test_dir / "output_stats.txt",
    }


def test_snakefile_pe(test_paths, tmp_path, capsys):
    """Test that the cutadapt-pe Snakefile is generated correctly."""
    from run_pe import run_pe

    # Temporary paths for the outputs
    temp_trimmed_fastq1 = tmp_path / "temp_trimmed_1.fastq"
    temp_trimmed_fastq2 = tmp_path / "temp_trimmed_2.fastq"
    temp_stats = tmp_path / "temp_stats.txt"

    # Generate the Snakefile with print_only=True
    run_pe(
        input_fastq1=str(test_paths["input_fastq1"]),
        input_fastq2=str(test_paths["input_fastq2"]),
        output_trimmed_fastq1=str(temp_trimmed_fastq1),
        output_trimmed_fastq2=str(temp_trimmed_fastq2),
        output_stats=str(temp_stats),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile elements
    assert "rule cutadapt_pe:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "fastq1=" in content, "Missing fastq1 input parameter"
    assert "fastq2=" in content, "Missing fastq2 input parameter"
    assert "trimmed_fastq1=" in content, "Missing trimmed_fastq1 output parameter"
    assert "trimmed_fastq2=" in content, "Missing trimmed_fastq2 output parameter"
    assert "stats=" in content, "Missing stats output parameter"


def test_run_pe(test_paths, tmp_path):
    """Test that the cutadapt-pe tool executes successfully with sample files."""
    from run_pe import run_pe

    # Temporary paths for outputs
    temp_trimmed_fastq1 = tmp_path / "temp_trimmed_1.fastq"
    temp_trimmed_fastq2 = tmp_path / "temp_trimmed_2.fastq"
    temp_stats = tmp_path / "temp_stats.txt"

    # Run the tool
    result = run_pe(
        input_fastq1=str(test_paths["input_fastq1"]),
        input_fastq2=str(test_paths["input_fastq2"]),
        output_trimmed_fastq1=str(temp_trimmed_fastq1),
        output_trimmed_fastq2=str(temp_trimmed_fastq2),
        output_stats=str(temp_stats),
    )

    # Verify that the process completed successfully
    assert result.returncode == 0, "The cutadapt-pe tool execution failed"

    # Verify that output files are generated
    assert temp_trimmed_fastq1.exists(), "Trimmed FASTQ file 1 was not created"
    assert temp_trimmed_fastq2.exists(), "Trimmed FASTQ file 2 was not created"
    assert temp_stats.exists(), "Statistics file was not created"
