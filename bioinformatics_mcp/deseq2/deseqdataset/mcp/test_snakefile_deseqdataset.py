import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "colData": test_dir / "colData.tsv",
        "counts": test_dir / "counts.tsv",
        "output": test_dir / "output.rds",
    }

def test_snakefile_deseqdataset(test_paths, tmp_path, capsys):
    """Test that deseqdataset generates the expected Snakefile."""
    from bioinformatics_mcp.deseq2.deseqdataset.run_deseqdataset import run_deseqdataset
    temp_output = tmp_path / "output.rds"

    run_deseqdataset(
        colData=str(test_paths["colData"]),
        counts=str(test_paths["counts"]),
        output=str(temp_output),
        formula="~ condition",
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule deseqdataset:" in content, "Missing 'deseqdataset' rule in Snakefile"
    assert "input:" in content, "Missing 'input' section"
    assert "output:" in content, "Missing 'output' section"
    assert "params:" in content, "Missing 'params' section"
    assert "wrapper:" in content, "Missing 'wrapper' section"
    assert "colData=" in content, "Missing 'colData' input in Snakefile"
    assert "counts=" in content, "Missing 'counts' input in Snakefile"
    assert "output=" in content, "Missing 'output' parameter in Snakefile"
    assert "formula=" in content, "Missing 'formula' parameter in Snakefile"

def test_run_deseqdataset(test_paths, tmp_path):
    """Test that deseqdataset runs successfully with test files."""
    from bioinformatics_mcp.deseq2.deseqdataset.run_deseqdataset import run_deseqdataset
    temp_output = tmp_path / "output.rds"

    result = run_deseqdataset(
        colData=str(test_paths["colData"]),
        counts=str(test_paths["counts"]),
        output=str(temp_output),
        formula="~ condition"
    )

    assert result.returncode == 0, "deseqdataset run failed"
    assert temp_output.exists(), "Output file was not created"