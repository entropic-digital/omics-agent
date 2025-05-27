import pytest
from pathlib import Path
from bioinformatics_mcp.reference.ensembl_mysql_table.run_ensembl_mysql_table import (
    run_ensembl_mysql_table,
)


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_species": test_dir / "species.txt",
        "input_build": test_dir / "build.txt",
        "input_release": test_dir / "release.txt",
        "input_main_tables": test_dir / "main_tables.json",
        "input_join_tables": test_dir / "join_tables.json",
        "output_tsv": test_dir / "output.tsv",
        "output_parquet": test_dir / "output.parquet",
    }


def test_snakefile_ensembl_mysql_table(test_paths, tmp_path, capsys):
    """Test that ensembl-mysql-table generates the expected Snakefile."""
    run_ensembl_mysql_table(
        species="Homo_sapiens",
        build="GRCh38",
        release="112",
        main_tables={"gene": "core"},
        join_tables={"transcript": {"database": "core", "join_column": "gene_id"}},
        output_tsv=str(tmp_path / "output.tsv"),
        output_parquet=str(tmp_path / "output.parquet"),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule ensembl_mysql_table:" in content, (
        "Missing ensembl_mysql_table rule definition"
    )
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "params:" in content, "Missing params section"
    assert "species=" in content, "Missing species parameter"
    assert "build=" in content, "Missing build parameter"
    assert "release=" in content, "Missing release parameter"
    assert "main_tables=" in content, "Missing main_tables parameter"
    assert "join_tables=" in content, "Missing join_tables parameter"
    assert "output_tsv=" in content, "Missing output_tsv parameter"
    assert "output_parquet=" in content, "Missing output_parquet parameter"


def test_run_ensembl_mysql_table(test_paths, tmp_path):
    """Test that ensembl-mysql-table runs successfully with test files."""
    temp_output_tsv = tmp_path / "output.tsv"
    temp_output_parquet = tmp_path / "output.parquet"

    result = run_ensembl_mysql_table(
        species="Homo_sapiens",
        build="GRCh38",
        release="112",
        main_tables={"gene": "core"},
        join_tables={"transcript": {"database": "core", "join_column": "gene_id"}},
        output_tsv=str(temp_output_tsv),
        output_parquet=str(temp_output_parquet),
    )

    assert result.returncode == 0, "ensembl-mysql-table execution failed"
    assert temp_output_tsv.exists(), "Output TSV file was not created"
    assert temp_output_parquet.exists(), "Output Parquet file was not created"
    assert temp_output_tsv.stat().st_size > 0, "Output TSV file is empty"
    assert temp_output_parquet.stat().st_size > 0, "Output Parquet file is empty"
