import pytest
from pathlib import Path
import subprocess


@pytest.fixture
def test_paths():
    """Set up test file paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_fastq": test_dir / "test_input.fastq.gz",
        "output_txt": test_dir / "test_output.txt",
        "output_png": test_dir / "test_output.png",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_fastq_screen(test_paths, tmp_path, capsys):
    """Test that fastq_screen generates the expected Snakefile."""
    from bioinformatics_mcp.fastq_screen.mcp.run_fastq_screen import run_fastq_screen

    run_fastq_screen(
        input_fastq=str(test_paths["input_fastq"]),
        output_txt=str(test_paths["output_txt"]),
        output_png=str(test_paths["output_png"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assertions for essential Snakefile elements
    assert "rule fastq_screen:" in content, "Missing 'fastq_screen' rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify required input fields
    assert "input_fastq" in content, "Missing 'input_fastq' parameter"

    # Verify required output fields
    assert "output_txt" in content, "Missing 'output_txt' parameter"
    assert "output_png" in content, "Missing 'output_png' parameter"

    # Verify additional parameters
    assert "fastq_screen_config" in content, "Missing 'fastq_screen_config' parameter"
    assert "aligner" in content, "Missing 'aligner' parameter"
    assert "subset" in content, "Missing 'subset' parameter"


def test_run_fastq_screen(test_paths, tmp_path):
    """Test that fastq_screen can be run with the test files."""
    from bioinformatics_mcp.fastq_screen.mcp.run_fastq_screen import run_fastq_screen

    temp_output_txt = tmp_path / "test_output.txt"
    temp_output_png = tmp_path / "test_output.png"

    result = run_fastq_screen(
        input_fastq=str(test_paths["input_fastq"]),
        output_txt=str(temp_output_txt),
        output_png=str(temp_output_png),
    )

    # Verify the tool runs successfully
    assert result.returncode == 0, "fastq_screen execution failed"

    # Verify the expected output files are created
    assert temp_output_txt.exists(), "Output TXT file was not created"
    assert temp_output_png.exists(), "Output PNG file was not created"
