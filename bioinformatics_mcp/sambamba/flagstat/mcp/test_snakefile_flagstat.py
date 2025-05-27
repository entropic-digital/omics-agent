"""Module that tests if the flagstat Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "bam_file": test_dir / "test.bam",
        "flag_statistics": test_dir / "expected_flagstat.txt",
    }


def test_snakefile_flagstat(test_paths, tmp_path, capsys):
    """Test that flagstat generates the expected Snakefile."""
    from bioinformatics_mcp.sambamba.flagstat.run_flagstat import run_flagstat

    temp_flagstat = tmp_path / "flag_statistics.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_flagstat(
        bam_file=str(test_paths["bam_file"]),
        flag_statistics=str(temp_flagstat),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule flagstat:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Add assertions for all required input parameters
    assert "bam_file=" in content, "Missing bam_file parameter"
    # Add assertions for all required output parameters
    assert "flag_statistics=" in content, "Missing flag_statistics parameter"


def test_run_flagstat(test_paths, tmp_path):
    """Test that flagstat can be run with the test files."""
    from bioinformatics_mcp.sambamba.flagstat.run_flagstat import run_flagstat

    temp_flagstat = tmp_path / "flag_statistics.txt"

    result = run_flagstat(
        bam_file=str(test_paths["bam_file"]), flag_statistics=str(temp_flagstat)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "flagstat run failed"

    # Check that output file was created
    assert temp_flagstat.exists(), "Output flagstat file not created"
    assert temp_flagstat.stat().st_size > 0, "Output flagstat file is empty"
