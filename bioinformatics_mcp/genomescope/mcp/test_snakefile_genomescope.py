import pytest
from pathlib import Path
from subprocess import CompletedProcess


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "kmer_histogram": test_dir / "kmer_histogram.txt",
        "inferred_genome_characteristics_and_plots": test_dir / "output_plots",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_genomescope(test_paths, tmp_path, capsys):
    """Test that genomescope generates the expected Snakefile."""
    from bioinformatics_mcp.genomescope.mcp.run_genomescope import run_genomescope

    temp_output = tmp_path / "output_dir"

    # Generate the Snakefile with print_only=True to capture the content
    run_genomescope(
        kmer_histogram=str(test_paths["kmer_histogram"]),
        inferred_genome_characteristics_and_plots=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in Snakefile
    assert "rule genomescope:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    # Verify required inputs
    assert "kmer_histogram=" in content, "Missing kmer_histogram input parameter"
    # Verify required outputs
    assert "inferred_genome_characteristics_and_plots=" in content, (
        "Missing inferred_genome_characteristics_and_plots output parameter"
    )
    # Verify wrapper path
    assert 'wrapper: "file:tools/genomescope"' in content, (
        "Incorrect or missing wrapper path"
    )


def test_run_genomescope(test_paths, tmp_path):
    """Test that genomescope can be run with the test files."""
    from bioinformatics_mcp.genomescope.mcp.run_genomescope import run_genomescope

    temp_output = tmp_path / "output_dir"

    # Execute the tool
    result = run_genomescope(
        kmer_histogram=str(test_paths["kmer_histogram"]),
        inferred_genome_characteristics_and_plots=str(temp_output),
    )

    # Verify the run is successful
    assert isinstance(result, CompletedProcess), (
        "Result is not a CompletedProcess instance"
    )
    assert result.returncode == 0, "genomescope tool execution failed"

    # Confirm that the expected output directory is created
    assert temp_output.exists(), "Output directory was not created"
    # Additional checks can be added for specific output files within the directory
