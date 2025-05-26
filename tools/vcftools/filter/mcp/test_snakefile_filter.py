import pytest
from pathlib import Path
from tools.vcftools.filter.run_filter import run_filter


@pytest.fixture
def test_paths():
    """Set up and provide test file paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test"
    input_vcf = test_dir / "input.vcf"
    expected_vcf = test_dir / "expected_output.vcf"
    return {
        "input_vcf": input_vcf,
        "expected_vcf": expected_vcf,
    }


def test_snakefile_filter(test_paths, tmp_path, capsys):
    """Test correct generation of the Snakefile for filtering."""
    temp_output = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True
    run_filter(
        input_vcf=str(test_paths["input_vcf"]),
        output_vcf=str(temp_output),
        print_only=True,
    )

    # Capture the generated Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Check for essential rule components
    assert "rule filter:" in content, "Snakefile missing 'filter' rule definition."
    assert "input:" in content, "Snakefile missing input section."
    assert "output:" in content, "Snakefile missing output section."
    assert "params:" in content, "Snakefile missing params section."
    assert "wrapper:" in content, "Snakefile missing wrapper declaration."

    # Verify required parameters and I/O structure
    assert f"input_vcf='{str(test_paths['input_vcf'])}'" in content, "Missing input VCF specification."
    assert f"output_vcf='{str(temp_output)}'" in content, "Missing output VCF specification."


def test_run_filter(test_paths, tmp_path):
    """Test the execution of the filter tool with test files."""
    temp_output = tmp_path / "output.vcf"

    # Run the filter tool
    result = run_filter(
        input_vcf=str(test_paths["input_vcf"]),
        output_vcf=str(temp_output),
    )

    # Check if the tool executed successfully
    assert result.returncode == 0, "Filter tool execution failed."

    # Verify output file existence
    assert temp_output.exists(), "Output VCF file not generated."

    # Additional test: Compare with expected output if needed (mocked or real test data can be used)
    # For demonstration: use simple content assertion if expected VCF is provided
    if test_paths["expected_vcf"].exists():
        with open(temp_output, "r") as output_file, open(test_paths["expected_vcf"], "r") as expected_file:
            assert (
                output_file.read() == expected_file.read()
            ), "Output VCF content does not match the expected output."
