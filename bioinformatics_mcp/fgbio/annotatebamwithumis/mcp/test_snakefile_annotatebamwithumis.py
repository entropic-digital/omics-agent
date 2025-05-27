import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths for annotatebamwithumis."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "test_input.bam",
        "input_fastq": test_dir / "test_input.fastq",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_annotatebamwithumis(test_paths, tmp_path, capsys):
    """Test that the annotatebamwithumis tool generates the expected Snakefile."""
    from bioinformatics_mcp.annotatebamwithumis.mcp.run_annotatebamwithumis import run_annotatebamwithumis
    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True
    run_annotatebamwithumis(
        input_bam=str(test_paths["input_bam"]),
        input_fastq=str(test_paths["input_fastq"]),
        output_bam=str(temp_output),
        print_only=True
    )

    # Capture the generated Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements in the Snakefile
    assert "rule annotatebamwithumis:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "input_bam=" in content, "Missing input_bam parameter"
    assert "input_fastq=" in content, "Missing input_fastq parameter"
    assert "output:" in content, "Missing output section"
    assert "output_bam=" in content, "Missing output_bam parameter"
    assert "params:" in content, "Missing params section"
    assert "umi_tag=" in content, "Missing umi_tag parameter"
    assert "discard_tag_failures=" in content, "Missing discard_tag_failures parameter"
    assert "max_records_in_ram=" in content, "Missing max_records_in_ram parameter"
    assert "compression_level=" in content, "Missing compression_level parameter"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "file:tools/fgbio/annotatebamwithumis" in content, "Incorrect or missing wrapper path"


def test_run_annotatebamwithumis(test_paths, tmp_path):
    """Test that the annotatebamwithumis tool executes correctly with test files."""
    from bioinformatics_mcp.annotatebamwithumis.mcp.run_annotatebamwithumis import run_annotatebamwithumis
    temp_output = tmp_path / "output.bam"

    # Run the tool with test inputs
    result = run_annotatebamwithumis(
        input_bam=str(test_paths["input_bam"]),
        input_fastq=str(test_paths["input_fastq"]),
        output_bam=str(temp_output)
    )

    # Verify the process completed successfully
    assert result.returncode == 0, "annotatebamwithumis run failed"
    assert temp_output.exists(), "Output BAM file was not created"