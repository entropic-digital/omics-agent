import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "test.bam",
        "sorted_bam_file": test_dir / "sorted_test.bam",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_sort(test_paths, tmp_path, capsys):
    """Test that sambamba_sort generates the expected Snakefile."""
    from bioinformatics_mcp.sambamba.sort.run_sort import run_sort
    temp_output = tmp_path / "sorted_output.bam"

    run_sort(
        bam_file=str(test_paths["bam_file"]),
        sorted_bam_file=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule all:" in content, "Missing 'all' rule definition"
    assert "rule sambamba_sort:" in content, "Missing 'sambamba_sort' rule definition"
    assert "input:" in content, "Missing 'input' section"
    assert "bam_file=" in content, "Missing 'bam_file' input parameter"
    assert "output:" in content, "Missing 'output' section"
    assert "sorted_bam_file" in content, "Missing 'sorted_bam_file' output parameter"
    assert "wrapper:" in content, "Missing 'wrapper' section"
    assert "file:tools/sambamba/sort" in content, "Incorrect or missing wrapper path"

def test_run_sort(test_paths, tmp_path):
    """Test that sambamba_sort runs with the test files and produces output."""
    from bioinformatics_mcp.sambamba.sort.run_sort import run_sort
    temp_output = tmp_path / "sorted_output.bam"

    result = run_sort(
        bam_file=str(test_paths["bam_file"]),
        sorted_bam_file=str(temp_output)
    )

    assert result.returncode == 0, "sambamba_sort run failed"
    assert temp_output.exists(), "Sorted BAM file was not created"
    assert temp_output.stat().st_size > 0, "Sorted BAM file is empty"