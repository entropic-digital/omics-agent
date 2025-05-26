import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "sequence_fasta_file": test_dir / "test_sequences.fasta",
        "kmer_count_jf_file": test_dir / "test_kmer_counts.jf",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_count(test_paths, tmp_path, capsys):
    """Test that jellyfish_count generates the expected Snakefile."""
    from tools.jellyfish.count.mcp.run_count import run_count
    temp_output = tmp_path / "output.jf"

    # Generate the Snakefile with print_only=True
    run_count(
        sequence_fasta_file=str(test_paths["sequence_fasta_file"]),
        kmer_count_jf_file=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule jellyfish_count:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "sequence_fasta_file=" in content, "Missing sequence_fasta_file input parameter"
    assert "kmer_count_jf_file=" in content, "Missing kmer_count_jf_file output parameter"
    assert "tools/jellyfish/count" in content, "Incorrect wrapper path"


def test_run_jellyfish_count(test_paths, tmp_path):
    """Test that jellyfish_count can be run with the test files."""
    from tools.jellyfish.count.mcp.run_count import run_count
    temp_output = tmp_path / "output.jf"

    result = run_count(
        sequence_fasta_file=str(test_paths["sequence_fasta_file"]),
        kmer_count_jf_file=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "jellyfish_count run failed"
    assert temp_output.exists(), "Output file was not created"
