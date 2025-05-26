import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "test_dir": test_dir,
        "input_tsv": test_dir / "test_input.tsv",
        "output_tsv": test_dir / "test_output.tsv",
        "output_parquet": test_dir / "test_output.parquet",
    }


def test_snakefile_ensembl_biomart_table(test_paths, tmp_path, capsys):
    """Test that ensembl-biomart-table generates the expected Snakefile."""
    from tools.reference.ensembl_biomart_table.mcp.run_ensembl_biomart_table import (
        run_ensembl_biomart_table,
    )

    output_tsv = tmp_path / "output.tsv"
    output_parquet = tmp_path / "output.parquet"

    # Generate the Snakefile with print_only=True to capture the content
    run_ensembl_biomart_table(
        biomart="genes",
        species="homo_sapiens",
        build="GRCh38",
        release="112",
        attributes=["ensembl_gene_id", "ensembl_transcript_id"],
        filters={"chromosome_name": ["X", "Y"]},
        output_tsv=str(output_tsv),
        output_parquet=str(output_parquet),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements
    assert "rule ensembl_biomart_table:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "params:" in content, "Missing params section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "biomart=" in content, "Missing biomart parameter"
    assert "species=" in content, "Missing species parameter"
    assert "build=" in content, "Missing build parameter"
    assert "release=" in content, "Missing release parameter"
    assert "attributes=" in content, "Missing attributes parameter"
    assert "filters=" in content, "Missing filters parameter"
    assert "output_tsv=" in content, "Missing output_tsv parameter"
    assert "output_parquet=" in content, "Missing output_parquet parameter"


def test_run_ensembl_biomart_table(test_paths, tmp_path):
    """Test that ensembl-biomart-table can be run with the test files."""
    from tools.reference.ensembl_biomart_table.mcp.run_ensembl_biomart_table import (
        run_ensembl_biomart_table,
    )

    output_tsv = tmp_path / "output.tsv"
    output_parquet = tmp_path / "output.parquet"

    # Run the tool with test parameters
    result = run_ensembl_biomart_table(
        biomart="genes",
        species="homo_sapiens",
        build="GRCh38",
        release="112",
        attributes=["ensembl_gene_id", "ensembl_transcript_id"],
        filters={"chromosome_name": ["X", "Y"]},
        output_tsv=str(output_tsv),
        output_parquet=str(output_parquet),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "ensembl-biomart-table run failed"

    # Verify that the output files are created
    assert output_tsv.exists(), "Output TSV file was not created"
    assert output_parquet.exists(), "Output Parquet file was not created"
