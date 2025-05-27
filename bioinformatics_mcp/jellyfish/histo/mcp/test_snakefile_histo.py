import pytest
from pathlib import Path
import subprocess


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "kmer_count_jf_file": test_dir / "example.jf",
        "kmer_histogram_file": test_dir / "example.hist",
        "expected_snakefile": test_dir / "expected_snakefile.smk",
    }


def test_snakefile_histo(test_paths, tmp_path, capsys):
    """Test that histo generates the expected Snakefile."""
    from bioinformatics_mcp.jellyfish.histo.run_histo import run_histo

    temp_output = tmp_path / "output.hist"

    # Generate the Snakefile with print_only=True to capture the content
    run_histo(
        kmer_count_jf_file=str(test_paths["kmer_count_jf_file"]),
        kmer_histogram_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential Snakefile elements are present
    assert "rule histo:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify input parameters are correctly included
    assert f"kmer_count_jf_file={str(test_paths['kmer_count_jf_file'])}" in content, "Missing kmer_count_jf_file parameter"
    
    # Verify output parameters are correctly included
    assert f"kmer_histogram_file={str(temp_output)}" in content, "Missing kmer_histogram_file parameter"


def test_run_histo(test_paths, tmp_path):
    """Test that histo can be run with the test files."""
    from bioinformatics_mcp.jellyfish.histo.run_histo import run_histo

    temp_output = tmp_path / "output.hist"

    # Run the tool
    result = run_histo(
        kmer_count_jf_file=str(test_paths["kmer_count_jf_file"]),
        kmer_histogram_file=str(temp_output)
    )

    # Check the process ran successfully
    assert result.returncode == 0, "histo run failed with a non-zero exit code"

    # Verify the output file was created
    assert temp_output.exists(), "Expected output file was not created"

    # Add additional verification steps if required (e.g., file content checks)