"""Module that tests if the sort Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_vcf": test_dir / "test_input.vcf",
        "expected_output_vcf": test_dir / "expected_output.vcf",
        "temp_dir": test_dir / "temp_folder",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_sort(test_paths, tmp_path, capsys):
    """Test that sort generates the expected Snakefile."""
    from bioinformatics_mcp.bcftools.sort.run_sort import run_sort

    temp_output = tmp_path / "output_sorted.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_sort(
        input_vcf=str(test_paths["input_vcf"]),
        output_vcf=str(temp_output),
        max_mem="2G",
        temp_dir=str(test_paths["temp_dir"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile rule elements are present
    assert "rule sort:" in content, "Missing rule definition in generated Snakefile"
    assert "input:" in content, "Missing input section in generated Snakefile"
    assert "output:" in content, "Missing output section in generated Snakefile"
    assert "params:" in content, "Missing params section in generated Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in generated Snakefile"

    # Verify required input parameters
    assert f'"{test_paths["input_vcf"]}"' in content, (
        "Missing input_vcf parameter in Snakefile"
    )

    # Verify required output parameters
    assert f'"{temp_output}"' in content, "Missing output_vcf parameter in Snakefile"

    # Verify required params
    assert "max_mem=" in content, "Missing max_mem parameter in Snakefile"
    assert "temp_dir=" in content, "Missing temp_dir parameter in Snakefile"


def test_run_sort(test_paths, tmp_path):
    """Test that sort can be run with the test files."""
    from bioinformatics_mcp.bcftools.sort.run_sort import run_sort

    temp_output = tmp_path / "output_sorted.vcf"

    # Run the sort tool
    result = run_sort(
        input_vcf=str(test_paths["input_vcf"]),
        output_vcf=str(temp_output),
        max_mem="2G",
        temp_dir=str(test_paths["temp_dir"]),
    )

    # Verify the execution was successful
    assert result.returncode == 0, "sort run failed"
    assert temp_output.exists(), "Output VCF file was not created"
