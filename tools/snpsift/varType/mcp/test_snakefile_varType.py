import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_vcf": test_dir / "input.vcf",
        "expected_output_vcf": test_dir / "expected_output.vcf",
    }


def test_snakefile_varType(test_paths, tmp_path, capsys):
    """Test that varType generates the expected Snakefile."""
    from tools.snpsift.varType.run_varType import run_varType
    temp_output = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_varType(
        input_vcf=str(test_paths["input_vcf"]),
        output_vcf=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential content of the Snakefile
    assert "rule varType:" in content, "Missing rule definition for varType"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper declaration in Snakefile"
    # Verify required inputs and outputs
    assert "input_vcf=" in content, "Missing input_vcf parameter in Snakefile"
    assert "output_vcf=" in content, "Missing output_vcf parameter in Snakefile"


def test_run_varType(test_paths, tmp_path):
    """Test that varType executes successfully with test files."""
    from tools.snpsift.varType.run_varType import run_varType
    temp_output = tmp_path / "output.vcf"

    # Run the varType function
    result = run_varType(
        input_vcf=str(test_paths["input_vcf"]),
        output_vcf=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "varType execution failed"

    # Check if output file is created
    assert temp_output.exists(), "Output VCF file was not created"

    # Ensure the output matches expectations (basic check)
    with open(temp_output, "r") as generated, open(test_paths["expected_output_vcf"], "r") as expected:
        assert generated.read() == expected.read(), "Output VCF file contents do not match expected"