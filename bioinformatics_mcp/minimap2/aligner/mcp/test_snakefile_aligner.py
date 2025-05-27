import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_files": [test_dir / "test_input1.fastq", test_dir / "test_input2.fastq"],
        "reference_genome": test_dir / "test_reference.fasta",
        "expected_snakefile": test_dir / "Snakefile",
        "expected_output": test_dir / "expected_output.bam"
    }

def test_snakefile_aligner(test_paths, tmp_path, capsys):
    """Test that the aligner's Snakefile is generated as expected."""
    from bioinformatics_mcp.minimap2.aligner.run_aligner import run_aligner

    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_aligner(
        input_files=[str(input_file) for input_file in test_paths["input_files"]],
        reference_genome=str(test_paths["reference_genome"]),
        output_file=str(temp_output),
        print_only=True
    )

    # Capture the generated Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule components are present
    assert "rule aligner:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "extra" in content, "Missing 'extra' parameter declaration"
    assert "sort" in content, "Missing 'sort' parameter declaration"
    assert "sort_extra" in content, "Missing 'sort_extra' parameter declaration"

    # Verify input and output paths
    for input_file in test_paths["input_files"]:
        assert str(input_file) in content, f"Missing input file {input_file} in Snakefile"
    assert str(test_paths["reference_genome"]) in content, "Missing reference genome in Snakefile"
    assert str(temp_output) in content, "Missing output file in Snakefile"

def test_run_aligner(test_paths, tmp_path):
    """Test that the aligner tool executes successfully with test files."""
    from bioinformatics_mcp.minimap2.aligner.run_aligner import run_aligner

    temp_output = tmp_path / "output.bam"

    result = run_aligner(
        input_files=[str(input_file) for input_file in test_paths["input_files"]],
        reference_genome=str(test_paths["reference_genome"]),
        output_file=str(temp_output)
    )

    # Verify completion and output
    assert result.returncode == 0, "aligner run failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"