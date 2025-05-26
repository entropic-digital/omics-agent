import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_files": (test_dir / "test1.fastq", test_dir / "test2.fastq"),
        "expected_snakefile": test_dir / "expected_Snakefile",
        "output_file": test_dir / "merged_output.fastq"
    }


def test_snakefile_pear(test_paths, tmp_path, capsys):
    """Test that pear generates the expected Snakefile."""
    from tools.pear.mcp.run_pear import run_pear
    temp_output = tmp_path / "merged_output.fastq"

    # Generate the Snakefile with print_only=True to capture the content
    run_pear(
        input_files=(str(test_paths["input_files"][0]), str(test_paths["input_files"][1])),
        output_file=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule pear:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "input_files=" in content, "Missing input_files parameter"
    assert "output_file=" in content, "Missing output_file parameter"
    assert "file:tools/pear" in content, "Missing wrapper path"


def test_run_pear(test_paths, tmp_path):
    """Test that pear can be run with the test files."""
    from tools.pear.mcp.run_pear import run_pear
    temp_output = tmp_path / "merged_output.fastq"

    result = run_pear(
        input_files=(str(test_paths["input_files"][0]), str(test_paths["input_files"][1])),
        output_file=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "pear run failed"
    # Verify output file is created
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"