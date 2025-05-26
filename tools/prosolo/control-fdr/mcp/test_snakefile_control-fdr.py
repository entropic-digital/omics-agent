import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_vcf": test_dir / "test_input.vcf",
        "output_bcf": test_dir / "output.bcf",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_control_fdr(test_paths, tmp_path, capsys):
    """Test that control-fdr generates the expected Snakefile."""
    from tools.prosolo.control_fdr.run_control_fdr import run_control_fdr
    temp_output = tmp_path / "output.bcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_control_fdr(
        input_vcf=str(test_paths["input_vcf"]),
        output_bcf=str(temp_output),
        event_specification="some_event",
        fdr_threshold=0.05,
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential components of the generated Snakefile
    assert "rule control_fdr:" in content, "Missing rule definition in the Snakefile"
    assert "input:" in content, "Missing input section in the Snakefile"
    assert "output:" in content, "Missing output section in the Snakefile"
    assert "params:" in content, "Missing params section in the Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in the Snakefile"

    # Verify specific input parameters from meta.yaml
    assert "input_vcf=" in content, "Missing input_vcf parameter in the Snakefile"

    # Verify specific output parameters from meta.yaml
    assert "output_bcf=" in content, "Missing output_bcf parameter in the Snakefile"

    # Verify included params from run_control_fdr
    assert "event_specification=" in content, "Missing event_specification parameter in the Snakefile"
    assert "fdr_threshold=" in content, "Missing fdr_threshold parameter in the Snakefile"

def test_run_control_fdr(test_paths, tmp_path):
    """Test that control-fdr runs successfully with test input files."""
    from tools.prosolo.control_fdr.run_control_fdr import run_control_fdr
    temp_output = tmp_path / "output.bcf"

    # Run the tool with test input files
    result = run_control_fdr(
        input_vcf=str(test_paths["input_vcf"]),
        output_bcf=str(temp_output),
        event_specification="some_event",
        fdr_threshold=0.05
    )

    # Verify the process completes successfully
    assert result.returncode == 0, "control-fdr execution failed"

    # Verify the output file is created
    assert temp_output.exists(), "Output BCF file was not created"
    assert temp_output.stat().st_size > 0, "Output BCF file is empty"