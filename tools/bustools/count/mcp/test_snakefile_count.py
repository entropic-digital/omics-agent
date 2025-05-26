import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bus": test_dir / "input.bus",
        "genemap": test_dir / "genemap.txt",
        "txnames": test_dir / "txnames.txt",
        "ecmap": test_dir / "ecmap.txt",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_count(test_paths, tmp_path, capsys):
    """Test that the count tool generates the expected Snakefile."""
    from tools.bustools.count.run_count import run_count
    temp_output = tmp_path / "output.genes.txt"

    # Generate the Snakefile with print_only=True
    run_count(
        bus=str(test_paths["bus"]),
        genemap=str(test_paths["genemap"]),
        txnames=str(test_paths["txnames"]),
        ecmap=str(test_paths["ecmap"]),
        output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements in the Snakefile
    assert "rule count:" in content, "Missing rule definition for 'count'"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "bus=" in content, "Missing 'bus' input in Snakefile"
    assert "genemap=" in content, "Missing 'genemap' input in Snakefile"
    assert "txnames=" in content, "Missing 'txnames' input in Snakefile"
    assert "ecmap=" in content, "Missing 'ecmap' input in Snakefile"
    assert "output=" in content, "Missing 'output' parameter in Snakefile"
    assert "file:tools/bustools/count" in content, "Incorrect or missing wrapper path"

def test_run_count(test_paths, tmp_path):
    """Test that the count tool runs successfully with the test files."""
    from tools.bustools.count.run_count import run_count
    temp_output = tmp_path / "output.genes.txt"

    result = run_count(
        bus=str(test_paths["bus"]),
        genemap=str(test_paths["genemap"]),
        txnames=str(test_paths["txnames"]),
        ecmap=str(test_paths["ecmap"]),
        output=str(temp_output)
    )

    # Check the process exit code for success
    assert result.returncode == 0, "count tool execution failed"
    # Check if the expected output file is created
    assert temp_output.exists(), "Expected output file was not generated"