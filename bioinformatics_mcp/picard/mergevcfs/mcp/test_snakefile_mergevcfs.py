import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths for input and output files."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test_files"
    return {
        "vcf_file1": test_dir / "vcf_file1.vcf",
        "vcf_file2": test_dir / "vcf_file2.vcf",
        "expected_merged_vcf": test_dir / "expected_merged.vcf",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_mergevcfs(test_paths, tmp_path, capsys):
    """Test that the mergevcfs tool generates a valid Snakefile."""
    from bioinformatics_mcp.picard.mergevcfs.run_mergevcfs import run_mergevcfs
    temp_output = tmp_path / "output.vcf"

    # Generate the Snakefile using print_only=True
    run_mergevcfs(
        vcf_files=[str(test_paths["vcf_file1"]), str(test_paths["vcf_file2"])],
        merged_vcf_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential parts of the Snakefile
    assert "rule mergevcfs:" in content, "Missing 'mergevcfs' rule definition."
    assert "input:" in content, "Missing input section in Snakefile."
    assert "output:" in content, "Missing output section in Snakefile."
    assert "params:" in content, "Missing params section in Snakefile."
    assert "wrapper:" in content, "Missing wrapper section in Snakefile."

    # Verify required inputs and outputs
    assert test_paths["vcf_file1"].name in content, "First VCF input file missing in Snakefile."
    assert test_paths["vcf_file2"].name in content, "Second VCF input file missing in Snakefile."
    assert str(temp_output) in content, "Output merged VCF file missing in Snakefile."

    # Verify wrapper location matches the tool
    assert "file:tools/picard/mergevcfs" in content, "Incorrect wrapper path in Snakefile."


def test_run_mergevcfs(test_paths, tmp_path):
    """Test that mergevcfs runs successfully with test VCF files."""
    from bioinformatics_mcp.picard.mergevcfs.run_mergevcfs import run_mergevcfs
    temp_output = tmp_path / "output.vcf"

    # Run the mergevcfs tool
    result = run_mergevcfs(
        vcf_files=[str(test_paths["vcf_file1"]), str(test_paths["vcf_file2"])],
        merged_vcf_file=str(temp_output),
    )

    # Verify the tool completed successfully
    assert result.returncode == 0, "mergevcfs run failed."

    # Verify the merged output file is created
    assert temp_output.exists(), "Merged VCF file was not created."

    # Verify the output file's content matches expectations (if applicable)
    with open(temp_output, "r") as temp, open(test_paths["expected_merged_vcf"], "r") as expected:
        temp_content = temp.read()
        expected_content = expected.read()
        assert temp_content == expected_content, "Merged VCF file content does not match expected output."