import pytest
from pathlib import Path
from bioinformatics_mcp.purge_dups.calcuts.run_calcuts import run_calcuts


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).resolve().parent
    test_dir = base_dir / "test_files"
    return {
        "stats_file": test_dir / "input.stats",
        "coverage_cutoffs": test_dir / "expected.cutoffs",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_calcuts(test_paths, tmp_path, capsys):
    """Test that calcuts generates the expected Snakefile."""
    temp_cutoffs = tmp_path / "output.cutoffs"

    # Generate the Snakefile with print_only=True to capture the content
    run_calcuts(
        stats_file=str(test_paths["stats_file"]),
        coverage_cutoffs=str(temp_cutoffs),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule definition and structure
    assert "rule calcuts:" in content, "Missing 'rule calcuts:' definition"
    assert "input:" in content, "Missing 'input:' section in Snakefile"
    assert "output:" in content, "Missing 'output:' section in Snakefile"
    assert "wrapper:" in content, "Missing 'wrapper:' section in Snakefile"

    # Verify inputs and outputs are correctly defined
    assert "stats_file=" in content, "Missing 'stats_file' parameter in input"
    assert "coverage_cutoffs=" in content, "Missing 'coverage_cutoffs' parameter in output"

    # Check wrapper path is correct (change if different in your setup)
    assert "file:tools/purge_dups/calcuts" in content, "Missing or incorrect wrapper path"


def test_run_calcuts(test_paths, tmp_path):
    """Test that calcuts tool executes successfully with test files."""
    temp_cutoffs = tmp_path / "output.cutoffs"

    # Execute the tool
    result = run_calcuts(
        stats_file=str(test_paths["stats_file"]),
        coverage_cutoffs=str(temp_cutoffs)
    )

    # Verify successful execution
    assert result.returncode == 0, "calcuts run failed with non-zero return code"

    # Verify output file is created
    assert temp_cutoffs.exists(), "Expected output file was not created"
    assert temp_cutoffs.stat().st_size > 0, "Output file is empty"
