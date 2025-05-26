import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input": test_dir / "input.fasta",
        "output": test_dir / "output.fasta",
        "log": test_dir / "vsearch.log",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_vsearch(test_paths, tmp_path, capsys):
    """Test that vsearch generates the expected Snakefile."""
    from tools.vsearch.mcp.run_vsearch import run_vsearch
    temp_output = tmp_path / "output.fasta"

    # Generate the Snakefile with print_only=True to capture the content
    run_vsearch(
        input_files=str(test_paths["input"]),
        output_files=str(temp_output),
        log=str(test_paths["log"]),
        extra="--threads 4",
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential elements in the Snakefile
    assert "rule vsearch:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "input_files=" in content, "Missing input_files parameter in Snakefile"
    assert "output_files=" in content, "Missing output_files parameter in Snakefile"
    assert "log=" in content, "Missing log parameter in Snakefile"
    assert "--threads 4" in content, "Missing extra arguments in Snakefile"


def test_run_vsearch(test_paths, tmp_path):
    """Test that vsearch can be run with the test files."""
    from tools.vsearch.mcp.run_vsearch import run_vsearch
    temp_output = tmp_path / "output.fasta"

    result = run_vsearch(
        input_files=str(test_paths["input"]),
        output_files=str(temp_output),
        log=str(test_paths["log"]),
        extra="--threads 4"
    )

    # Verify the tool execution is successful
    assert result.returncode == 0, "vsearch execution failed"
    assert temp_output.exists(), "Output file was not created"
    assert test_paths["log"].exists(), "Log file was not created"