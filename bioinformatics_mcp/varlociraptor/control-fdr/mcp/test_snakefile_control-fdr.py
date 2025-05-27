import pytest
from pathlib import Path
from bioinformatics_mcp.varlociraptor.control_fdr.run_control_fdr import run_control_fdr

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "input.vcf",
        "expected_output": test_dir / "expected_output.vcf",
        "expected_snakefile": test_dir / "expected_snakefile"
    }

def test_snakefile_control_fdr(test_paths, tmp_path, capsys):
    """Test that control_fdr generates the expected Snakefile."""
    temp_output = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_control_fdr(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        fdr=0.05,
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule control_fdr:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "input_file=" in content, "Missing input_file parameter"
    assert "output_file=" in content, "Missing output_file parameter"

def test_run_control_fdr(test_paths, tmp_path):
    """Test that control_fdr can be run with the test files."""
    temp_output = tmp_path / "output.vcf"

    result = run_control_fdr(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        fdr=0.05
    )

    # Verify that the run is successful
    assert result.returncode == 0, "control_fdr run failed"

    # Check if the output file is created
    assert temp_output.exists(), "Output file was not created"
