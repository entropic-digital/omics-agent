import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.fastq",
        "expected_output": test_dir / "expected_output.txt",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_profiler_illumina(test_paths, tmp_path, capsys):
    """Test that profiler_illumina generates the expected Snakefile."""
    from tools.profiler_illumina.mcp.run_profiler_illumina import run_profiler_illumina
    temp_output = tmp_path / "output.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_profiler_illumina(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule profiler_illumina:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Verify inputs
    assert f"input_file='{test_paths['input_file']}'" in content, "Missing input_file parameter"
    # Verify outputs
    assert f"output_file='{temp_output}'" in content, "Missing output_file parameter"


def test_run_profiler_illumina(test_paths, tmp_path):
    """Test that profiler_illumina can be executed with the test files."""
    from tools.profiler_illumina.mcp.run_profiler_illumina import run_profiler_illumina
    temp_output = tmp_path / "output.txt"

    result = run_profiler_illumina(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "profiler_illumina run failed"
    # Verify output file is created
    assert temp_output.exists(), "Output file was not created"
    # Optional: Compare output to expected result (if available)
    if test_paths["expected_output"].exists():
        assert temp_output.read_text() == test_paths["expected_output"].read_text(), "Output file content does not match expected"