import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "test_input.bam",
        "ref": test_dir / "test_reference.fasta",
        "output_vcf": test_dir / "test_output.vcf",
        "bed": test_dir / "test_regions.bed",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_call(test_paths, tmp_path, capsys):
    """Test that call generates the expected Snakefile."""
    from bioinformatics_mcp.call.mcp.run_call import run_call
    temp_output = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_call(
        input_bam=str(test_paths["input_bam"]),
        ref=str(test_paths["ref"]),
        output_vcf=str(temp_output),
        bed=str(test_paths["bed"]),
        sample_name="test_sample",
        threads=4,
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule call:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    # Check specific input parameters
    assert "input_bam=" in content, "Missing input_bam parameter in Snakefile"
    assert "ref=" in content, "Missing ref parameter in Snakefile"
    assert "bed=" in content, "Missing bed parameter in Snakefile"
    # Check specific output parameter
    assert "output_vcf=" in content, "Missing output_vcf parameter in Snakefile"
    # Check specific params
    assert "sample_name=" in content, "Missing sample_name parameter in Snakefile"
    assert "threads=" in content, "Missing threads parameter in Snakefile"


def test_run_call(test_paths, tmp_path):
    """Test that call can be executed using sample input files."""
    from bioinformatics_mcp.call.mcp.run_call import run_call
    temp_output = tmp_path / "output.vcf"

    result = run_call(
        input_bam=str(test_paths["input_bam"]),
        ref=str(test_paths["ref"]),
        output_vcf=str(temp_output),
        bed=str(test_paths["bed"]),
        sample_name="test_sample",
        threads=4
    )

    # Verify that the tool execution is successful
    assert result.returncode == 0, "call run failed"
    assert temp_output.exists(), "Output VCF file was not created"
    # Optional: Add further checks for the correctness of the output VCF file