import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "normal_pileup": test_dir / "normal.pileup",
        "tumor_pileup": test_dir / "tumor.pileup",
        "expected_output_vcf": test_dir / "expected_output.vcf",
    }


def test_snakefile_somatic(test_paths, tmp_path, capsys):
    """Test that somatic generates the expected Snakefile."""
    from bioinformatics_mcp.varscan.somatic.run_somatic import run_somatic
    temp_vcf = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_somatic(
        normal_pileup=str(test_paths["normal_pileup"]),
        tumor_pileup=str(test_paths["tumor_pileup"]),
        output_vcf=str(temp_vcf),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule somatic:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Verify input parameters
    assert f"normal_pileup={test_paths['normal_pileup']}" in content, "Missing normal_pileup parameter"
    assert f"tumor_pileup={test_paths['tumor_pileup']}" in content, "Missing tumor_pileup parameter"
    # Verify output parameters
    assert f"output_vcf={temp_vcf}" in content, "Missing output_vcf parameter"
    # Check that the wrapper path is correct
    assert "tools/varscan/somatic" in content, "Incorrect or missing wrapper path"


def test_run_somatic(test_paths, tmp_path):
    """Test that somatic can be run with the test files."""
    from bioinformatics_mcp.varscan.somatic.run_somatic import run_somatic
    temp_vcf = tmp_path / "output.vcf"

    result = run_somatic(
        normal_pileup=str(test_paths["normal_pileup"]),
        tumor_pileup=str(test_paths["tumor_pileup"]),
        output_vcf=str(temp_vcf),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "Somatic run failed"

    # Verify that the output VCF file is generated
    assert temp_vcf.exists(), "Output VCF file was not generated"
    assert temp_vcf.stat().st_size > 0, "Output VCF file is empty"