import pytest
from pathlib import Path
from bioinformatics_mcp.igv_reports.run_igv_reports import run_igv_reports

@pytest.fixture
def test_paths():
    """Set up test file paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam": test_dir / "test.bam",
        "vcf": test_dir / "test.vcf",
        "html": test_dir / "expected_output.html",
    }

def test_snakefile_igv_reports(test_paths, tmp_path, capsys):
    """Test that igv-reports generates the expected Snakefile."""
    temp_output = tmp_path / "output.html"

    run_igv_reports(
        bam=str(test_paths["bam"]),
        vcf=str(test_paths["vcf"]),
        html=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule igv_reports:" in content, "Missing rule definition for igv_reports"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper definition in Snakefile"
    assert "bam=" in content, "Missing BAM input parameter"
    assert "vcf=" in content, "Missing VCF input parameter"
    assert "html=" in content, "Missing HTML output parameter"

def test_run_igv_reports(test_paths, tmp_path):
    """Test that igv-reports runs successfully with test files."""
    temp_output = tmp_path / "output.html"

    result = run_igv_reports(
        bam=str(test_paths["bam"]),
        vcf=str(test_paths["vcf"]),
        html=str(temp_output),
    )

    assert result.returncode == 0, "igv-reports run failed"
    assert temp_output.exists(), "Expected output file was not created"