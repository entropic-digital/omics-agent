import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "test_input.bam",
        "index_file": test_dir / "test_index.str",
        "reference_genome": test_dir / "reference.fa",
        "expected_output": test_dir / "expected_output.genotype",
    }


def test_snakefile_call(test_paths, tmp_path, capsys):
    """Test that run_call generates the expected Snakefile."""
    from bioinformatics_mcp.strling.call.run_call import run_call

    temp_output = tmp_path / "output.genotype"

    # Generate the Snakefile with print_only=True to capture the content
    run_call(
        input_bam=str(test_paths["input_bam"]),
        index_file=str(test_paths["index_file"]),
        output_file=str(temp_output),
        reference_genome=str(test_paths["reference_genome"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements of the Snakefile
    assert "rule call:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper definition in Snakefile"
    # Verify required input parameters
    assert "input_bam=" in content, "Missing input_bam parameter"
    assert "index_file=" in content, "Missing index_file parameter"
    # Verify required output parameters
    assert "output_file=" in content, "Missing output_file parameter"
    # Verify optional parameters
    assert "reference_genome=" in content, "Missing reference_genome parameter"


def test_run_call(test_paths, tmp_path):
    """Test that run_call executes successfully with test files."""
    from bioinformatics_mcp.strling.call.run_call import run_call

    temp_output = tmp_path / "output.genotype"

    result = run_call(
        input_bam=str(test_paths["input_bam"]),
        index_file=str(test_paths["index_file"]),
        output_file=str(temp_output),
        reference_genome=str(test_paths["reference_genome"]),
    )

    # Verify the run is successful
    assert result.returncode == 0, "run_call execution failed"
    assert temp_output.exists(), "Output file was not generated"
