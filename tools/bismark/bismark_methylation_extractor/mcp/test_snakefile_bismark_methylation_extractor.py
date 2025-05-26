import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "input_bam": test_dir / "test_input.bam",
        "output_dir": test_dir / "output",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_bismark_methylation_extractor(test_paths, tmp_path, capsys):
    """Test that bismark_methylation_extractor generates the expected Snakefile."""
    from tools.bismark.bismark_methylation_extractor.run_bismark_methylation_extractor import (
        run_bismark_methylation_extractor,
    )

    temp_output_dir = tmp_path / "output_dir"

    # Generate the Snakefile with print_only=True to capture the output
    run_bismark_methylation_extractor(
        input_bam=str(test_paths["input_bam"]),
        output_dir=str(temp_output_dir),
        ignore=10,
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential Snakefile elements
    assert "rule bismark_methylation_extractor:" in content, (
        "Snakefile is missing the rule definition."
    )
    assert "input:" in content, "Snakefile is missing the input section."
    assert "output:" in content, "Snakefile is missing the output section."
    assert "params:" in content, "Snakefile is missing the params section."
    assert "wrapper:" in content, "Snakefile is missing the wrapper definition."
    assert "tools/bismark/bismark_methylation_extractor" in content, (
        "Incorrect wrapper path."
    )

    # Verify input parameters
    assert "input_bam" in content, "Snakefile is missing the 'input_bam' parameter."
    # Verify params
    assert "ignore=" in content, "Snakefile is missing the 'ignore' parameter."

    # Verify output parameters
    assert "output_dir" in content, "Snakefile is missing the 'output_dir' parameter."


def test_run_bismark_methylation_extractor(test_paths, tmp_path):
    """Test that bismark_methylation_extractor runs successfully with the test files."""
    from tools.bismark.bismark_methylation_extractor.run_bismark_methylation_extractor import (
        run_bismark_methylation_extractor,
    )

    temp_output_dir = tmp_path / "output_dir"
    temp_mbias_report = tmp_path / "mbias_report.txt"
    temp_splitting_report = tmp_path / "splitting_report.txt"

    # Execute the tool
    result = run_bismark_methylation_extractor(
        input_bam=str(test_paths["input_bam"]),
        output_dir=str(temp_output_dir),
        mbias_report=str(temp_mbias_report),
        splitting_report=str(temp_splitting_report),
    )

    # Verify the run is successful
    assert result.returncode == 0, "bismark_methylation_extractor run failed."
    assert temp_output_dir.exists(), "The output directory was not created."
    assert temp_mbias_report.exists(), "The M-bias report was not generated."
    assert temp_splitting_report.exists(), "The splitting report was not generated."
