import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "gfa_file": test_dir / "test.gfa",
        "expected_snakefile": test_dir / "Snakefile",
        "dummy_output": test_dir / "dummy_output.txt",
    }


def test_snakefile_gfatools(test_paths, tmp_path, capsys):
    """Test that gfatools generates the expected Snakefile."""
    from bioinformatics_mcp.gfatools.run_gfatools import run_gfatools

    # Generate the Snakefile with print_only=True to capture the content
    run_gfatools(
        gfa_file=str(test_paths["gfa_file"]),
        command="view",
        output_file=str(test_paths["dummy_output"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule gfatools:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "gfa_file=" in content, "Missing gfa_file parameter"
    assert "command=" in content, "Missing command parameter"
    assert "output_file=" in content, "Missing output_file parameter"


def test_run_gfatools(test_paths, tmp_path):
    """Test that gfatools can be run with the test files."""
    from bioinformatics_mcp.gfatools.run_gfatools import run_gfatools

    temp_output = tmp_path / "output.txt"

    result = run_gfatools(
        gfa_file=str(test_paths["gfa_file"]),
        command="stat",
        output_file=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "gfatools run failed"

    # Check that the output file is created
    assert temp_output.is_file(), "Output file not created"

    # Optional: Validate the output content (not shown here; depends on expected output)