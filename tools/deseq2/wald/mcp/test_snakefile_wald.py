import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "dds": test_dir / "dds.rds",
        "wald_rds": test_dir / "wald_results.rds",
        "wald_tsv": test_dir / "wald_results.tsv",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_wald(test_paths, tmp_path, capsys):
    """Test that the wald tool generates the expected Snakefile."""
    from tools.deseq2.wald.run_wald import run_wald
    
    run_wald(
        dds=str(test_paths["dds"]),
        wald_rds=str(test_paths["wald_rds"]),
        wald_tsv=str(test_paths["wald_tsv"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule wald:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "dds=" in content, "Missing dds input"
    assert "wald_rds=" in content, "Missing wald_rds output"
    assert "wald_tsv=" in content, "Missing wald_tsv output"


def test_run_wald(test_paths, tmp_path):
    """Test that the wald tool can be executed with test files."""
    from tools.deseq2.wald.run_wald import run_wald

    output_dir = tmp_path / "output"
    output_dir.mkdir()
    wald_rds_output = output_dir / "wald_results.rds"
    wald_tsv_output = output_dir / "wald_results.tsv"

    result = run_wald(
        dds=str(test_paths["dds"]),
        wald_rds=str(wald_rds_output),
        wald_tsv=str(wald_tsv_output),
    )

    assert result.returncode == 0, "wald tool execution failed"
    assert wald_rds_output.exists(), "Missing wald_rds output file"
    assert wald_tsv_output.exists(), "Missing wald_tsv output file"