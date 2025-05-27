import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "vcf_file1": test_dir / "input1.vcf",
        "vcf_file2": test_dir / "input2.vcf",
        "expected_snakefile": test_dir / "Snakefile",
        "output_file": test_dir / "output.vcf"
    }


def test_snakefile_concat(test_paths, tmp_path, capsys):
    """Test that bcftools concat generates the expected Snakefile."""
    from bioinformatics_mcp.bcftools.concat.run_concat import run_concat
    temp_output = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_concat(
        vcf_files=[str(test_paths["vcf_file1"]), str(test_paths["vcf_file2"])],
        output_file=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present in the generated Snakefile
    assert "rule concat:" in content, "Missing 'concat' rule definition."
    assert "input:" in content, "Missing input section."
    assert "output:" in content, "Missing output section."
    assert "params:" in content, "Missing params section."
    assert "wrapper:" in content, "Missing wrapper section."

    # Verify required input VCF files in Snakefile
    assert str(test_paths["vcf_file1"]) in content, "Missing input VCF file 1 in Snakefile."
    assert str(test_paths["vcf_file2"]) in content, "Missing input VCF file 2 in Snakefile."

    # Verify required output file in Snakefile
    assert str(temp_output) in content, "Missing output file in Snakefile."


def test_run_concat(test_paths, tmp_path):
    """Test that bcftools concat can be run with the test files."""
    from bioinformatics_mcp.bcftools.concat.run_concat import run_concat
    temp_output = tmp_path / "output.vcf"

    # Run the concat tool
    result = run_concat(
        vcf_files=[str(test_paths["vcf_file1"]), str(test_paths["vcf_file2"])],
        output_file=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "bcftools concat run failed."
    assert temp_output.exists(), "Output file was not created."

    # Add additional checks if content verification is required
    assert temp_output.stat().st_size > 0, "Output file is empty."
