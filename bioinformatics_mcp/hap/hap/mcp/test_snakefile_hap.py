"""Module that tests if the hap.py Snakefile is rendered and runnable"""

import pytest
from pathlib import Path
from subprocess import CompletedProcess


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_files"
    return {
        "truth_vcf": base_dir / "truth.vcf",
        "query_vcf": base_dir / "query.vcf",
        "reference": base_dir / "reference.fasta",
        "truth_bed": base_dir / "truth.bed",
        "query_bed": base_dir / "query.bed",
        "roc_levels": base_dir / "roc.levels",
        "expected_snakefile": base_dir / "expected_snakefile",
    }


def test_snakefile_hap_py(test_paths, tmp_path, capsys):
    """Test that hap.py generates the expected Snakefile."""
    from bioinformatics_mcp.hap.py.mcp.run_hap import run_hap

    # Generate the Snakefile with print_only=True
    run_hap(
        truth_vcf=str(test_paths["truth_vcf"]),
        query_vcf=str(test_paths["query_vcf"]),
        output_dir=str(tmp_path),
        reference=str(test_paths["reference"]),
        truth_bed=str(test_paths["truth_bed"]),
        query_bed=str(test_paths["query_bed"]),
        roc_levels=str(test_paths["roc_levels"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule hap_py:" in content, "Missing rule definition for hap.py"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "truth_vcf=" in content, "Missing truth_vcf parameter in Snakefile"
    assert "query_vcf=" in content, "Missing query_vcf parameter in Snakefile"
    assert "reference=" in content, "Missing reference parameter in Snakefile"
    assert "truth_bed=" in content, "Missing truth_bed parameter in Snakefile"
    assert "query_bed=" in content, "Missing query_bed parameter in Snakefile"
    assert "roc_levels=" in content, "Missing roc_levels parameter in Snakefile"
    assert "output_dir=" in content, "Missing output_dir parameter in Snakefile"


def test_run_hap_py(test_paths, tmp_path):
    """Test that hap.py can be run with the test files."""
    from bioinformatics_mcp.hap.py.mcp.run_hap import run_hap

    result: CompletedProcess = run_hap(
        truth_vcf=str(test_paths["truth_vcf"]),
        query_vcf=str(test_paths["query_vcf"]),
        output_dir=str(tmp_path),
        reference=str(test_paths["reference"]),
        truth_bed=str(test_paths["truth_bed"]),
        query_bed=str(test_paths["query_bed"]),
        roc_levels=str(test_paths["roc_levels"]),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "hap.py execution failed"
    assert (tmp_path / "output.ext").exists(), "Expected output file is missing"
