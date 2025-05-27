import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_vcf_bcf": test_dir / "test_input.vcf",
        "output_filtered_vcf_bcf": test_dir / "test_output.vcf",
    }


def test_snakefile_filter(test_paths, tmp_path, capsys):
    """Test that the filter tool generates the expected Snakefile."""
    from bioinformatics_mcp.bcftools.filter.run_filter import run_filter

    temp_output = tmp_path / "filtered_output.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_filter(
        input_vcf_bcf=str(test_paths["input_vcf_bcf"]),
        output_filtered_vcf_bcf=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements in the generated Snakefile
    assert "rule filter:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify all required inputs are defined
    assert "input_vcf_bcf=" in content, "Missing input_vcf_bcf parameter in Snakefile"

    # Verify the output is defined
    assert "output_filtered_vcf_bcf=" in content, (
        "Missing output_filtered_vcf_bcf parameter in Snakefile"
    )


def test_run_filter(test_paths, tmp_path):
    """Test that the filter tool can run successfully with test input files."""
    from bioinformatics_mcp.bcftools.filter.run_filter import run_filter

    temp_output = tmp_path / "filtered_output.vcf"

    # Execute the tool
    result = run_filter(
        input_vcf_bcf=str(test_paths["input_vcf_bcf"]),
        output_filtered_vcf_bcf=str(temp_output),
    )

    # Verify successful execution
    assert result.returncode == 0, "Filter tool execution failed"
    assert temp_output.exists(), "Output file was not created after filter execution"
