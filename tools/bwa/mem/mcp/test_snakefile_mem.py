import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fastq1": test_dir / "test_reads_1.fastq",
        "fastq2": test_dir / "test_reads_2.fastq",
        "reference": test_dir / "test_reference.fasta",
        "expected_output": test_dir / "expected_output.bam",
    }


def test_snakefile_mem(test_paths, tmp_path, capsys):
    """Test that the mem Snakefile is generated as expected."""
    from tools.bwa.mem.mcp.run_mem import run_mem

    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_mem(
        fastq_files=[str(test_paths["fastq1"]), str(test_paths["fastq2"])],
        reference_genome=str(test_paths["reference"]),
        output_file=str(temp_output),
        sorting="samtools",
        sort_extra="",
        extra="",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assertions for essential Snakefile properties
    assert "rule mem:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Assertions for required input parameters
    assert "fastq_files=" in content, "Missing fastq_files parameter"
    assert "reference_genome=" in content, "Missing reference_genome parameter"

    # Assertions for required output parameters
    assert "output_file=" in content, "Missing output_file parameter"

    # Assertions for optional parameters
    assert "params:" in content, "Missing params section in Snakefile"
    assert "extra=" in content, "Missing extra parameter"
    assert "sorting=" in content, "Missing sorting parameter"
    assert "sort_extra=" in content, "Missing sort_extra parameter"


def test_run_mem(test_paths, tmp_path):
    """Test that the mem tool runs successfully."""
    from tools.bwa.mem.mcp.run_mem import run_mem

    temp_output = tmp_path / "output.bam"

    result = run_mem(
        fastq_files=[str(test_paths["fastq1"]), str(test_paths["fastq2"])],
        reference_genome=str(test_paths["reference"]),
        output_file=str(temp_output),
        sorting="samtools",
        sort_extra="",
        extra="",
    )

    # Verify that the run completes successfully
    assert result.returncode == 0, "mem tool run failed"
    assert temp_output.exists(), "Output file was not created"
