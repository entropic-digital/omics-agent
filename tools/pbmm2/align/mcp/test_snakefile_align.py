import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths for align tool."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_reads": test_dir / "test_reads.fasta",
        "reference_genome": test_dir / "test_reference.fasta",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "output_bam": test_dir / "test_output.bam",
    }


def test_snakefile_align(test_paths, tmp_path, capsys):
    """Test align tool generates the expected Snakefile."""
    from tools.pbmm2.align.run_align import run_align

    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True
    run_align(
        input_reads=str(test_paths["input_reads"]),
        reference_genome=str(test_paths["reference_genome"]),
        output_bam=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the generated Snakefile
    assert "rule align:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "input_reads=" in content, "Missing input_reads parameter in Snakefile"
    assert "reference_genome=" in content, (
        "Missing reference_genome parameter in Snakefile"
    )
    assert "output_bam=" in content, "Missing output_bam parameter in Snakefile"


def test_run_align_tool_execution(test_paths, tmp_path):
    """Test align tool execution with test files."""
    from tools.pbmm2.align.run_align import run_align

    temp_output = tmp_path / "output.bam"

    # Execute the tool with test input files
    result = run_align(
        input_reads=str(test_paths["input_reads"]),
        reference_genome=str(test_paths["reference_genome"]),
        output_bam=str(temp_output),
    )

    # Verify the tool execution was successful
    assert result.returncode == 0, "Align tool execution failed"

    # Verify the output BAM file is created
    assert temp_output.exists(), "Output BAM file was not created"
