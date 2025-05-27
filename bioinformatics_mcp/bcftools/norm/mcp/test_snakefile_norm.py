import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_vcf": test_dir / "input.vcf",
        "fasta_ref": test_dir / "reference.fasta",
        "output_vcf": test_dir / "output.vcf",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_norm(test_paths, tmp_path, capsys):
    """Test that norm generates the expected Snakefile."""
    from bioinformatics_mcp.norm.mcp.run_norm import run_norm
    temp_output = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_norm(
        input_vcf=str(test_paths["input_vcf"]),
        fasta_ref=str(test_paths["fasta_ref"]),
        output_vcf=str(temp_output),
        output_type="v",
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential params are present
    assert "rule norm:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify required inputs
    assert "input_vcf=" in content, "Missing input_vcf parameter"
    assert "fasta_ref=" in content, "Missing fasta_ref parameter"
    
    # Verify required outputs
    assert "output_vcf=" in content, "Missing output_vcf parameter"
    
    # Verify params
    assert "output_type=" in content, "Missing output_type parameter"

def test_run_norm(test_paths, tmp_path):
    """Test that norm can be run with the test files."""
    from bioinformatics_mcp.norm.mcp.run_norm import run_norm
    temp_output = tmp_path / "output.vcf"

    result = run_norm(
        input_vcf=str(test_paths["input_vcf"]),
        fasta_ref=str(test_paths["fasta_ref"]),
        output_vcf=str(temp_output),
        output_type="v"
    )

    # Verify that the run is successful
    assert result.returncode == 0, "norm tool run failed"

    # Check if output file is created
    assert temp_output.exists(), "Output VCF file was not created"