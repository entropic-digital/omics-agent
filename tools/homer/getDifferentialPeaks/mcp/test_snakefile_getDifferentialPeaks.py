import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths for getDifferentialPeaks."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "peak_files_condition1": test_dir / "condition1_peaks.txt",
        "peak_files_condition2": test_dir / "condition2_peaks.txt",
        "annotation_file": test_dir / "annotation_file.txt",
        "expected_snakefile": test_dir / "Snakefile",
    }

def test_snakefile_getDifferentialPeaks(test_paths, tmp_path, capsys):
    """Test that getDifferentialPeaks generates the expected Snakefile."""
    from tools.homer.getDifferentialPeaks.run_getDifferentialPeaks import run_getDifferentialPeaks

    temp_output = tmp_path / "differential_peaks_output.txt"

    run_getDifferentialPeaks(
        condition1="condition1",
        condition2="condition2",
        output_file=str(temp_output),
        peak_files_condition1=str(test_paths["peak_files_condition1"]),
        peak_files_condition2=str(test_paths["peak_files_condition2"]),
        annotation_file=str(test_paths["annotation_file"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule getDifferentialPeaks:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "peak_files_condition1=" in content, "Missing peak_files_condition1 input"
    assert "peak_files_condition2=" in content, "Missing peak_files_condition2 input"
    assert "output_file=" in content, "Missing output_file parameter"

def test_run_getDifferentialPeaks(test_paths, tmp_path):
    """Test that getDifferentialPeaks runs successfully with test files."""
    from tools.homer.getDifferentialPeaks.run_getDifferentialPeaks import run_getDifferentialPeaks

    temp_output = tmp_path / "differential_peaks_output.txt"

    result = run_getDifferentialPeaks(
        condition1="condition1",
        condition2="condition2",
        output_file=str(temp_output),
        peak_files_condition1=str(test_paths["peak_files_condition1"]),
        peak_files_condition2=str(test_paths["peak_files_condition2"]),
        annotation_file=str(test_paths["annotation_file"]),
    )

    assert result.returncode == 0, "getDifferentialPeaks run failed"
    assert temp_output.exists(), "Output file not created"
