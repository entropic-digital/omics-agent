import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "test.bam",
        "input_control": test_dir / "control.bam",
        "output_dir": test_dir / "output",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_findPeaks(test_paths, tmp_path, capsys):
    """Test that findPeaks generates the expected Snakefile."""
    from tools.homer.findPeaks.run_findPeaks import run_findPeaks

    temp_output_dir = tmp_path / "output_dir"

    run_findPeaks(
        input_bam=str(test_paths["input_bam"]),
        output_dir=str(temp_output_dir),
        genome="hg19",
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule findPeaks:" in content, "Missing rule definition in the Snakefile"
    assert "input:" in content, "Missing input section in the Snakefile"
    assert "output:" in content, "Missing output section in the Snakefile"
    assert "params:" in content, "Missing params section in the Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in the Snakefile"
    assert "bam=" in content, "Missing BAM input parameter in the Snakefile"
    assert "output_dir=" in content, "Missing output directory parameter in the Snakefile"
    assert "genome=" in content, "Missing genome parameter in the Snakefile"

def test_run_findPeaks(test_paths, tmp_path):
    """Test that findPeaks can be run with the test files."""
    from tools.homer.findPeaks.run_findPeaks import run_findPeaks

    temp_output_dir = tmp_path / "output_dir"

    result = run_findPeaks(
        input_bam=str(test_paths["input_bam"]),
        output_dir=str(temp_output_dir),
        genome="hg19"
    )

    assert result.returncode == 0, "findPeaks run failed"
    assert (temp_output_dir / "peaks.txt").is_file(), "Peaks output file missing"
    assert (temp_output_dir / "statistics.txt").is_file(), "Statistics output file missing"