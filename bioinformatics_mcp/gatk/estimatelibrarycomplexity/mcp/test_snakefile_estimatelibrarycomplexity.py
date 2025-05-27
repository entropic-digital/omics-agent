import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.bam",
        "output_file": test_dir / "test_output.metrics",
    }


def test_snakefile_estimatelibrarycomplexity(test_paths, tmp_path, capsys):
    """Test that estimatelibrarycomplexity generates the expected Snakefile."""
    from bioinformatics_mcp.gatk.estimatelibrarycomplexity.mcp.run_estimatelibrarycomplexity import run_estimatelibrarycomplexity

    temp_output = tmp_path / "output.metrics"

    # Generate the Snakefile with print_only=True
    run_estimatelibrarycomplexity(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule estimatelibrarycomplexity:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert f"'{str(test_paths['input_file'])}'" in content, "Missing input file"
    assert "output:" in content, "Missing output section"
    assert f"'{str(temp_output)}'" in content, "Missing output file"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "file:tools/gatk/estimatelibrarycomplexity" in content, "Incorrect wrapper path"


def test_run_estimatelibrarycomplexity(test_paths, tmp_path):
    """Test that estimatelibrarycomplexity can be run with the test files."""
    from bioinformatics_mcp.gatk.estimatelibrarycomplexity.mcp.run_estimatelibrarycomplexity import run_estimatelibrarycomplexity

    temp_output = tmp_path / "output.metrics"

    result = run_estimatelibrarycomplexity(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "estimatelibrarycomplexity run failed"
    assert temp_output.exists(), "Output file was not created"