from pathlib import Path
import pytest


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file1": test_dir / "test1.bam",
        "bam_file2": test_dir / "test2.bam",
        "blacklist": test_dir / "blacklist.bed",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_bampefragmentsize(test_paths, tmp_path, capsys):
    """Test that bampefragmentsize generates the expected Snakefile."""
    from tools.deeptools.bampefragmentsize.run_bampefragmentsize import (
        run_bampefragmentsize,
    )

    histogram_output = tmp_path / "histogram.png"
    raw_lengths_output = tmp_path / "fragment_lengths.tab"

    # Generate the Snakefile with print_only=True to capture the content
    run_bampefragmentsize(
        bams=[str(test_paths["bam_file1"]), str(test_paths["bam_file2"])],
        blacklist=str(test_paths["blacklist"]),
        histogram=str(histogram_output),
        raw_lengths=str(raw_lengths_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    snakefile_content = captured.out

    # Verify essential rule elements are present in the Snakefile content
    assert "rule bampefragmentsize:" in snakefile_content, (
        "Missing bampefragmentsize rule definition"
    )
    assert "input:" in snakefile_content, "Missing input section in Snakefile"
    assert "output:" in snakefile_content, "Missing output section in Snakefile"
    assert "params:" in snakefile_content, "Missing params section in Snakefile"
    assert "wrapper:" in snakefile_content, "Missing wrapper section in Snakefile"
    assert "bams=" in snakefile_content, "Missing bams input parameter in Snakefile"
    assert "blacklist=" in snakefile_content, (
        "Missing blacklist input parameter in Snakefile"
    )
    assert "hist=" in snakefile_content, "Missing histogram output in Snakefile"
    assert "raw=" in snakefile_content, (
        "Missing raw fragment lengths output in Snakefile"
    )


def test_run_bampefragmentsize(test_paths, tmp_path):
    """Test that bampefragmentsize can successfully run with the test files."""
    from tools.deeptools.bampefragmentsize.run_bampefragmentsize import (
        run_bampefragmentsize,
    )

    histogram_output = tmp_path / "histogram.png"
    raw_lengths_output = tmp_path / "fragment_lengths.tab"

    result = run_bampefragmentsize(
        bams=[str(test_paths["bam_file1"]), str(test_paths["bam_file2"])],
        blacklist=str(test_paths["blacklist"]),
        histogram=str(histogram_output),
        raw_lengths=str(raw_lengths_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "bampefragmentsize tool execution failed"
    # Verify output files are created
    assert histogram_output.exists(), "Histogram output file not created"
    assert raw_lengths_output.exists(), "Raw fragment lengths output file not created"
