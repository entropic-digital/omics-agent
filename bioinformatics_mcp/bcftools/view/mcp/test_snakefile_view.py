import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths for the bcftools view tool."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "vcf_bcf_file": test_dir / "test_input.vcf",
        "output_file": test_dir / "expected_output.bcf",
    }

def test_snakefile_view_bcftools(test_paths, tmp_path, capsys):
    """Test that the bcftools view tool generates the expected Snakefile."""
    from run_view import run_view
    temp_output = tmp_path / "output.bcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_view(
        vcf_bcf_file=str(test_paths["vcf_bcf_file"]),
        output_file=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the Snakefile
    assert "rule view:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "vcf_bcf_file=" in content, "Missing vcf_bcf_file input parameter"
    assert "output_file=" in content, "Missing output_file output parameter"

def test_run_view_bcftools(test_paths, tmp_path):
    """Test that the bcftools view tool can be run with test inputs."""
    from run_view import run_view
    temp_output = tmp_path / "output.bcf"

    # Run the tool with test inputs
    result = run_view(
        vcf_bcf_file=str(test_paths["vcf_bcf_file"]),
        output_file=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "bcftools view run failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"