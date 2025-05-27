import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "variant_call_set": test_dir / "test_input.vcf",
        "output_vcf": test_dir / "test_output.vcf",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_leftalignandtrimvariants(test_paths, tmp_path, capsys):
    """Test that leftalignandtrimvariants generates the expected Snakefile."""
    from bioinformatics_mcp.gatk.leftalignandtrimvariants.mcp.run_leftalignandtrimvariants import run_leftalignandtrimvariants
    temp_output = tmp_path / "temp_output.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_leftalignandtrimvariants(
        variant_call_set=str(test_paths["variant_call_set"]),
        output_vcf=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule and sections are present in the Snakefile
    assert "rule leftalignandtrimvariants:" in content, "Missing rule definition for leftalignandtrimvariants"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify inputs and outputs are correctly defined
    assert test_paths["variant_call_set"].name in content, "Missing variant_call_set in input section"
    assert temp_output.name in content, "Missing output_vcf in output section"


def test_run_leftalignandtrimvariants(test_paths, tmp_path):
    """Test that leftalignandtrimvariants can be run with the test files."""
    from bioinformatics_mcp.gatk.leftalignandtrimvariants.mcp.run_leftalignandtrimvariants import run_leftalignandtrimvariants
    temp_output = tmp_path / "temp_output.vcf"

    result = run_leftalignandtrimvariants(
        variant_call_set=str(test_paths["variant_call_set"]),
        output_vcf=str(temp_output),
    )

    # Verify that the run completes successfully
    assert result.returncode == 0, "leftalignandtrimvariants run failed with non-zero return code"
    assert temp_output.exists(), "Output VCF file was not created"
