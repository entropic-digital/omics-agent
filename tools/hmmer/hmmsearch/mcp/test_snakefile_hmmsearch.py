import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "hmm_profiles": test_dir / "test_profiles.hmm",
        "sequence_database": test_dir / "test_sequences.fasta",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_hmmsearch(test_paths, tmp_path, capsys):
    """Test that hmmsearch generates the expected Snakefile."""
    from tools.hmmer.hmmsearch.run_hmmsearch import run_hmmsearch
    temp_output = tmp_path / "matches_output.txt"

    run_hmmsearch(
        hmm_profiles=str(test_paths["hmm_profiles"]),
        sequence_database=str(test_paths["sequence_database"]),
        matches_output=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule hmmsearch:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "hmm_profiles=" in content, "Missing hmm_profiles parameter"
    assert "sequence_database=" in content, "Missing sequence_database parameter"
    assert "matches_output=" in content, "Missing matches_output parameter"

def test_run_hmmsearch(test_paths, tmp_path):
    """Test that hmmsearch can be run with the test files."""
    from tools.hmmer.hmmsearch.run_hmmsearch import run_hmmsearch
    temp_output = tmp_path / "matches_output.txt"

    result = run_hmmsearch(
        hmm_profiles=str(test_paths["hmm_profiles"]),
        sequence_database=str(test_paths["sequence_database"]),
        matches_output=str(temp_output)
    )

    assert result.returncode == 0, "hmmsearch run failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"