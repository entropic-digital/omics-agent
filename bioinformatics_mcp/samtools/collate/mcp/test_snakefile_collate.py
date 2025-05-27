"""Module that tests if the collate Snakefile is rendered and runnable"""

import pytest
from pathlib import Path
from bioinformatics_mcp.samtools.collate.run_collate import run_collate


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.bam",
        "expected_output": test_dir / "expected_output.bam",
        "non_existent_input": test_dir / "non_existent.bam",
    }


def test_snakefile_collate(test_paths, tmp_path, capsys):
    """Test that the collate Snakefile is generated as expected."""
    temporary_output = tmp_path / "output.bam"

    # Generate Snakefile with print_only=True
    run_collate(
        input_file=str(test_paths["input_file"]),
        output_file=str(temporary_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    snakefile_content = captured.out

    # Verify essential elements in the generated Snakefile
    assert "rule collate:" in snakefile_content, "Missing rule definition"
    assert "input:" in snakefile_content, "Missing input section"
    assert "output:" in snakefile_content, "Missing output section"
    assert "wrapper:" in snakefile_content, "Missing wrapper section"
    assert str(test_paths["input_file"]) in snakefile_content, "Input file not included"
    assert str(temporary_output) in snakefile_content, "Output file not included"


def test_run_collate_with_valid_inputs(test_paths, tmp_path):
    """Test that collate runs successfully with valid inputs."""
    temporary_output = tmp_path / "output.bam"

    result = run_collate(
        input_file=str(test_paths["input_file"]),
        output_file=str(temporary_output),
    )

    # Verify the process executed successfully
    assert result.returncode == 0, "Tool execution failed"
    assert temporary_output.exists(), "Output file not created"


def test_run_collate_with_invalid_input(test_paths, tmp_path):
    """Test that collate fails gracefully with invalid input."""
    temporary_output = tmp_path / "output.bam"

    with pytest.raises(Exception, match="No such file or directory"):
        run_collate(
            input_file=str(test_paths["non_existent_input"]),
            output_file=str(temporary_output),
        )
