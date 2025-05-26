import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_bam": test_dir / "test_input.bam",
        "expected_output_bam": test_dir / "expected_output.bam",
    }


def test_snakefile_view(test_paths, tmp_path, capsys):
    """Test that the Sambamba view Snakefile is correctly generated."""
    from tools.sambamba.view.run_view import run_view

    temp_output = tmp_path / "output.bam"

    run_view(
        input_file=str(test_paths["input_bam"]),
        output_file=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    snakefile_content = captured.out

    assert "rule view:" in snakefile_content, "Snakefile missing rule 'view'"
    assert "input:" in snakefile_content, "Snakefile missing 'input' section"
    assert "output:" in snakefile_content, "Snakefile missing 'output' section"
    assert "wrapper:" in snakefile_content, "Snakefile missing 'wrapper' section"
    assert "input_file=" in snakefile_content, "Snakefile missing 'input_file' parameter"
    assert "output_file=" in snakefile_content, "Snakefile missing 'output_file' parameter"
    assert "tools/sambamba/view" in snakefile_content, "Snakefile missing Sambamba view wrapper path"


def test_run_view_execution(test_paths, tmp_path):
    """Test the actual execution of the Sambamba view tool."""
    from tools.sambamba.view.run_view import run_view

    temp_output = tmp_path / "output.bam"

    result = run_view(
        input_file=str(test_paths["input_bam"]),
        output_file=str(temp_output),
    )

    assert result.returncode == 0, "Sambamba view tool execution failed"
    assert temp_output.exists(), "Expected output file not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"