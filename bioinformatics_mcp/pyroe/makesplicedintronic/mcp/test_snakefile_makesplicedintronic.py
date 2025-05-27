import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test_data"
    return {
        "gtf": test_dir / "test.gtf",
        "fasta": test_dir / "test.fasta",
        "spliced": test_dir / "test.spliced.fasta",
        "unspliced": test_dir / "test.unspliced.fasta",
        "fasta_output": test_dir / "output_splici.fasta",
        "gene_id_to_name": test_dir / "gene_id_to_name.tsv",
        "t2g": test_dir / "t2g.tsv",
    }


def test_snakefile_makesplicedintronic(test_paths, tmp_path, capsys):
    """Test that makesplicedintronic generates the expected Snakefile."""
    from bioinformatics_mcp.pyroe.makesplicedintronic.run_makesplicedintronic import run_makesplicedintronic

    run_makesplicedintronic(
        gtf=str(test_paths["gtf"]),
        fasta=str(test_paths["fasta"]),
        spliced=str(test_paths["spliced"]),
        unspliced=str(test_paths["unspliced"]),
        fasta_output=str(test_paths["fasta_output"]),
        gene_id_to_name=str(test_paths["gene_id_to_name"]),
        t2g=str(test_paths["t2g"]),
        read_length=100,
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule makesplicedintronic:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "gtf=" in content, "Missing gtf input parameter"
    assert "fasta=" in content, "Missing fasta input parameter"
    assert "spliced=" in content, "Missing spliced input parameter"
    assert "unspliced=" in content, "Missing unspliced input parameter"
    assert "fasta=" in content, "Missing fasta output parameter"
    assert "gene_id_to_name=" in content, "Missing gene_id_to_name output parameter"
    assert "t2g=" in content, "Missing t2g output parameter"
    assert "read_length=" in content, "Missing read_length parameter"


def test_run_makesplicedintronic(test_paths, tmp_path):
    """Test that makesplicedintronic can be run with the test files."""
    from bioinformatics_mcp.pyroe.makesplicedintronic.run_makesplicedintronic import run_makesplicedintronic

    output_fasta = tmp_path / "test_splici.fasta"
    output_gene_id_to_name = tmp_path / "test_gene_id_to_name.tsv"
    output_t2g = tmp_path / "test_t2g.tsv"

    result = run_makesplicedintronic(
        gtf=str(test_paths["gtf"]),
        fasta=str(test_paths["fasta"]),
        spliced=str(test_paths["spliced"]),
        unspliced=str(test_paths["unspliced"]),
        fasta_output=str(output_fasta),
        gene_id_to_name=str(output_gene_id_to_name),
        t2g=str(output_t2g),
        read_length=100,
    )

    assert result.returncode == 0, "makesplicedintronic run failed"
    assert output_fasta.exists(), "Output fasta file was not created"
    assert output_gene_id_to_name.exists(), "Output gene_id_to_name file was not created"
    assert output_t2g.exists(), "Output t2g file was not created"