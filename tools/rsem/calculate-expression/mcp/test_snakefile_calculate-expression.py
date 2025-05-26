import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam": test_dir / "test.bam",
        "fq_one": test_dir / "test_1.fastq",
        "fq_two": test_dir / "test_2.fastq",
        "reference": test_dir / "ref.idx",
        "reference_bowtie": test_dir / "ref_bowtie.idx",
        "genes_results": test_dir / "genes.results",
        "isoforms_results": test_dir / "isoforms.results",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_calculate_expression(test_paths, tmp_path, capsys):
    """Test that calculate-expression generates the expected Snakefile content."""
    from tools.rsem.calculate_expression.run_calculate_expression import run_calculate_expression

    run_calculate_expression(
        bam=str(test_paths["bam"]),
        fq_one=str(test_paths["fq_one"]),
        reference=str(test_paths["reference"]),
        reference_bowtie=str(test_paths["reference_bowtie"]),
        fq_two=str(test_paths["fq_two"]),
        genes_results=str(test_paths["genes_results"]),
        isoforms_results=str(test_paths["isoforms_results"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule calculate_expression:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "bam=" in content, "Missing bam parameter"
    assert "fq_one=" in content, "Missing fq_one parameter"
    assert "fq_two=" in content, "Missing fq_two parameter"
    assert "reference=" in content, "Missing reference parameter"
    assert "reference_bowtie=" in content, "Missing reference_bowtie parameter"
    assert "output:" in content, "Missing output section"
    assert "genes_results=" in content, "Missing genes_results parameter"
    assert "isoforms_results=" in content, "Missing isoforms_results parameter"
    assert "wrapper:" in content, "Missing wrapper section"


def test_run_calculate_expression(test_paths, tmp_path):
    """Test that calculate-expression can be run with the provided test files."""
    from tools.rsem.calculate_expression.run_calculate_expression import run_calculate_expression

    temp_genes_results = tmp_path / "temp_genes.results"
    temp_isoforms_results = tmp_path / "temp_isoforms.results"

    result = run_calculate_expression(
        bam=str(test_paths["bam"]),
        fq_one=str(test_paths["fq_one"]),
        reference=str(test_paths["reference"]),
        reference_bowtie=str(test_paths["reference_bowtie"]),
        fq_two=str(test_paths["fq_two"]),
        genes_results=str(temp_genes_results),
        isoforms_results=str(temp_isoforms_results),
    )

    assert result.returncode == 0, "calculate-expression execution failed"
    assert temp_genes_results.exists(), "Genes results file was not generated"
    assert temp_isoforms_results.exists(), "Isoforms results file was not generated"