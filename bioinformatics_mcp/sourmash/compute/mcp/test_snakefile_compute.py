import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_data"
    return {
        "input_file": base_dir / "input.fasta",
        "output_signature": base_dir / "output.sig",
        "expected_snakefile": base_dir / "Snakefile"
    }


def test_snakefile_compute(test_paths, tmp_path, capsys):
    """Test that sourmash_compute generates the expected Snakefile."""
    from bioinformatics_mcp.sourmash.compute.run_compute import run_compute
    temp_output = tmp_path / "output.sig"

    # Generate the Snakefile with print_only=True to capture the content
    run_compute(
        input_file=str(test_paths["input_file"]),
        output_signature=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential sections are present in the Snakefile
    assert "rule compute:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify all required input and output parameters from meta.yaml
    assert "input_file=" in content, "Missing input_file parameter in Snakefile"
    assert "output_signature=" in content, "Missing output_signature parameter in Snakefile"


def test_run_compute(test_paths, tmp_path):
    """Test that sourmash_compute executes successfully."""
    from bioinformatics_mcp.sourmash.compute.run_compute import run_compute
    temp_output = tmp_path / "output.sig"

    # Run the tool with required inputs and outputs
    result = run_compute(
        input_file=str(test_paths["input_file"]),
        output_signature=str(temp_output)
    )

    # Assert the process executed successfully
    assert result.returncode == 0, "sourmash_compute execution failed"

    # Verify that the output file was created
    assert temp_output.exists(), "Output signature file was not created"

    # Add further output validation if needed (e.g., checking file content)