"""Module that tests if the stats Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        # Add all input and output files for testing
        "bam_file": test_dir / "test_input.bam",
        "bamstats_file": test_dir / "test_output.bamstats",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_stats(test_paths, tmp_path, capsys):
    """Test that stats generates the expected Snakefile."""
    from bioinformatics_mcp.bamtools.stats.run_stats import run_stats

    # Temporary file path for captured output
    temp_bamstats_file = tmp_path / "output.bamstats"

    # Run the function with print_only to generate Snakefile content
    run_stats(
        bam_file=str(test_paths["bam_file"]),
        bamstats_file=str(temp_bamstats_file),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify Snakefile contains essential rule elements
    assert "rule stats:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify inputs are correctly set
    assert "bam_file=" in content, "Missing bam_file input parameter"

    # Verify outputs are correctly set
    assert "bamstats_file=" in content, "Missing bamstats_file output parameter"

    # Verify wrapper path
    assert "tools/bamtools/stats" in content, "Incorrect or missing wrapper path"


def test_run_stats(test_paths, tmp_path):
    """Test that stats can be run with the test files."""
    from bioinformatics_mcp.bamtools.stats.run_stats import run_stats

    # Temporary file path for test output
    temp_bamstats_file = tmp_path / "output.bamstats"

    # Execute the stats function
    result = run_stats(
        bam_file=str(test_paths["bam_file"]), bamstats_file=str(temp_bamstats_file)
    )

    # Verify process completed successfully
    assert result.returncode == 0, "stats run failed"

    # Verify that the output BAM stats file was created
    assert temp_bamstats_file.exists(), "Output BAM stats file was not created"

    # (Optional) Add assertions to verify the contents of the output file if needed
