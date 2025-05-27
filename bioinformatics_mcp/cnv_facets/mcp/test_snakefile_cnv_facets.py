import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "tumor": test_dir / "tumor.bam",
        "normal": test_dir / "normal.bam",
        "vcf": test_dir / "variants.vcf.gz",
        "pileup": test_dir / "pileup.csv.gz",
        "output_vcf": test_dir / "output.vcf.gz",
        "cnv": test_dir / "cnv.png",
        "hist": test_dir / "hist.pdf",
        "spider": test_dir / "spider.pdf",
    }


def test_snakefile_cnv_facets(test_paths, tmp_path, capsys):
    """Test that cnv_facets generates the expected Snakefile."""
    from bioinformatics_mcp.cnv_facets.mcp.run_cnv_facets import run_cnv_facets

    run_cnv_facets(
        tumor=str(test_paths["tumor"]),
        normal=str(test_paths["normal"]),
        vcf=str(test_paths["vcf"]),
        pileup=str(test_paths["pileup"]),
        output_vcf=str(test_paths["output_vcf"]),
        cnv=str(test_paths["cnv"]),
        hist=str(test_paths["hist"]),
        spider=str(test_paths["spider"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule cnv_facets:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "tumor=" in content, "Missing tumor parameter in inputs"
    assert "normal=" in content, "Missing normal parameter in inputs"
    assert "vcf=" in content, "Missing vcf parameter in inputs"
    assert "pileup=" in content, "Missing pileup parameter in inputs"
    assert "vcf=" in content, "Missing vcf parameter in outputs"
    assert "cnv=" in content, "Missing cnv parameter in outputs"
    assert "hist=" in content, "Missing hist parameter in outputs"
    assert "spider=" in content, "Missing spider parameter in outputs"


def test_run_cnv_facets(test_paths, tmp_path):
    """Test that cnv_facets can be run with the test files."""
    from bioinformatics_mcp.cnv_facets.mcp.run_cnv_facets import run_cnv_facets

    temp_output_vcf = tmp_path / "output.vcf.gz"
    temp_cnv = tmp_path / "cnv.png"
    temp_hist = tmp_path / "hist.pdf"
    temp_spider = tmp_path / "spider.pdf"

    result = run_cnv_facets(
        tumor=str(test_paths["tumor"]),
        normal=str(test_paths["normal"]),
        vcf=str(test_paths["vcf"]),
        pileup=str(test_paths["pileup"]),
        output_vcf=str(temp_output_vcf),
        cnv=str(temp_cnv),
        hist=str(temp_hist),
        spider=str(temp_spider),
    )

    assert result.returncode == 0, "cnv_facets run failed"
    assert temp_output_vcf.exists(), "Expected output VCF not generated"
    assert temp_cnv.exists(), "Expected CNV plot not generated"
    assert temp_hist.exists(), "Expected histogram plot not generated"
    assert temp_spider.exists(), "Expected spider plot not generated"