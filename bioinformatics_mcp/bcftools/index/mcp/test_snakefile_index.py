import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_data"
    return {
        "input_file": base_dir / "input.vcf",
        "expected_output": base_dir / "expected_output.idx",
        "expected_snakefile": base_dir / "expected_Snakefile"
    }

def test_snakefile_index(test_paths, tmp_path, capsys):
    """Test that index generates the expected Snakefile."""
    from run_index import run_index

    temp_output = tmp_path / "output.idx"

    run_index(
        input_file=str(test_paths["input_file"]),
        output=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile elements
    assert "rule index:" in content, "Snakefile is missing rule definition"
    assert "input:" in content, "Snakefile is missing input section"
    assert "output:" in content, "Snakefile is missing output section"
    assert "wrapper:" in content, "Snakefile is missing wrapper reference"
    assert test_paths["input_file"].name in content, "Input file is not included in Snakefile"
    assert str(temp_output) in content, "Output file is not included in Snakefile"
    assert "file:tools/bcftools/index" in content, "Snakefile is missing correct wrapper path"

def test_run_index(test_paths, tmp_path):
    """Test that the index tool executes correctly."""
    from run_index import run_index

    temp_output = tmp_path / "output.idx"

    result = run_index(
        input_file=str(test_paths["input_file"]),
        output=str(temp_output)
    )

    # Verify tool execution
    assert result.returncode == 0, "index run failed"
    assert temp_output.exists(), "Output file was not generated"
    assert temp_output.stat().st_size > 0, "Output file is empty"