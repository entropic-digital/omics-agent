import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam": test_dir / "test.bam",
        "intervals": test_dir / "test.intervals",
        "expected_counts": test_dir / "expected_counts.tsv",
    }


def test_snakefile_collectreadcounts(test_paths, tmp_path, capsys):
    """Test that collectreadcounts generates the expected Snakefile."""
    from tools.collectreadcounts.mcp.run_collectreadcounts import run_collectreadcounts
    temp_output = tmp_path / "output.tsv"

    # Generate the Snakefile with print_only=True to capture the content
    run_collectreadcounts(
        bam=str(test_paths["bam"]),
        intervals=str(test_paths["intervals"]),
        counts=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the Snakefile
    assert "rule collectreadcounts:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert f"bam={str(test_paths['bam'])}" in content, "Missing BAM input in Snakefile"
    assert f"intervals={str(test_paths['intervals'])}" in content, "Missing intervals input in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert f"counts={str(temp_output)}" in content, "Missing counts output in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper definition in Snakefile"
    assert "mergingRule=OVERLAPPING_ONLY" in content, "Default mergingRule parameter not set in Snakefile"


def test_run_collectreadcounts(test_paths, tmp_path):
    """Test that collectreadcounts can be run with the test files."""
    from tools.collectreadcounts.mcp.run_collectreadcounts import run_collectreadcounts
    temp_output = tmp_path / "output.tsv"

    result = run_collectreadcounts(
        bam=str(test_paths["bam"]),
        intervals=str(test_paths["intervals"]),
        counts=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "collectreadcounts run failed"
    
    # Verify the output file is created
    assert temp_output.exists(), "Counts output file was not created"
    
    # Optionally, compare output content with expected
    with open(temp_output, "r") as output_file, open(test_paths["expected_counts"], "r") as expected_file:
        assert output_file.read() == expected_file.read(), "Output counts file does not match expected output"