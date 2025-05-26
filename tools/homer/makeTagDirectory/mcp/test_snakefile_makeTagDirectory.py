import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "test.bam",
        "expected_snakefile": test_dir / "Snakefile",
        "output_directory": test_dir / "output_tag_directory"
    }


def test_snakefile_makeTagDirectory(test_paths, tmp_path, capsys):
    """Test that makeTagDirectory generates the expected Snakefile."""
    from tools.homer.makeTagDirectory.run_makeTagDirectory import run_makeTagDirectory

    # Use a temporary output path for testing
    temp_output = tmp_path / "output_dir"

    # Generate the Snakefile with print_only=True to capture the content
    run_makeTagDirectory(
        input_bam=str(test_paths["input_bam"]),
        output_directory=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the generated Snakefile
    assert "rule makeTagDirectory:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"input_bam='{str(test_paths['input_bam'])}'" in content, "Missing or incorrect input BAM parameter"
    assert f"output_directory='{str(temp_output)}'" in content, "Missing or incorrect output directory parameter"


def test_run_makeTagDirectory(test_paths, tmp_path):
    """Test that makeTagDirectory can be run with the test files."""
    from tools.homer.makeTagDirectory.run_makeTagDirectory import run_makeTagDirectory

    # Use a temporary output directory for testing
    temp_output = tmp_path / "output_tag_directory"

    # Run the makeTagDirectory tool with the test files
    result = run_makeTagDirectory(
        input_bam=str(test_paths["input_bam"]),
        output_directory=str(temp_output)
    )

    # Verify that the tool executed successfully
    assert result.returncode == 0, "makeTagDirectory execution failed"

    # Verify that the output directory was created
    assert temp_output.exists(), "Output tag directory was not created"