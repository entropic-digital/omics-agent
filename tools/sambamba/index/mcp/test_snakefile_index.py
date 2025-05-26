import pytest
from pathlib import Path
import subprocess


@pytest.fixture
def test_paths(tmp_path):
    """Set up test paths for the sambamba index tool."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "test.bam",
        "bam_index": tmp_path / "test.bam.bai",  # Temporary test output
        "expected_snakefile": tmp_path / "Snakefile"
    }


def test_snakefile_sambamba_index(test_paths, capsys):
    """Test that sambamba index generates the expected Snakefile."""
    from tools.sambamba.index.run_index import run_index

    # Generate the Snakefile with print_only=True to capture its content
    run_index(
        bam_file=str(test_paths["bam_file"]),
        bam_index=str(test_paths["bam_index"]),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential parameters and structure in the Snakefile
    assert "rule sambamba_index:" in content, "Missing rule definition for sambamba_index"
    assert "input:" in content, "Missing input section in the Snakefile"
    assert "output:" in content, "Missing output section in the Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in the Snakefile"
    assert "bam_file=" in content, "Missing bam_file input parameter"
    assert "bam_index=" in content, "Missing bam_index output parameter"


def test_run_sambamba_index(test_paths):
    """Test that sambamba index runs successfully with test files."""
    from tools.sambamba.index.run_index import run_index

    result = run_index(
        bam_file=str(test_paths["bam_file"]),
        bam_index=str(test_paths["bam_index"])
    )

    # Verify that the Snakemake workflow ran successfully
    assert result.returncode == 0, "Sambamba index tool execution failed"

    # Verify that the expected output file is created
    assert test_paths["bam_index"].exists(), "BAM index file was not created"