import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.sam",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_cleansam(test_paths, tmp_path, capsys):
    """Test that the cleansam Snakefile is correctly generated."""
    from bioinformatics_mcp.gatk.cleansam.run_cleansam import run_cleansam
    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True
    run_cleansam(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify that the Snakefile contains essential rule components
    assert "rule cleansam:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert '"input": ' in content, "Missing input parameter in Snakefile"
    assert str(test_paths["input_file"]) in content, "Input file path is missing in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert '"output": ' in content, "Missing output parameter in Snakefile"
    assert str(temp_output) in content, "Output file path is missing in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "file:tools/gatk/cleansam" in content, "Wrapper path is incorrect or missing"


def test_run_cleansam(test_paths, tmp_path):
    """Test running the cleansam tool with test files."""
    from bioinformatics_mcp.gatk.cleansam.run_cleansam import run_cleansam
    temp_output = tmp_path / "output.bam"

    # Execute the runsnake_wrapper call
    result = run_cleansam(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
    )

    # Verify the process completed successfully
    assert result.returncode == 0, "cleansam execution process failed"
    assert temp_output.exists(), "Output file was not created after cleansam execution"