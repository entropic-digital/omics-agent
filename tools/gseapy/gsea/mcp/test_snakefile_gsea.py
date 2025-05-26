import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "gmt": test_dir / "example.gmt",
        "expr": test_dir / "example_expression.rnk",
        "cls": test_dir / "example.cls",
        "rank": test_dir / "example_rank.rnk",
        "gene_list": test_dir / "example_gene_list.txt",
        "background": test_dir / "example_background.txt",
        "outdir": test_dir / "output",
        "pkl": test_dir / "output.pkl",
    }

def test_snakefile_gsea(test_paths, tmp_path, capsys):
    """Test that gsea generates the expected Snakefile."""
    from tools.gseapy.gsea.run_gsea import run_gsea
    run_gsea(
        gmt=str(test_paths["gmt"]),
        expr=str(test_paths["expr"]),
        cls=str(test_paths["cls"]),
        rank=str(test_paths["rank"]),
        gene_list=str(test_paths["gene_list"]),
        background=str(test_paths["background"]),
        outdir=str(test_paths["outdir"]),
        pkl=str(test_paths["pkl"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule gsea:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "gmt=" in content, "Missing 'gmt' parameter in Snakefile input"
    assert "expr=" in content, "Missing 'expr' parameter in Snakefile input"
    assert "cls=" in content, "Missing 'cls' parameter in Snakefile input"
    assert "rank=" in content, "Missing 'rank' parameter in Snakefile input"
    assert "gene_list=" in content, "Missing 'gene_list' parameter in Snakefile input"
    assert "background=" in content, "Missing 'background' parameter in Snakefile input"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "outdir=" in content, "Missing 'outdir' parameter in Snakefile output"
    assert "pkl=" in content, "Missing 'pkl' parameter in Snakefile output"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "file:tools/gseapy/gsea" in content, "Missing correct wrapper path in Snakefile"

def test_run_gsea(test_paths, tmp_path):
    """Test that gsea runs successfully with the provided inputs."""
    from tools.gseapy.gsea.run_gsea import run_gsea

    temp_outdir = tmp_path / "output"
    temp_pkl = tmp_path / "output.pkl"

    result = run_gsea(
        gmt=str(test_paths["gmt"]),
        expr=str(test_paths["expr"]),
        cls=str(test_paths["cls"]),
        rank=str(test_paths["rank"]),
        gene_list=str(test_paths["gene_list"]),
        background=str(test_paths["background"]),
        outdir=str(temp_outdir),
        pkl=str(temp_pkl)
    )

    assert result.returncode == 0, f"gsea run failed with return code {result.returncode}"
    assert temp_outdir.exists(), "Output directory was not created"
    assert temp_pkl.exists(), "Pickle file was not created in output directory"