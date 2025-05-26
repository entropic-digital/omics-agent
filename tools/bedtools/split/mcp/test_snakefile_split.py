import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bed": test_dir / "test_input.bed",
        "expected_snakefile": test_dir / "expected_snakefile",
        "output_dir": test_dir / "output",
    }


def test_snakefile_split(test_paths, tmp_path, capsys):
    """Test that split generates the expected Snakefile."""
    from tools.bedtools.split.run_split import run_split

    temp_output = tmp_path / "output"
    temp_output.mkdir()

    # Generate the Snakefile with print_only=True to capture its content
    run_split(
        bed=str(test_paths["input_bed"]), output=str(temp_output), print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify that the Snakefile contains all essential components
    assert "rule split:" in content, "Missing rule definition for 'split'"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "bed=" in content, "Missing required 'bed' input parameter"

    # Verify that the wrapper points to the correct tool path
    assert 'wrapper: "file:tools/bedtools/split"' in content, (
        "Incorrect or missing wrapper path in Snakefile"
    )


def test_run_split(test_paths, tmp_path):
    """Test that the split tool can be executed successfully."""
    from tools.bedtools.split.run_split import run_split

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    # Run the split tool
    result = run_split(bed=str(test_paths["input_bed"]), output=str(output_dir))

    # Verify that the process completed successfully
    assert result.returncode == 0, "split tool execution failed"
    assert output_dir.exists(), "Output directory was not created"
    assert any(output_dir.iterdir()), "No output files were generated"

    # Further assertions can verify content and structure of output files
