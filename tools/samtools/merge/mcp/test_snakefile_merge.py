import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam1": test_dir / "input1.bam",
        "input_bam2": test_dir / "input2.bam",
        "expected_snakefile": test_dir / "Snakefile",
        "expected_output_bam": test_dir / "expected_output.bam",
    }


def test_snakefile_merge(test_paths, tmp_path, capsys):
    """Test that samtools merge generates the expected Snakefile."""
    from tools.samtools.merge.run_merge import run_merge

    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture content
    run_merge(
        input_bam_files=[str(test_paths["input_bam1"]), str(test_paths["input_bam2"])],
        output_bam_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assertions for all essential Snakefile elements
    assert "rule merge:" in content, "Snakefile missing 'merge' rule definition"
    assert "input:" in content, "Snakefile missing input section"
    assert "output:" in content, "Snakefile missing output section"
    assert "wrapper:" in content, "Snakefile missing wrapper section"
    assert test_paths["input_bam1"].name in content, "Input BAM 1 missing from Snakefile"
    assert test_paths["input_bam2"].name in content, "Input BAM 2 missing from Snakefile"
    assert str(temp_output) in content, "Output BAM missing from Snakefile"
    assert "file:tools/samtools/merge" in content, "Incorrect wrapper path in Snakefile"


def test_run_merge(test_paths, tmp_path):
    """Test that samtools merge can be executed with test files."""
    from tools.samtools.merge.run_merge import run_merge

    temp_output = tmp_path / "output.bam"

    # Execute the merge tool
    result = run_merge(
        input_bam_files=[str(test_paths["input_bam1"]), str(test_paths["input_bam2"])],
        output_bam_file=str(temp_output),
    )

    # Assertions for a successful run
    assert result.returncode == 0, "samtools merge run failed"
    assert temp_output.exists(), "Output BAM file was not created"
    # Depending on your requirements, add additional checks like file size/content comparison