import pytest
from pathlib import Path
from tools.dada2.filter_trim.mcp.run_filter_trim import run_filter_trim


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = (
        base_dir / "test_files"
    )  # Assuming test files are placed in a test_files directory
    return {
        "fwd": test_dir / "test_forward.fastq",
        "rev": test_dir / "test_reverse.fastq",
        "filt": test_dir / "filtered_forward.fastq.gz",
        "filt_rev": test_dir / "filtered_reverse.fastq.gz",
        "stats": test_dir / "stats.tsv",
    }


def test_snakefile_filter_trim(test_paths, tmp_path, capsys):
    """Test that the filter-trim tool generates the expected Snakefile."""
    temp_filt = tmp_path / "temp_filtered_forward.fastq.gz"
    temp_filt_rev = tmp_path / "temp_filtered_reverse.fastq.gz"
    temp_stats = tmp_path / "temp_stats.tsv"

    # Generate the Snakefile with print_only=True to capture the content
    run_filter_trim(
        fwd=str(test_paths["fwd"]),
        rev=str(test_paths["rev"]),
        filt=str(temp_filt),
        filt_rev=str(temp_filt_rev),
        stats=str(temp_stats),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential elements of the Snakefile
    assert "rule filter_trim:" in content, "Missing rule definition for filter_trim"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"fwd='{test_paths['fwd']}'" in content, "Missing forward input parameter"
    assert f"rev='{test_paths['rev']}'" in content, "Missing reverse input parameter"
    assert f"filt='{temp_filt}'" in content, "Missing filtered forward output parameter"
    assert f"filt_rev='{temp_filt_rev}'" in content, (
        "Missing filtered reverse output parameter"
    )
    assert f"stats='{temp_stats}'" in content, "Missing stats output parameter"


def test_run_filter_trim(test_paths, tmp_path):
    """Test that the filter-trim tool runs successfully with test files."""
    temp_filt = tmp_path / "output_filtered_forward.fastq.gz"
    temp_filt_rev = tmp_path / "output_filtered_reverse.fastq.gz"
    temp_stats = tmp_path / "output_stats.tsv"

    # Run the tool with test files
    result = run_filter_trim(
        fwd=str(test_paths["fwd"]),
        rev=str(test_paths["rev"]),
        filt=str(temp_filt),
        filt_rev=str(temp_filt_rev),
        stats=str(temp_stats),
    )

    # Verify that the tool execution was successful
    assert result.returncode == 0, "filter-trim tool execution failed"

    # Verify the expected output files are present
    assert temp_filt.exists(), "Filtered forward FASTQ output file not created"
    assert temp_filt_rev.exists(), "Filtered reverse FASTQ output file not created"
    assert temp_stats.exists(), "Stats output file not created"
