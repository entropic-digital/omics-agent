import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_file": test_dir / "input_file.gz",
        "expected_index": test_dir / "expected_file.tbi",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_index(test_paths, tmp_path, capsys):
    """Test that run_index generates the expected Snakefile."""
    from run_index import run_index

    temp_output = tmp_path / "output.tbi"

    run_index(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule index:" in content, "Missing 'index' rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "input_file=" in content, "Missing 'input_file' parameter in Snakefile"
    assert "output_file=" in content, "Missing 'output_file' parameter in Snakefile"


def test_run_index(test_paths, tmp_path):
    """Test that run_index executes successfully with test files."""
    from run_index import run_index

    temp_output = tmp_path / "output.tbi"

    result = run_index(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output)
    )

    assert result.returncode == 0, "Tabix index creation failed"
    assert temp_output.exists(), "Output index file was not created"
