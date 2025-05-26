import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reference_genome": test_dir / "reference.fasta",
        "indexed_reference_genome": test_dir / "indexed_reference.mmi",
    }


def test_snakefile_index(test_paths, tmp_path, capsys):
    """Test that minimap2 index generates the expected Snakefile."""
    from tools.minimap2.index.run_index import run_index

    temp_output = tmp_path / "indexed_reference.mmi"

    # Generate the Snakefile with print_only=True to capture the content
    run_index(
        reference_genome=str(test_paths["reference_genome"]),
        indexed_reference_genome=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the Snakefile
    assert "rule index:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Check required inputs
    assert "reference_genome=" in content, (
        "Missing reference_genome parameter in Snakefile"
    )

    # Check required outputs
    assert "indexed_reference_genome=" in content, (
        "Missing indexed_reference_genome parameter in Snakefile"
    )


def test_run_index(test_paths, tmp_path):
    """Test that minimap2 index can be run with the test files."""
    from tools.minimap2.index.run_index import run_index

    temp_output = tmp_path / "indexed_reference.mmi"

    result = run_index(
        reference_genome=str(test_paths["reference_genome"]),
        indexed_reference_genome=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "Minimap2 index run failed"

    # Verify the output file is created
    assert temp_output.exists(), "Indexed reference genome file was not created"
