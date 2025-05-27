import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "calls": test_dir / "input_calls.vcf",
        "db": test_dir / "snpeff_db",
        "output_calls": test_dir / "output_calls.vcf",
        "output_genes": test_dir / "output_genes.txt",
        "output_stats": test_dir / "output_stats.txt",
        "output_csvstats": test_dir / "output_stats.csv",
    }

def test_snakefile_annotate(test_paths, tmp_path, capsys):
    """Test that the annotate tool generates the expected Snakefile."""
    from bioinformatics_mcp.snpeff.annotate.run_annotate import run_annotate

    temp_output = tmp_path / "output_calls.vcf"

    run_annotate(
        calls=str(test_paths["calls"]),
        db=str(test_paths["db"]),
        output_calls=str(temp_output),
        output_genes=str(test_paths["output_genes"]),
        output_stats=str(test_paths["output_stats"]),
        output_csvstats=str(test_paths["output_csvstats"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule annotate:" in content, "Missing rule definition for annotate"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "calls=" in content, "Missing input parameter for calls"
    assert "db=" in content, "Missing input parameter for db"
    assert "output_calls=" in content, "Missing output parameter for output_calls"
    assert "output_genes=" in content, "Missing output parameter for output_genes"
    assert "output_stats=" in content, "Missing output parameter for output_stats"
    assert "output_csvstats=" in content, "Missing output parameter for output_csvstats"

def test_run_annotate(test_paths, tmp_path):
    """Test that the annotate tool runs successfully with test files."""
    from bioinformatics_mcp.snpeff.annotate.run_annotate import run_annotate

    temp_output_calls = tmp_path / "output_calls.vcf"
    temp_output_genes = tmp_path / "output_genes.txt"
    temp_output_stats = tmp_path / "output_stats.txt"
    temp_output_csvstats = tmp_path / "output_stats.csv"

    result = run_annotate(
        calls=str(test_paths["calls"]),
        db=str(test_paths["db"]),
        output_calls=str(temp_output_calls),
        output_genes=str(temp_output_genes),
        output_stats=str(temp_output_stats),
        output_csvstats=str(temp_output_csvstats),
    )

    assert result.returncode == 0, "Annotate tool execution failed"
    assert temp_output_calls.exists(), "Output file for annotated calls was not created"
    assert temp_output_genes.exists(), "Output file for genes was not created"
    assert temp_output_stats.exists(), "Output stats file was not created"
    assert temp_output_csvstats.exists(), "Output CSV stats file was not created"