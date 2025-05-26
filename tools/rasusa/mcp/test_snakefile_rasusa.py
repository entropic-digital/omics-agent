import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_reads": test_dir / "test_reads.fq",
        "expected_snakefile": test_dir / "expected_snakefile.smk",
    }


def test_snakefile_rasusa(test_paths, tmp_path, capsys):
    """Test that rasusa Snakefile is properly generated."""
    from tools.rasusa.mcp.run_rasusa import run_rasusa

    temp_output = tmp_path / "output_reads.fq"

    # Generate the Snakefile with print_only=True
    run_rasusa(
        input_reads=str(test_paths["input_reads"]),
        output_reads=str(temp_output),
        coverage="30x",
        genome_size="4.5Mb",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Check for essential Snakefile elements
    assert "rule rasusa:" in content, "Snakefile does not define the rasusa rule"
    assert "input:" in content, "Snakefile is missing the input section"
    assert "output:" in content, "Snakefile is missing the output section"
    assert "params:" in content, "Snakefile is missing the params section"
    assert "wrapper:" in content, "Snakefile is missing the wrapper section"

    # Verify the presence of required inputs, outputs, and parameters
    assert "input_reads=" in content, "Snakefile is missing the input_reads parameter"
    assert "output_reads=" in content, "Snakefile is missing the output_reads parameter"
    assert "coverage=" in content, "Snakefile is missing the coverage parameter"
    assert "genome_size=" in content, "Snakefile is missing the genome_size parameter"
    assert 'wrapper = "file:tools/rasusa"' in content, (
        "Snakefile has incorrect or missing wrapper"
    )

    # Optionally, verify that generated Snakefile matches an expected version
    expected_snakefile_content = test_paths["expected_snakefile"].read_text()
    assert content == expected_snakefile_content, (
        "Generated Snakefile does not match the expected content"
    )


def test_run_rasusa(test_paths, tmp_path):
    """Test that rasusa runs successfully with test files."""
    from tools.rasusa.mcp.run_rasusa import run_rasusa

    temp_output = tmp_path / "subsampled_reads.fq"

    # Run rasusa tool
    result = run_rasusa(
        input_reads=str(test_paths["input_reads"]),
        output_reads=str(temp_output),
        coverage="30x",
        genome_size="4.5Mb",
    )

    # Verify successful execution
    assert result.returncode == 0, "rasusa run failed with non-zero exit code"

    # Assert output file is created and has content
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"
