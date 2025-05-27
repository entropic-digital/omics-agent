import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "ref": test_dir / "ref.fasta",
        "query": test_dir / "query.fasta",
        "fasta": test_dir / "output.fasta",
        "agp": test_dir / "output.agp",
        "stats": test_dir / "output.stats",
    }

def test_snakefile_scaffold(test_paths, tmp_path, capsys):
    """Test that ragtag-scaffold generates the expected Snakefile."""
    from bioinformatics_mcp.ragtag.scaffold.run_scaffold import run_scaffold

    # Generate the Snakefile with print_only=True
    run_scaffold(
        ref=str(test_paths["ref"]),
        query=str(test_paths["query"]),
        fasta=str(test_paths["fasta"]),
        agp=str(test_paths["agp"]),
        stats=str(test_paths["stats"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in the generated Snakefile
    assert "rule scaffold:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "ref=" in content, "Missing 'ref' input parameter"
    assert "query=" in content, "Missing 'query' input parameter"
    assert "fasta=" in content, "Missing 'fasta' output parameter"
    assert "agp=" in content, "Missing 'agp' output parameter"
    assert "stats=" in content, "Missing 'stats' output parameter"

def test_run_scaffold(test_paths, tmp_path):
    """Test that ragtag-scaffold can be executed with test files."""
    from bioinformatics_mcp.ragtag.scaffold.run_scaffold import run_scaffold

    temp_fasta = tmp_path / "scaffold_output.fasta"
    temp_agp = tmp_path / "scaffold_output.agp"
    temp_stats = tmp_path / "scaffold_output.stats"

    # Run the scaffold function
    result = run_scaffold(
        ref=str(test_paths["ref"]),
        query=str(test_paths["query"]),
        fasta=str(temp_fasta),
        agp=str(temp_agp),
        stats=str(temp_stats),
    )

    # Verify successful execution
    assert result.returncode == 0, "Scaffold execution failed"
    assert temp_fasta.exists(), "Output FASTA file was not created"
    assert temp_agp.exists(), "Output AGP file was not created"
    assert temp_stats.exists(), "Output stats file was not created"