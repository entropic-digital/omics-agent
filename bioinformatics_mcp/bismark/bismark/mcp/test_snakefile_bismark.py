import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fq": test_dir / "reads.fastq",
        "bismark_indexes_dir": test_dir / "indexes",
        "report": test_dir / "alignment_report.txt",
        "bam": test_dir / "aligned.bam",
        "expected_snakefile": test_dir / "Snakefile_expected",
    }


def test_snakefile_bismark(test_paths, tmp_path, capsys):
    """Test that bismark generates the expected Snakefile."""
    from bioinformatics_mcp.bismark.mcp.run_bismark import run_bismark
    
    temp_report = tmp_path / "alignment_report.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_bismark(
        fq=str(test_paths["fq"]),
        bismark_indexes_dir=str(test_paths["bismark_indexes_dir"]),
        report=str(temp_report),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile elements
    assert "rule bismark:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify required inputs
    assert "fq=" in content, "Missing fq input parameter"
    assert "bismark_indexes_dir=" in content, "Missing bismark_indexes_dir input parameter"

    # Verify required outputs
    assert "report=" in content, "Missing report output parameter"

    # Optionally, compare with an expected Snakefile if available
    if test_paths["expected_snakefile"].exists():
        expected_content = test_paths["expected_snakefile"].read_text()
        assert content.strip() == expected_content.strip(), "Generated Snakefile does not match expected content"


def test_run_bismark(test_paths, tmp_path):
    """Test that bismark can be run with the test files."""
    from bioinformatics_mcp.bismark.mcp.run_bismark import run_bismark

    temp_report = tmp_path / "alignment_report.txt"
    temp_bam = tmp_path / "aligned.bam"

    result = run_bismark(
        fq=str(test_paths["fq"]),
        bismark_indexes_dir=str(test_paths["bismark_indexes_dir"]),
        report=str(temp_report),
        bam=str(temp_bam),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "bismark execution failed"
    
    # Verify outputs are created
    assert temp_report.exists(), "Alignment report file was not created"
    assert temp_bam.exists(), "Aligned BAM file was not created"
