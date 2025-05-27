import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_vcf": test_dir / "input.vcf",
        "output_vcf": test_dir / "output.vcf",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_call_bcftools(test_paths, tmp_path, capsys):
    """Test that bcftools call generates the expected Snakefile."""
    from bioinformatics_mcp.bcftools.call.run_call import run_call
    temp_output = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True to capture content
    run_call(
        input_vcf=str(test_paths["input_vcf"]),
        output_vcf=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in the Snakefile
    assert "rule call:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"input_vcf='{test_paths['input_vcf']}'" in content, "Missing input_vcf parameter"
    assert f"output_vcf='{temp_output}'" in content, "Missing output_vcf parameter"

def test_run_call_bcftools(test_paths, tmp_path):
    """Test that bcftools call tool executes with the test files."""
    from bioinformatics_mcp.bcftools.call.run_call import run_call
    temp_output = tmp_path / "output.vcf"

    result = run_call(
        input_vcf=str(test_paths["input_vcf"]),
        output_vcf=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "bcftools call execution failed"
    assert temp_output.exists(), "Output file was not created"