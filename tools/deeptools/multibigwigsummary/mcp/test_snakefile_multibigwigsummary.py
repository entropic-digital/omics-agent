import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths for multibigwigsummary."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bw": [test_dir / "test1.bw", test_dir / "test2.bw"],  # Example bigWig test files
        "blacklist": test_dir / "blacklist.bed",  # Example blacklist file
        "bed": test_dir / "regions.bed",  # Example BED file
        "npz": test_dir / "output.npz",  # Expected compressed matrix file
        "counts": test_dir / "output_counts.tsv",  # Expected counts file
        "expected_snakefile": test_dir / "Snakefile",  # Expected Snakefile structure
    }


def test_snakefile_multibigwigsummary(test_paths, tmp_path, capsys):
    """Test that multibigwigsummary generates the expected Snakefile."""
    from tools.deeptools.multibigwigsummary.mcp.run_multibigwigsummary import run_multibigwigsummary
    
    temp_npz = tmp_path / "output.npz"
    temp_counts = tmp_path / "output_counts.tsv"

    # Generate the Snakefile with print_only=True
    run_multibigwigsummary(
        bw=[str(f) for f in test_paths["bw"]],
        npz=str(temp_npz),
        counts=str(temp_counts),
        blacklist=str(test_paths["blacklist"]),
        bed=str(test_paths["bed"]),
        extra="--binSize 1000",
        print_only=True,
    )
    
    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in the generated Snakefile
    assert "rule multibigwigsummary:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify required inputs
    assert "bw=" in content, "Missing bigWig input parameter"
    assert "blacklist=" in content, "Missing blacklist input parameter"
    assert "bed=" in content, "Missing BED input parameter"

    # Verify required outputs
    assert "npz=" in content, "Missing compressed matrix output parameter"
    assert "counts=" in content, "Missing counts output parameter"

    # Verify additional parameters
    assert "--binSize 1000" in content, "Missing extra parameters in Snakefile"


def test_run_multibigwigsummary(test_paths, tmp_path):
    """Test that multibigwigsummary runs successfully with the test files."""
    from tools.deeptools.multibigwigsummary.mcp.run_multibigwigsummary import run_multibigwigsummary
    
    temp_npz = tmp_path / "output.npz"
    temp_counts = tmp_path / "output_counts.tsv"

    # Execute the tool with test data
    result = run_multibigwigsummary(
        bw=[str(f) for f in test_paths["bw"]],
        npz=str(temp_npz),
        counts=str(temp_counts),
        blacklist=str(test_paths.get("blacklist")),
        bed=str(test_paths.get("bed")),
        extra="--binSize 1000",
    )

    # Verify that the process completed successfully
    assert result.returncode == 0, "multibigwigsummary tool execution failed"

    # Verify output files are created
    assert temp_npz.exists(), "Missing output .npz file after execution"
    assert temp_counts.exists(), "Missing output counts file after execution"