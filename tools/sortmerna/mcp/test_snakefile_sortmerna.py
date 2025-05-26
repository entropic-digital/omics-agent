import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reference_file": test_dir / "reference.fa",
        "query_file": test_dir / "query.fa",
        "aligned_reads": test_dir / "aligned_reads.fq",
        "unaligned_reads": test_dir / "unaligned_reads.fq",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_sortmerna(test_paths, tmp_path, capsys):
    """Test that sortmerna generates the expected Snakefile."""
    from tools.sortmerna.mcp.run_sortmerna import run_sortmerna

    temp_aligned = tmp_path / "aligned_reads.fq"
    temp_unaligned = tmp_path / "unaligned_reads.fq"

    run_sortmerna(
        reference_files=[str(test_paths["reference_file"])],
        query_file=str(test_paths["query_file"]),
        aligned_reads=str(temp_aligned),
        unaligned_reads=str(temp_unaligned),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule sortmerna:" in content, "Missing rule definition."
    assert "input:" in content, "Missing input section."
    assert "output:" in content, "Missing output section."
    assert "wrapper:" in content, "Missing wrapper section."
    assert "reference_files=" in content, "Missing 'reference_files' parameter."
    assert "query_file=" in content, "Missing 'query_file' parameter."
    assert "aligned_reads=" in content, "Missing 'aligned_reads' parameter."
    assert "unaligned_reads=" in content, "Missing 'unaligned_reads' parameter."


def test_run_sortmerna(test_paths, tmp_path):
    """Test that sortmerna can be run with the test files."""
    from tools.sortmerna.mcp.run_sortmerna import run_sortmerna

    temp_aligned = tmp_path / "aligned_reads.fq"
    temp_unaligned = tmp_path / "unaligned_reads.fq"

    result = run_sortmerna(
        reference_files=[str(test_paths["reference_file"])],
        query_file=str(test_paths["query_file"]),
        aligned_reads=str(temp_aligned),
        unaligned_reads=str(temp_unaligned),
    )

    assert result.returncode == 0, "SortMeRNA execution failed."
    assert temp_aligned.exists(), "Aligned reads file was not created."
    assert temp_unaligned.exists(), "Unaligned reads file was not created."