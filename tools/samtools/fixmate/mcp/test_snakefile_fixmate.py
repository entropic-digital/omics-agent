import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths for fixmate."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.bam",
        "expected_snakefile": test_dir / "expected_snakefile.smk"
    }


def test_snakefile_fixmate(test_paths, tmp_path, capsys):
    """Test that fixmate generates the expected Snakefile."""
    from tools.samtools.fixmate.run_fixmate import run_fixmate
    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_fixmate(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements in the Snakefile
    assert "rule fixmate:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f'input="{test_paths["input_file"]}"' in content, "Missing input file path"
    assert f'output="{temp_output}"' in content, "Missing output file path"
    assert "wrapper: \"file:tools/samtools/fixmate\"" in content, "Missing wrapper directive"


def test_run_fixmate(test_paths, tmp_path):
    """Test that fixmate can be executed with test files."""
    from tools.samtools.fixmate.run_fixmate import run_fixmate
    temp_output = tmp_path / "output.bam"

    # Run the fixmate tool
    result = run_fixmate(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output)
    )

    # Verify that the tool executed successfully
    assert result.returncode == 0, "Fixmate execution failed"
    assert temp_output.exists(), "Output file was not created"