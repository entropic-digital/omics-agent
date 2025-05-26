import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "input_file": test_dir / "input.bed",
        "genome_file": test_dir / "genome.txt",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_slop(test_paths, tmp_path, capsys):
    """Test that slop generates the expected Snakefile."""
    from tools.slop.run_slop import run_slop
    temp_output = tmp_path / "output.bed"

    # Generate Snakefile with print_only=True
    run_slop(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        genome=str(test_paths["genome_file"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential elements of the Snakefile
    assert "rule slop:" in content, "Snakefile missing 'slop' rule definition"
    assert "input:" in content, "Snakefile missing input section"
    assert "output:" in content, "Snakefile missing output section"
    assert "params:" in content, "Snakefile missing params section"
    assert "wrapper:" in content, "Snakefile missing wrapper section"
    assert "input_file=" in content, "Snakefile missing input_file parameter"
    assert "genome=" in content, "Snakefile missing genome parameter"
    assert "output_file=" in content, "Snakefile missing output_file"


def test_run_slop(test_paths, tmp_path):
    """Test that slop correctly processes test files."""
    from tools.slop.run_slop import run_slop
    temp_output = tmp_path / "output.bed"

    # Run the slop tool
    result = run_slop(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        genome=str(test_paths["genome_file"]),
    )

    # Verify successful run
    assert result.returncode == 0, "slop tool execution failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"