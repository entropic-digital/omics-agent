import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.bam",
        "index_file": test_dir / "test_input.bam.bai",
        "output_file": test_dir / "test_output.idxstats",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_idxstats(test_paths, tmp_path, capsys):
    """Test that the idxstats tool generates the expected Snakefile."""
    from bioinformatics_mcp.samtools.idxstats.mcp.run_idxstats import run_idxstats

    temp_output = tmp_path / "output.idxstats"

    # Generate the Snakefile with print_only=True to capture the content
    run_idxstats(
        input_file=str(test_paths["input_file"]),
        index_file=str(test_paths["index_file"]),
        output_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential parameters and structure are in the Snakefile
    assert "rule idxstats:" in content, "Missing 'rule idxstats:' in Snakefile"
    assert "input:" in content, "Missing 'input:' section in Snakefile"
    assert "output:" in content, "Missing 'output:' section in Snakefile"
    assert "wrapper:" in content, "Missing 'wrapper:' section in Snakefile"
    assert "input_file=" in content, "Missing 'input_file' parameter in rule inputs"
    assert "index_file=" in content, "Missing 'index_file' parameter in rule inputs"
    assert "output_file=" in content, "Missing 'output_file' parameter in rule outputs"


def test_run_idxstats(test_paths, tmp_path):
    """Test that the idxstats tool runs correctly with test files."""
    from bioinformatics_mcp.samtools.idxstats.mcp.run_idxstats import run_idxstats

    temp_output = tmp_path / "output.idxstats"

    # Run the tool with test files
    result = run_idxstats(
        input_file=str(test_paths["input_file"]),
        index_file=str(test_paths["index_file"]),
        output_file=str(temp_output),
    )

    # Verify that the tool execution is successful
    assert result.returncode == 0, "idxstats tool execution failed"

    # Verify the expected output file is created
    assert temp_output.exists(), "Output idxstats file was not created"
    assert temp_output.stat().st_size > 0, "Output idxstats file is empty"