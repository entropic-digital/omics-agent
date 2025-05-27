import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "vcf": test_dir / "input.vcf",
        "ref": test_dir / "reference.fasta",
        "vcf_out": test_dir / "output.vcf",
        "stats_out": test_dir / "stats.txt",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_filtermutectcalls(test_paths, tmp_path, capsys):
    """Test that the filtermutectcalls tool generates the expected Snakefile."""
    from bioinformatics_mcp.gatk.filtermutectcalls.mcp.run_filtermutectcalls import run_filtermutectcalls
    temp_output = tmp_path / "output.vcf"

    run_filtermutectcalls(
        vcf=str(test_paths["vcf"]),
        ref=str(test_paths["ref"]),
        vcf_out=str(temp_output),
        stats_out=str(test_paths["stats_out"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule filtermutectcalls:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "vcf=" in content, "Missing vcf parameter"
    assert "ref=" in content, "Missing ref parameter"
    assert "vcf_out=" in content, "Missing vcf_out parameter"
    assert "stats_out=" in content, "Missing stats_out parameter"

def test_run_filtermutectcalls(test_paths, tmp_path):
    """Test that the filtermutectcalls tool can execute successfully."""
    from bioinformatics_mcp.gatk.filtermutectcalls.mcp.run_filtermutectcalls import run_filtermutectcalls
    temp_output = tmp_path / "output.vcf"

    result = run_filtermutectcalls(
        vcf=str(test_paths["vcf"]),
        ref=str(test_paths["ref"]),
        vcf_out=str(temp_output),
        stats_out=str(test_paths["stats_out"])
    )

    assert result.returncode == 0, "filtermutectcalls run failed"
    assert temp_output.exists(), "Filtered VCF file was not created"
    assert test_paths["stats_out"].exists(), "Stats output file was not created"