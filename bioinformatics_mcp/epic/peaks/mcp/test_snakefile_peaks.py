import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "treatment": test_dir / "treatment.bed",
        "background": test_dir / "background.bed",
        "enriched_regions": test_dir / "expected_enriched_regions.txt",
        "snakefile_expected": test_dir / "expected_Snakefile"
    }


def test_snakefile_peaks(test_paths, tmp_path, capsys):
    """Test that peaks generates the expected Snakefile."""
    from bioinformatics_mcp.epic.peaks import run_peaks

    run_peaks(
        treatment=str(test_paths["treatment"]),
        background=str(test_paths["background"]),
        enriched_regions="output_enriched_regions.bed",
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule peaks:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "treatment=" in content, "Missing treatment parameter"
    assert "background=" in content, "Missing background parameter"
    assert "enriched_regions=" in content, "Missing enriched_regions parameter"


def test_run_peaks(test_paths, tmp_path):
    """Test that peaks can be run with the test files."""
    from bioinformatics_mcp.epic.peaks import run_peaks

    temp_output = tmp_path / "output_enriched_regions.bed"
    temp_log = tmp_path / "log.txt"

    result = run_peaks(
        treatment=str(test_paths["treatment"]),
        background=str(test_paths["background"]),
        enriched_regions=str(temp_output),
        log=str(temp_log)
    )

    assert result.returncode == 0, "peaks run failed"
    assert temp_output.exists(), "Output enriched_regions file not created"
    assert temp_log.exists(), "Log file not created"