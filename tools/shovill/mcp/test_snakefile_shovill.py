import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "input_reads": test_dir / "test_reads.fastq",
        "output_dir": test_dir / "output",
        "expected_snakefile": test_dir / "Snakefile",
    }

def test_snakefile_shovill(test_paths, tmp_path, capsys):
    """Test that shovill generates the expected Snakefile."""
    from tools.shovill.mcp.run_shovill import run_shovill
    temp_output_dir = tmp_path / "output"

    # Generate the Snakefile with print_only=True to capture the content
    run_shovill(
        input_reads=str(test_paths["input_reads"]),
        output_dir=str(temp_output_dir),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements in the generated Snakefile
    assert "rule shovill:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper definition in Snakefile"
    assert "input_reads=" in content, "Missing input_reads parameter in Snakefile"
    assert "output_dir=" in content, "Missing output_dir parameter in Snakefile"

def test_run_shovill(test_paths, tmp_path):
    """Test that shovill can be run with the test inputs and produces output."""
    from tools.shovill.mcp.run_shovill import run_shovill
    temp_output_dir = tmp_path / "output"

    # Run the shovill tool with test inputs
    result = run_shovill(
        input_reads=str(test_paths["input_reads"]),
        output_dir=str(temp_output_dir)
    )

    # Verify that the run was successful
    assert result.returncode == 0, "shovill run failed"
    # Verify output directory has been created
    assert temp_output_dir.exists(), "Output directory not created by shovill"
    # Verify that expected output files are present
    expected_output_file = temp_output_dir / "assembly.fasta"
    assert expected_output_file.exists(), "Expected output assembly.fasta not found in output directory"