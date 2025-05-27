import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths for ngscstat testing."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "mapped_reads": test_dir / "mapped_reads.paf",
        "coverage": test_dir / "output_coverage.txt",
        "stats": test_dir / "output_stats.txt",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_ngscstat(test_paths, tmp_path, capsys):
    """Test that ngscstat generates the expected Snakefile."""
    from bioinformatics_mcp.purge_dups.ngscstat.run_ngscstat import run_ngscstat

    temp_coverage = tmp_path / "output_coverage.txt"
    temp_stats = tmp_path / "output_stats.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_ngscstat(
        mapped_reads=str(test_paths["mapped_reads"]),
        coverage=str(temp_coverage),
        stats=str(temp_stats),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule ngscstat:" in content, (
        "Snakefile is missing the 'rule ngscstat' definition."
    )
    assert "input:" in content, "Snakefile is missing the 'input' section."
    assert "output:" in content, "Snakefile is missing the 'output' section."
    assert "params:" in content, (
        "Snakefile is missing the 'params' section, required for additional options."
    )
    assert "wrapper:" in content, (
        "Snakefile is missing the 'wrapper' section that points to the tool."
    )

    # Verify the required input parameters from meta.yaml
    assert "mapped_reads=" in content, (
        "Snakefile is missing 'mapped_reads' input parameter."
    )
    # Verify the required outputs from meta.yaml
    assert "coverage=" in content, "Snakefile is missing coverage output parameter."
    assert "stats=" in content, "Snakefile is missing stats output parameter."


def test_run_ngscstat(test_paths, tmp_path):
    """Test that ngscstat can be run successfully with the provided files."""
    from bioinformatics_mcp.purge_dups.ngscstat.run_ngscstat import run_ngscstat

    temp_coverage = tmp_path / "output_coverage.txt"
    temp_stats = tmp_path / "output_stats.txt"

    # Run the tool with test files
    result = run_ngscstat(
        mapped_reads=str(test_paths["mapped_reads"]),
        coverage=str(temp_coverage),
        stats=str(temp_stats),
    )

    # Verify that the run is successful
    assert result.returncode == 0, (
        "ngscstat tool execution failed. Ensure the files are correct and the tool is functional."
    )

    # Verify output files were created
    assert temp_coverage.exists(), "Coverage output file was not created by ngscstat."
    assert temp_stats.exists(), "Stats output file was not created by ngscstat."
