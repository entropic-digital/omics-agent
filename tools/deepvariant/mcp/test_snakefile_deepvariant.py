import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fasta": test_dir / "test.fasta",
        "bam": test_dir / "test.bam",
        "vcf": test_dir / "output.vcf",
        "visual_report_html": test_dir / "output.html",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_deepvariant(test_paths, tmp_path, capsys):
    """Test that deepvariant generates the expected Snakefile."""
    from tools.deepvariant.mcp.run_deepvariant import run_deepvariant
    temp_vcf = tmp_path / "output.vcf"
    temp_html = tmp_path / "output.html"

    # Generate the Snakefile with print_only=True to capture the content
    run_deepvariant(
        fasta=str(test_paths["fasta"]),
        bam=str(test_paths["bam"]),
        vcf=str(temp_vcf),
        visual_report_html=str(temp_html),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the content of the generated Snakefile
    assert "rule deepvariant:" in content, "Missing rule definition in generated Snakefile."
    assert "input:" in content, "Missing input section in generated Snakefile."
    assert "output:" in content, "Missing output section in generated Snakefile."
    assert "wrapper:" in content, "Missing wrapper section in generated Snakefile."
    assert f"fasta={str(test_paths['fasta'])}" in content, "Missing fasta input in generated Snakefile."
    assert f"bam={str(test_paths['bam'])}" in content, "Missing bam input in generated Snakefile."
    assert f"vcf={str(temp_vcf)}" in content, "Missing vcf output in generated Snakefile."
    assert f"visual_report_html={str(temp_html)}" in content, "Missing visual_report_html output in generated Snakefile."

def test_run_deepvariant(test_paths, tmp_path):
    """Test that deepvariant can be run with the test files."""
    from tools.deepvariant.mcp.run_deepvariant import run_deepvariant
    temp_vcf = tmp_path / "output.vcf"
    temp_html = tmp_path / "output.html"

    result = run_deepvariant(
        fasta=str(test_paths["fasta"]),
        bam=str(test_paths["bam"]),
        vcf=str(temp_vcf),
        visual_report_html=str(temp_html)
    )

    # Verify that the process executed successfully
    assert result.returncode == 0, "deepvariant run failed."
    # Verify the expected output files are generated
    assert temp_vcf.exists(), "VCF output file was not generated."
    assert temp_html.exists(), "Visual report HTML file was not generated."