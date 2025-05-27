import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "fasta_reference": test_dir / "test_reference.fasta",
        "indexed_db": test_dir / "test_indexed_db",
    }


def test_snakefile_lastdb(test_paths, tmp_path, capsys):
    """Test that lastdb generates the expected Snakefile."""
    from bioinformatics_mcp.last.mcp.run_lastdb import run_lastdb

    temp_output = tmp_path / "test_indexed_db"
    run_lastdb(
        fasta_reference=str(test_paths["fasta_reference"]),
        indexed_db=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule lastdb:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    assert "fasta_reference=" in content, "Missing fasta_reference input in Snakefile"
    assert "indexed_db=" in content, "Missing indexed_db output in Snakefile"


def test_run_lastdb(test_paths, tmp_path):
    """Test that lastdb can be run with the test files."""
    from bioinformatics_mcp.last.mcp.run_lastdb import run_lastdb

    temp_output = tmp_path / "test_indexed_db"
    result = run_lastdb(
        fasta_reference=str(test_paths["fasta_reference"]),
        indexed_db=str(temp_output)
    )

    assert result.returncode == 0, "lastdb execution failed"
    assert temp_output.exists(), "Indexed database output was not created"