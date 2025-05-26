import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "interval_list": test_dir / "input.interval_list",
        "bed_file": test_dir / "output.bed"
    }

def test_snakefile_intervallisttobed(test_paths, tmp_path, capsys):
    """Test that intervallisttobed generates the expected Snakefile."""
    from tools.gatk.intervallisttobed.run_intervallisttobed import run_intervallisttobed

    temp_bed_file = tmp_path / "temp_output.bed"

    run_intervallisttobed(
        interval_list=str(test_paths["interval_list"]),
        bed_file=str(temp_bed_file),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule intervallisttobed:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "interval_list=" in content, "Missing interval_list input parameter in Snakefile"
    assert "bed_file=" in content, "Missing bed_file output parameter in Snakefile"

def test_run_intervallisttobed(test_paths, tmp_path):
    """Test that intervallisttobed can be run with the test files."""
    from tools.gatk.intervallisttobed.run_intervallisttobed import run_intervallisttobed

    temp_bed_file = tmp_path / "temp_output.bed"

    result = run_intervallisttobed(
        interval_list=str(test_paths["interval_list"]),
        bed_file=str(temp_bed_file)
    )

    assert result.returncode == 0, "intervallisttobed run failed"
    assert temp_bed_file.exists(), "Output BED file was not created"