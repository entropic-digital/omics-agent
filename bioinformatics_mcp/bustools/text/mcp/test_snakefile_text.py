import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file1": test_dir / "input1.bus",
        "input_file2": test_dir / "input2.bus",
        "expected_snakefile": test_dir / "Snakefile",
        "output_file": test_dir / "output.tsv",
    }


def test_snakefile_text(test_paths, tmp_path, capsys):
    """Test that text generates the expected Snakefile."""
    from bioinformatics_mcp.bustools.text.run_text import run_text

    temp_output = tmp_path / "output.tsv"

    run_text(
        input_files=[str(test_paths["input_file1"]), str(test_paths["input_file2"])],
        output_file=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule text:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f"'{test_paths['input_file1']}'" in content, (
        "Missing input file1 in Snakefile input"
    )
    assert f"'{test_paths['input_file2']}'" in content, (
        "Missing input file2 in Snakefile input"
    )
    assert f"'{temp_output}'" in content, "Missing output file in Snakefile output"


def test_run_text(test_paths, tmp_path):
    """Test that the text tool runs successfully with test files."""
    from bioinformatics_mcp.bustools.text.run_text import run_text

    temp_output = tmp_path / "output.tsv"

    result = run_text(
        input_files=[str(test_paths["input_file1"]), str(test_paths["input_file2"])],
        output_file=str(temp_output),
    )

    assert result.returncode == 0, "Text tool execution failed"
    assert temp_output.exists(), "Output file was not created"
