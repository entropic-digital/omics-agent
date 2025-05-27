import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "vcf_file": test_dir / "input.vcf",
        "recal_file": test_dir / "output.recal",
        "tranches_file": test_dir / "output.tranches",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_variantrecalibrator(test_paths, tmp_path, capsys):
    """Test that VariantRecalibrator generates the expected Snakefile."""
    from bioinformatics_mcp.gatk.variantrecalibrator.run_variantrecalibrator import run_variantrecalibrator

    temp_recal = tmp_path / "output.recal"
    temp_tranches = tmp_path / "output.tranches"

    run_variantrecalibrator(
        vcf_file=str(test_paths["vcf_file"]),
        recal_file=str(temp_recal),
        tranches_file=str(temp_tranches),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule variantrecalibrator:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert str(test_paths["vcf_file"]) in content, "Missing VCF file input in Snakefile"
    assert str(temp_recal) in content, "Missing recal file output in Snakefile"
    assert str(temp_tranches) in content, "Missing tranches file output in Snakefile"


def test_run_variantrecalibrator(test_paths, tmp_path):
    """Test that VariantRecalibrator can be run with the test files."""
    from bioinformatics_mcp.gatk.variantrecalibrator.run_variantrecalibrator import run_variantrecalibrator

    temp_recal = tmp_path / "output.recal"
    temp_tranches = tmp_path / "output.tranches"

    result = run_variantrecalibrator(
        vcf_file=str(test_paths["vcf_file"]),
        recal_file=str(temp_recal),
        tranches_file=str(temp_tranches)
    )

    assert result.returncode == 0, "VariantRecalibrator execution failed"
    assert temp_recal.exists(), "Recal file not created"
    assert temp_tranches.exists(), "Tranches file not created"