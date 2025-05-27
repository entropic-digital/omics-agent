import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fname_fasta": test_dir / "query.fasta",
        "fname_db": test_dir / "database.dmnd",
        "expected_output": test_dir / "expected_results.txt"
    }

def test_snakefile_blastp(test_paths, tmp_path, capsys):
    """Test that blastp generates the expected Snakefile."""
    from bioinformatics_mcp.diamond.mcp.run_blastp import run_blastp
    temp_output = tmp_path / "results.txt"

    run_blastp(
        fname_fasta=str(test_paths["fname_fasta"]),
        fname_db=str(test_paths["fname_db"]),
        fname=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule blastp:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "fname_fasta=" in content, "Missing fname_fasta parameter"
    assert "fname_db=" in content, "Missing fname_db parameter"
    assert "output=" in content, "Missing output parameter"

def test_run_blastp(test_paths, tmp_path):
    """Test that blastp tool executes successfully with test files."""
    from bioinformatics_mcp.diamond.mcp.run_blastp import run_blastp
    temp_output = tmp_path / "results.txt"

    result = run_blastp(
        fname_fasta=str(test_paths["fname_fasta"]),
        fname_db=str(test_paths["fname_db"]),
        fname=str(temp_output)
    )

    assert result.returncode == 0, "blastp run failed"
    assert temp_output.exists(), "Output file was not generated"
    assert temp_output.stat().st_size > 0, "Output file is empty"