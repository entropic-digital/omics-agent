import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file1": test_dir / "input1.bam",
        "bam_file2": test_dir / "input2.bam",
        "expected_snakefile": test_dir / "Snakefile",
        "output_bam": test_dir / "output.deduplicated.bam",
        "output_report": test_dir / "output.deduplication_report.txt",
    }


def test_snakefile_deduplicate_bismark(test_paths, tmp_path, capsys):
    """Test that deduplicate_bismark generates the expected Snakefile."""
    from bioinformatics_mcp.bismark.deduplicate_bismark.mcp.run_deduplicate_bismark import run_deduplicate_bismark

    run_deduplicate_bismark(
        bam_files=[str(test_paths["bam_file1"]), str(test_paths["bam_file2"])],
        output_bam=str(tmp_path / "output.deduplicated.bam"),
        output_report=str(tmp_path / "output.deduplication_report.txt"),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule deduplicate_bismark:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert str(test_paths["bam_file1"]) in content, "Missing first BAM file in inputs"
    assert str(test_paths["bam_file2"]) in content, "Missing second BAM file in inputs"
    assert str(tmp_path / "output.deduplicated.bam") in content, "Missing output BAM file in outputs"
    assert str(tmp_path / "output.deduplication_report.txt") in content, "Missing output report file in outputs"


def test_run_deduplicate_bismark(test_paths, tmp_path):
    """Test that deduplicate_bismark can be run with the test files."""
    from bioinformatics_mcp.bismark.deduplicate_bismark.mcp.run_deduplicate_bismark import run_deduplicate_bismark

    result = run_deduplicate_bismark(
        bam_files=[str(test_paths["bam_file1"]), str(test_paths["bam_file2"])],
        output_bam=str(tmp_path / "output.deduplicated.bam"),
        output_report=str(tmp_path / "output.deduplication_report.txt")
    )

    assert result.returncode == 0, "deduplicate_bismark run failed"
    assert (tmp_path / "output.deduplicated.bam").exists(), "Output BAM file not created"
    assert (tmp_path / "output.deduplication_report.txt").exists(), "Output report file not created"