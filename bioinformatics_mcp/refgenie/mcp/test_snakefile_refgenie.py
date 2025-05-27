import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "genome": test_dir / "genome.txt",
        "config": test_dir / "config.yaml",
        "expected_snakefile": test_dir / "Snakefile",
    }

def test_snakefile_refgenie(test_paths, tmp_path, capsys):
    """Test that refgenie generates the expected Snakefile."""
    from bioinformatics_mcp.refgenie.mcp.run_refgenie import run_refgenie
    temp_output = tmp_path / "output.txt"

    run_refgenie(
        action="build",
        genome=str(test_paths["genome"]),
        config=str(test_paths["config"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule refgenie:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "action=" in content, "Missing action parameter"
    assert "genome=" in content, "Missing genome parameter"
    assert "config=" in content, "Missing config parameter"

def test_run_refgenie(test_paths, tmp_path):
    """Test that refgenie can be run with the test files."""
    from bioinformatics_mcp.refgenie.mcp.run_refgenie import run_refgenie
    temp_output = tmp_path / "output.txt"

    result = run_refgenie(
        action="build",
        genome=str(test_paths["genome"]),
        config=str(test_paths["config"]),
    )

    assert result.returncode == 0, "refgenie run failed"