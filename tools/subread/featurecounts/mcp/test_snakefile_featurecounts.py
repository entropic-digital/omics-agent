import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "sam_or_bam_files": [test_dir / "test1.bam", test_dir / "test2.bam"],
        "annotation_file": test_dir / "test_annotation.gtf",
        "output_counts_file": test_dir / "output_counts.txt",
        "output_summary_file": test_dir / "output_summary.txt",
        "output_junction_file": test_dir / "output_junction.txt",
    }


def test_snakefile_featurecounts(test_paths, tmp_path, capsys):
    """Test that featurecounts generates the expected Snakefile."""
    from tools.featurecounts.mcp.run_featurecounts import run_featurecounts

    run_featurecounts(
        sam_or_bam_files=[str(f) for f in test_paths["sam_or_bam_files"]],
        annotation_file=str(test_paths["annotation_file"]),
        output_counts_file=str(tmp_path / "output_counts.txt"),
        output_summary_file=str(tmp_path / "output_summary.txt"),
        output_junction_file=str(tmp_path / "output_junction.txt"),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule featurecounts:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "sam_or_bam_files=" in content, "Missing sam_or_bam_files parameter"
    assert "annotation_file=" in content, "Missing annotation_file parameter"
    assert "output_counts_file=" in content, "Missing output_counts_file parameter"
    assert "output_summary_file=" in content, "Missing output_summary_file parameter"
    assert "output_junction_file=" in content, "Missing output_junction_file parameter"


def test_run_featurecounts(test_paths, tmp_path):
    """Test that featurecounts can be run with the test files."""
    from tools.featurecounts.mcp.run_featurecounts import run_featurecounts

    temp_counts = tmp_path / "output_counts.txt"
    temp_summary = tmp_path / "output_summary.txt"
    temp_junction = tmp_path / "output_junction.txt"

    result = run_featurecounts(
        sam_or_bam_files=[str(f) for f in test_paths["sam_or_bam_files"]],
        annotation_file=str(test_paths["annotation_file"]),
        output_counts_file=str(temp_counts),
        output_summary_file=str(temp_summary),
        output_junction_file=str(temp_junction),
    )

    assert result.returncode == 0, "featurecounts run failed"
    assert temp_counts.exists(), "Output counts file was not created"
    assert temp_summary.exists(), "Output summary file was not created"
    assert temp_junction.exists(), "Output junction file was not created"