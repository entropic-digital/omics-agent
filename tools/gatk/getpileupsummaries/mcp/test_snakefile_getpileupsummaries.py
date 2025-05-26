import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up paths for the test files."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test_files"
    return {
        "bam": test_dir / "test.bam",
        "intervals": test_dir / "test_intervals.bed",
        "variants": test_dir / "test_variants.vcf.gz",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }

def test_snakefile_getpileupsummaries(test_paths, tmp_path, capsys):
    """Test that getpileupsummaries generates the expected Snakefile."""
    from tools.gatk.getpileupsummaries.run_getpileupsummaries import run_getpileupsummaries

    temp_output = tmp_path / "output.table"

    run_getpileupsummaries(
        bam=str(test_paths["bam"]),
        intervals=str(test_paths["intervals"]),
        variants=str(test_paths["variants"]),
        output=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule getpileupsummaries:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam=" in content, "Missing BAM input parameter"
    assert "intervals=" in content, "Missing intervals input parameter"
    assert "variants=" in content, "Missing variants input parameter"
    assert "output=" in content, "Missing output parameter"

def test_run_getpileupsummaries(test_paths, tmp_path):
    """Test that getpileupsummaries can be run with the test files."""
    from tools.gatk.getpileupsummaries.run_getpileupsummaries import run_getpileupsummaries

    temp_output = tmp_path / "output.table"

    result = run_getpileupsummaries(
        bam=str(test_paths["bam"]),
        intervals=str(test_paths["intervals"]),
        variants=str(test_paths["variants"]),
        output=str(temp_output)
    )

    assert result.returncode == 0, "getpileupsummaries run failed"
    assert temp_output.exists(), "Output file was not created"