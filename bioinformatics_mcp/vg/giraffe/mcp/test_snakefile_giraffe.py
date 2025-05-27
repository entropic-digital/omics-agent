import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fastq_file1": test_dir / "input1.fastq",
        "fastq_file2": test_dir / "input2.fastq",
        "reference_graph": test_dir / "reference_graph.gfa",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_giraffe(test_paths, tmp_path, capsys):
    """Test that giraffe generates the expected Snakefile."""
    from bioinformatics_mcp.vg.giraffe.run_giraffe import run_giraffe
    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_giraffe(
        fastq_files=[str(test_paths["fastq_file1"]), str(test_paths["fastq_file2"])],
        reference_graph=str(test_paths["reference_graph"]),
        output_file=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential elements are present in the Snakefile
    assert "rule giraffe:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper reference in Snakefile"

    # Verify required input keys are rendered
    assert "fastq=" in content, "Missing 'fastq' input key in Snakefile"
    assert "reference_graph=" in content, "Missing 'reference_graph' key in Snakefile"

    # Verify required output key is rendered
    assert "output=" in content, "Missing 'output' key in Snakefile"

    # Verify required wrapper path
    assert "file:tools/vg/giraffe" in content, "Incorrect wrapper path in Snakefile"


def test_run_giraffe(test_paths, tmp_path):
    """Test that giraffe can be run with the test files."""
    from bioinformatics_mcp.vg.giraffe.run_giraffe import run_giraffe
    temp_output = tmp_path / "output.bam"

    result = run_giraffe(
        fastq_files=[str(test_paths["fastq_file1"]), str(test_paths["fastq_file2"])],
        reference_graph=str(test_paths["reference_graph"]),
        output_file=str(temp_output)
    )

    # Verify that tool execution is successful
    assert result.returncode == 0, "giraffe execution failed"
    assert temp_output.exists(), "Output file not created after giraffe execution"