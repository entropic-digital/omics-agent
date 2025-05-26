import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "test.bam",
        "intervals": [test_dir / "interval1.bed", test_dir / "interval2.bed"],
        "reference_genome": test_dir / "reference.fa",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_depthofcoverage(test_paths, tmp_path, capsys):
    """Test that depthofcoverage generates the expected Snakefile."""
    from tools.gatk.depthofcoverage.run_depthofcoverage import run_depthofcoverage
    temp_output_base = tmp_path / "output_base"

    # Generate the Snakefile with print_only=True to capture the content
    run_depthofcoverage(
        bam_file=str(test_paths["bam_file"]),
        intervals=[str(i) for i in test_paths["intervals"]],
        reference_genome=str(test_paths["reference_genome"]),
        output_base=str(temp_output_base),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule depthofcoverage:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    # Add assertions for all required inputs
    assert f"bam_file='{str(test_paths['bam_file'])}'" in content, "Missing bam_file input parameter"
    assert "intervals=" in content, "Missing intervals input parameter"
    assert f"reference_genome='{str(test_paths['reference_genome'])}'" in content, "Missing reference_genome input"
    # Add assertions for all required outputs
    assert f"output_base='{str(temp_output_base)}'" in content, "Missing output_base output parameter"


def test_run_depthofcoverage(test_paths, tmp_path):
    """Test that depthofcoverage can be run with the test files."""
    from tools.gatk.depthofcoverage.run_depthofcoverage import run_depthofcoverage
    temp_output_base = tmp_path / "output_base"

    result = run_depthofcoverage(
        bam_file=str(test_paths["bam_file"]),
        intervals=[str(i) for i in test_paths["intervals"]],
        reference_genome=str(test_paths["reference_genome"]),
        output_base=str(temp_output_base)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "depthofcoverage run failed"

    # Optionally, add checks for expected output files (if applicable)
    expected_files = [
        f"{temp_output_base}.sample_cumulative_coverage_counts",
        f"{temp_output_base}.sample_cumulative_coverage_proportions",
        f"{temp_output_base}.sample_interval_statistics",
        f"{temp_output_base}.sample_interval_summary",
    ]
    for file in expected_files:
        assert Path(file).exists(), f"Expected output file {file} was not created"