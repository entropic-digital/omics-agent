import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "gtf": test_dir / "input.gtf",
        "fasta": test_dir / "input.fasta",
        "spliced": test_dir / "input_spliced.fasta",
        "unspliced": test_dir / "input_unspliced.fasta",
        "output_fasta": test_dir / "output.fasta",
        "gene_id_to_name": test_dir / "gene_id_to_name.tsv",
        "t2g_3col": test_dir / "t2g_3col.tsv",
        "t2g": test_dir / "t2g.tsv",
        "g2g": test_dir / "g2g.tsv",
    }


def test_snakefile_makeunspliceunspliced(test_paths, tmp_path, capsys):
    """Test that makeunspliceunspliced generates the expected Snakefile."""
    from bioinformatics_mcp.pyroe.makeunspliceunspliced.run_makeunspliceunspliced import run_makeunspliceunspliced
    temp_output = tmp_path / "temp_output.fasta"

    run_makeunspliceunspliced(
        gtf=str(test_paths["gtf"]),
        fasta=str(test_paths["fasta"]),
        spliced=str(test_paths["spliced"]),
        unspliced=str(test_paths["unspliced"]),
        output_fasta=str(temp_output),
        gene_id_to_name=str(test_paths["gene_id_to_name"]),
        t2g_3col=str(test_paths["t2g_3col"]),
        t2g=str(test_paths["t2g"]),
        g2g=str(test_paths["g2g"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule makeunspliceunspliced:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"gtf={str(test_paths['gtf'])}" in content, "Missing gtf parameter"
    assert f"fasta={str(test_paths['fasta'])}" in content, "Missing fasta parameter"
    assert f"spliced={str(test_paths['spliced'])}" in content, "Missing spliced parameter"
    assert f"unspliced={str(test_paths['unspliced'])}" in content, "Missing unspliced parameter"
    assert "output.fasta=" in content, "Missing output_fasta parameter"
    assert f"gene_id_to_name={str(test_paths['gene_id_to_name'])}" in content, "Missing gene_id_to_name parameter"
    assert f"t2g_3col={str(test_paths['t2g_3col'])}" in content, "Missing t2g_3col parameter"
    assert f"t2g={str(test_paths['t2g'])}" in content, "Missing t2g parameter"
    assert f"g2g={str(test_paths['g2g'])}" in content, "Missing g2g parameter"


def test_run_makeunspliceunspliced(test_paths, tmp_path):
    """Test that makeunspliceunspliced can be run with the test files."""
    from bioinformatics_mcp.pyroe.makeunspliceunspliced.run_makeunspliceunspliced import run_makeunspliceunspliced
    temp_output = tmp_path / "output.fasta"

    result = run_makeunspliceunspliced(
        gtf=str(test_paths["gtf"]),
        fasta=str(test_paths["fasta"]),
        spliced=str(test_paths["spliced"]),
        unspliced=str(test_paths["unspliced"]),
        output_fasta=str(temp_output),
        gene_id_to_name=str(test_paths["gene_id_to_name"]),
        t2g_3col=str(test_paths["t2g_3col"]),
        t2g=str(test_paths["t2g"]),
        g2g=str(test_paths["g2g"]),
    )

    assert result.returncode == 0, "makeunspliceunspliced run failed"
    assert temp_output.exists(), "Output fasta file was not generated"