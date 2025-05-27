import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.vcf",
        "expected_snakefile": test_dir / "expected_snakefile",
        "output_dir": test_dir / "output_dir"
    }


def test_snakefile_module_opencravat(test_paths, tmp_path, capsys):
    """Test that OpenCRAVAT module generates the expected Snakefile."""
    from bioinformatics_mcp.open_cravat.run_module import run_module

    # Generate the Snakefile with print_only=True
    run_module(
        input_file=str(test_paths["input_file"]),
        output_dir=str(tmp_path),
        module_name="some_module",
        reference_genome="hg38",
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements
    assert "rule module:" in content, "Missing rule definition section"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "input_file=" in content, "Missing input_file parameter"
    assert "output_dir=" in content, "Missing output_dir parameter"
    assert "module_name=" in content, "Missing module_name parameter"
    assert "reference_genome=" in content, "Missing reference_genome parameter"


def test_run_module_opencravat(test_paths, tmp_path):
    """Test that OpenCRAVAT module can be executed correctly with test files."""
    from bioinformatics_mcp.open_cravat.run_module import run_module

    temp_output_dir = tmp_path / "output_dir"
    temp_output_dir.mkdir()

    # Run the module
    result = run_module(
        input_file=str(test_paths["input_file"]),
        output_dir=str(temp_output_dir),
        module_name="some_module",
        reference_genome="hg38"
    )

    # Verify the process completes successfully
    assert result.returncode == 0, "OpenCRAVAT module execution failed"

    # Verify output files or directory were created
    assert temp_output_dir.exists(), "Output directory was not created"
    # You can add more output file checks as needed
