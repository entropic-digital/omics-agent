import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_fastq": test_dir / "input.fastq",
        "expected_output_rds": test_dir / "output.rds",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_dereplicate_fastq(test_paths, tmp_path, capsys):
    """Test that dereplicate-fastq generates the expected Snakefile."""
    from bioinformatics_mcp.dada2.dereplicate_fastq.run_dereplicate_fastq import run_dereplicate_fastq
    temp_output_rds = tmp_path / "output.rds"

    # Generate the Snakefile with print_only=True to capture the content
    run_dereplicate_fastq(
        input_fastq=str(test_paths["input_fastq"]),
        output_rds=str(temp_output_rds),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule dereplicate_fastq:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    # Add assertions for all required input parameters
    assert f"'{test_paths['input_fastq']}'" in content, "Missing input_fastq parameter in Snakefile"
    # Add assertions for all required output parameters
    assert f"'{temp_output_rds}'" in content, "Missing output_rds parameter in Snakefile"

def test_run_dereplicate_fastq(test_paths, tmp_path):
    """Test that dereplicate-fastq can be run with the test files."""
    from bioinformatics_mcp.dada2.dereplicate_fastq.run_dereplicate_fastq import run_dereplicate_fastq
    temp_output_rds = tmp_path / "output.rds"

    result = run_dereplicate_fastq(
        input_fastq=str(test_paths["input_fastq"]),
        output_rds=str(temp_output_rds)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "dereplicate-fastq run failed"
    # Verify that the expected output file was generated
    assert temp_output_rds.exists(), "Output RDS file not generated"