import pytest
from pathlib import Path
from bioinformatics_mcp.collecthsmetrics.mcp.run_collecthsmetrics import run_collecthsmetrics


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "bam": test_dir / "test.bam",
        "metrics": test_dir / "output.metrics",
        "expected_snakefile": test_dir / "expected_Snakefile"
    }


def test_snakefile_collecthsmetrics(test_paths, tmp_path, capsys):
    """Test that collecthsmetrics generates the expected Snakefile."""
    temp_output = tmp_path / "output.metrics"

    # Generate the Snakefile with print_only=True to capture the content
    run_collecthsmetrics(
        bam=str(test_paths["bam"]),
        metrics=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule collecthsmetrics:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"'{test_paths['bam']}'" in content, "Missing BAM input"
    assert f"'{temp_output}'" in content, "Missing metrics output"
    assert "tools/picard/collecthsmetrics" in content, "Missing correct wrapper path"


def test_run_collecthsmetrics(test_paths, tmp_path):
    """Test that collecthsmetrics can be run with the test files."""
    temp_output = tmp_path / "output.metrics"

    result = run_collecthsmetrics(
        bam=str(test_paths["bam"]),
        metrics=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "collecthsmetrics run failed"

    # Verify that the output file was created
    assert temp_output.exists(), "Output metrics file was not created"
    assert temp_output.stat().st_size > 0, "Output metrics file is empty"