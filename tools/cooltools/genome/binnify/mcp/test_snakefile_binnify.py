import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "chromsizes": test_dir / "test.chrom.sizes",
        "expected_bed": test_dir / "expected_output.bed",
    }

def test_snakefile_binnify(test_paths, tmp_path, capsys):
    """Test that binnify generates the expected Snakefile."""
    from tools.cooltools.genome.binnify.run_binnify import run_binnify
    temp_output = tmp_path / "output_{binsize}.bed"

    run_binnify(
        chromsizes=str(test_paths["chromsizes"]),
        output=str(temp_output),
        binsize=50000,
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule binnify:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "chromsizes=" in content, "Missing chromsizes input parameter"
    assert "{binsize}" in content, "Output wildcard {binsize} not found"

def test_run_binnify(test_paths, tmp_path):
    """Test that binnify runs correctly with test files."""
    from tools.cooltools.genome.binnify.run_binnify import run_binnify
    temp_output = tmp_path / "output.bed"

    result = run_binnify(
        chromsizes=str(test_paths["chromsizes"]),
        output=str(temp_output),
        binsize=50000
    )

    assert result.returncode == 0, "Binnify execution failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"