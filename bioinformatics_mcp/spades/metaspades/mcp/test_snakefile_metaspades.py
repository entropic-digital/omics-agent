import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).resolve().parent
    test_dir = base_dir / "test_files"
    return {
        "reads": test_dir / "test_reads.fastq",
        "output": test_dir / "output",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_metaspades(test_paths, tmp_path, capsys):
    """Test that metaspades generates the expected Snakefile."""
    from bioinformatics_mcp.spades.metaspades.run_metaspades import run_metaspades

    temp_output = tmp_path / "output_dir"
    temp_output.mkdir()

    # Generate the Snakefile with print_only=True to capture the content
    run_metaspades(
        reads=str(test_paths["reads"]),
        output=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential parameters and structure of the Snakefile
    assert "rule metaspades:" in content, "Missing rule definition 'metaspades'"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "threads:" in content, "Missing thread specification in Snakefile"
    assert "memory:" in content, "Missing memory specification in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "input.reads=" in content, "Missing required input 'reads'"
    assert "output.output=" in content, "Missing required output 'output'"


def test_run_metaspades(test_paths, tmp_path):
    """Test that metaspades can be run with the test files."""
    from bioinformatics_mcp.spades.metaspades.run_metaspades import run_metaspades

    temp_output = tmp_path / "output_dir"
    temp_output.mkdir()

    # Execute the metaspades tool
    result = run_metaspades(
        reads=str(test_paths["reads"]),
        output=str(temp_output),
        threads=2,
        memory=8,
    )

    # Verify the run is successful
    assert result.returncode == 0, "metaspades run failed"
    assert temp_output.is_dir(), "Output directory not created"
    # Add additional checks for expected output files if applicable
    # Example: assert (temp_output / "assembly.fasta").exists(), "Missing assembly output file"