import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "sequences": test_dir / "sequences.fasta",
        "decoys": test_dir / "decoys.txt",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_index_salmon(test_paths, tmp_path, capsys):
    """Test that Salmon index generates the expected Snakefile."""
    from run_index import run_index

    run_index(
        sequences=str(test_paths["sequences"]),
        decoys=str(test_paths["decoys"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule index:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "sequences=" in content, "Missing sequences input in Snakefile"
    assert "decoys=" in content, "Missing decoys input in Snakefile"


def test_run_index_salmon(test_paths, tmp_path):
    """Test that Salmon index can be run with the test files."""
    from run_index import run_index

    temp_output = tmp_path / "salmon_index_output"

    result = run_index(
        sequences=str(test_paths["sequences"]),
        decoys=str(test_paths["decoys"]),
        outdir=str(temp_output),
    )

    assert result.returncode == 0, "Salmon index run failed"
    assert temp_output.exists() and temp_output.is_dir(), "Output directory not created"