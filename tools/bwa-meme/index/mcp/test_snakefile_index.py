import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fasta_file": test_dir / "test.fasta",
        "output_directory": test_dir / "output",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_index(test_paths, tmp_path, capsys):
    """Test that the index tool generates the expected Snakefile."""
    from tools.index.mcp.run_index import run_index

    run_index(
        fasta_file=str(test_paths["fasta_file"]),
        output_directory=str(tmp_path),
        prefix="test_prefix",
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule index:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper declaration in Snakefile"

    assert "fasta_file=" in content, "Missing 'fasta_file' input parameter"
    assert "output_directory=" in content, "Missing 'output_directory' output parameter"

    assert "prefix" in content, "Missing 'prefix' optional parameter"


def test_run_index(test_paths, tmp_path):
    """Test that the index tool runs successfully with test data."""
    from tools.index.mcp.run_index import run_index

    output_dir = tmp_path / "index_output"
    output_dir.mkdir()

    result = run_index(
        fasta_file=str(test_paths["fasta_file"]),
        output_directory=str(output_dir),
        prefix="test_prefix"
    )

    assert result.returncode == 0, "The tool execution failed unexpectedly"
    assert (output_dir / "test_prefix.bwt").exists(), "Missing expected output file: test_prefix.bwt"
    assert (output_dir / "test_prefix.sa").exists(), "Missing expected output file: test_prefix.sa"
    assert (output_dir / "test_prefix.ann").exists(), "Missing expected output file: test_prefix.ann"