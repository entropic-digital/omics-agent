import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "fasta": test_dir / "test.fasta",
        "expected_snakefile": test_dir / "expected_snakefile.smk",
        "output": test_dir / "output",
    }

def test_snakefile_makeblastdb(test_paths, tmp_path, capsys):
    """Test that makeblastdb generates the expected Snakefile."""
    from bioinformatics_mcp.blast.makeblastdb.run_makeblastdb import run_makeblastdb

    run_makeblastdb(
        fasta=str(test_paths["fasta"]),
        output=str(tmp_path / "output"),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule makeblastdb:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f"fasta='{test_paths['fasta']}'" in content, "Missing fasta input in Snakefile"
    assert "output=" in content, "Missing output parameter in Snakefile"

def test_run_makeblastdb(test_paths, tmp_path):
    """Test that makeblastdb can be run with the test files."""
    from bioinformatics_mcp.blast.makeblastdb.run_makeblastdb import run_makeblastdb

    output_path = tmp_path / "output"
    result = run_makeblastdb(
        fasta=str(test_paths["fasta"]),
        output=str(output_path),
    )

    assert result.returncode == 0, "makeblastdb execution failed"
    expected_extensions = [".nin", ".nsq", ".nhr"]
    for ext in expected_extensions:
        assert (output_path.parent / f"output{ext}").exists(), f"Missing {ext} file in output"