import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "input.bam",
        "expected_metrics": test_dir / "output.metrics",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_collectalignmentsummarymetrics(test_paths, tmp_path, capsys):
    """Test that collectalignmentsummarymetrics generates the expected Snakefile."""
    from tools.picard.collectalignmentsummarymetrics.mcp.run_collectalignmentsummarymetrics import run_collectalignmentsummarymetrics
    temp_output = tmp_path / "output.metrics"

    run_collectalignmentsummarymetrics(
        input=str(test_paths["input_bam"]),
        output=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule collectalignmentsummarymetrics:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"'{test_paths['input_bam']}'" in content, "Missing input BAM file"
    assert f"'{temp_output}'" in content, "Missing output metrics file"


def test_run_collectalignmentsummarymetrics(test_paths, tmp_path):
    """Test that collectalignmentsummarymetrics can be run with the test files."""
    from tools.picard.collectalignmentsummarymetrics.mcp.run_collectalignmentsummarymetrics import run_collectalignmentsummarymetrics
    temp_output = tmp_path / "output.metrics"

    result = run_collectalignmentsummarymetrics(
        input=str(test_paths["input_bam"]),
        output=str(temp_output)
    )

    assert result.returncode == 0, "collectalignmentsummarymetrics run failed"
    assert temp_output.exists(), "Output metrics file was not created"