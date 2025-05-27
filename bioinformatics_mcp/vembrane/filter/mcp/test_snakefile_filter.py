import pytest
from pathlib import Path
import subprocess


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_vcf": test_dir / "input.vcf",
        "expected_output_vcf": test_dir / "expected_output.vcf",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_filter(test_paths, tmp_path, capsys):
    """Test that vembrane filter generates the expected Snakefile."""
    from bioinformatics_mcp.vembrane.filter.run_filter import run_filter

    temp_output_vcf = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_filter(
        input_vcf=str(test_paths["input_vcf"]),
        output_vcf=str(temp_output_vcf),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the Snakefile
    assert "rule vembrane_filter:" in content, "Missing rule definition for vembrane_filter"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "input_vcf=" in content, "Missing input_vcf parameter in Snakefile"
    assert "output_vcf=" in content, "Missing output_vcf parameter in Snakefile"


def test_run_filter(test_paths, tmp_path):
    """Test that vembrane filter can be run with the test files."""
    from bioinformatics_mcp.vembrane.filter.run_filter import run_filter

    temp_output_vcf = tmp_path / "output.vcf"

    # Run vembrane filter tool
    result = run_filter(
        input_vcf=str(test_paths["input_vcf"]),
        output_vcf=str(temp_output_vcf),
    )

    # Verify that the tool execution is successful
    assert result.returncode == 0, "vembrane filter run failed"

    # Verify the output file is created
    assert temp_output_vcf.exists(), "Output VCF file was not created"

    # Optionally, validate output content against expected (e.g., diff or file content checks)
    # if test_paths["expected_output_vcf"].exists():
    #     with open(temp_output_vcf, 'r') as generated, open(test_paths["expected_output_vcf"], 'r') as expected:
    #         assert generated.read() == expected.read(), "Output VCF content does not match expected"
