import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_file": test_dir / "input.sam",
        "region": "chr1:100-2000",
        "output_file": test_dir / "output.bam",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_view_generation(test_paths, tmp_path, capsys):
    """Test that the view tool generates the expected Snakefile."""
    from tools.samtools.view.run_view import run_view

    temp_output = tmp_path / "output.bam"

    run_view(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        region=test_paths["region"],
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule view:" in content, "Snakefile missing rule definition."
    assert "input:" in content, "Snakefile missing input section."
    assert "output:" in content, "Snakefile missing output section."
    assert "params:" in content, "Snakefile missing params section."
    assert "wrapper:" in content, "Snakefile missing wrapper section."
    assert "input_file=" in content, "Snakefile missing input_file parameter."
    assert "output_file=" in content, "Snakefile missing output_file parameter."
    assert "region=" in content, "Snakefile missing region parameter."
    assert "write_index" in content, "Snakefile missing write_index parameter."


def test_run_view_execution(test_paths, tmp_path):
    """Test that the view tool runs successfully with given inputs."""
    from tools.samtools.view.run_view import run_view

    temp_output = tmp_path / "output.bam"
    result = run_view(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        region=test_paths["region"]
    )

    assert result.returncode == 0, "view tool execution failed."
    assert temp_output.exists(), "Output file not generated."
