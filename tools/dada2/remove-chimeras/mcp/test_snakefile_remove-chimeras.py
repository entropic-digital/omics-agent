import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_rds": test_dir / "input_sequence_table.rds",
        "expected_output_rds": test_dir / "chimera_free_sequence_table.rds",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_remove_chimeras(test_paths, tmp_path, capsys):
    """Test that remove-chimeras generates the expected Snakefile."""
    from tools.dada2.remove_chimeras.run_remove_chimeras import run_remove_chimeras
    temp_output_rds = tmp_path / "chimera_free_output.rds"

    # Generate the Snakefile with print_only=True to capture the content
    run_remove_chimeras(
        input_rds=str(test_paths["input_rds"]),
        output_rds=str(temp_output_rds),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule remove_chimeras:" in content, "Missing rule definition for remove_chimeras"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert '"input_rds"' in content, "Missing input_rds parameter in Snakefile"
    assert '"output_rds"' in content, "Missing output_rds parameter in Snakefile"
    assert "tools/dada2/remove-chimeras" in content, "Missing correct wrapper path in Snakefile"


def test_run_remove_chimeras(test_paths, tmp_path):
    """Test that remove-chimeras can be run with the test files."""
    from tools.dada2.remove_chimeras.run_remove_chimeras import run_remove_chimeras
    temp_output_rds = tmp_path / "chimera_free_output.rds"

    # Run the remove-chimeras tool
    result = run_remove_chimeras(
        input_rds=str(test_paths["input_rds"]),
        output_rds=str(temp_output_rds)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "remove-chimeras tool execution failed"
    assert temp_output_rds.exists(), "Expected output RDS file was not created"
    # Additional verification can be done here if specific output content checks are available