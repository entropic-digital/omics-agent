import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_file": test_dir / "test_input.bam",
        "output_file": test_dir / "expected_output.bam",
        "output_index_file": test_dir / "expected_output.bai",
    }


def test_snakefile_markdup(test_paths, tmp_path, capsys):
    """Test that markdup Snakefile is generated correctly."""
    from tools.samtools.markdup.run_markdup import run_markdup

    temp_output_file = tmp_path / "output.bam"
    temp_output_index_file = tmp_path / "output.bam.bai"

    # Generate the Snakefile with print_only=True
    run_markdup(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output_file),
        output_index_file=str(temp_output_index_file),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in the Snakefile
    assert "rule markdup:" in content, "Snakefile is missing 'rule markdup' definition"
    assert "input:" in content, "Snakefile is missing 'input' section"
    assert "output:" in content, "Snakefile is missing 'output' section"
    assert "params:" in content, "Snakefile is missing 'params' section"
    assert "wrapper:" in content, "Snakefile is missing 'wrapper' section"
    assert test_paths["input_file"].name in content, "Snakefile is missing input_file"
    assert str(temp_output_file) in content, "Snakefile is missing output_file"
    assert str(temp_output_index_file) in content, (
        "Snakefile is missing output_index_file"
    )


def test_run_markdup(test_paths, tmp_path):
    """Test that markdup runs correctly with test files."""
    from tools.samtools.markdup.run_markdup import run_markdup

    temp_output_file = tmp_path / "output.bam"
    temp_output_index_file = tmp_path / "output.bam.bai"

    # Execute the markdup function
    result = run_markdup(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output_file),
        output_index_file=str(temp_output_index_file),
    )

    # Verify that the run was successful
    assert result.returncode == 0, "markdup run failed (non-zero return code)"
    assert temp_output_file.exists(), "markdup did not create the output file"
    assert temp_output_index_file.exists(), "markdup did not create the index file"
