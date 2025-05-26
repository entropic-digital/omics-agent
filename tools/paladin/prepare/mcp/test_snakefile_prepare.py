"""Module that tests if the prepare Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input": test_dir / "test_input.fasta",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_prepare(test_paths, tmp_path, capsys):
    """Test that the prepare Snakefile is generated correctly."""
    from tools.paladin.mcp.run_prepare import run_prepare

    temp_output = tmp_path / "output.fasta"

    # Generate the Snakefile with print_only=True to capture the content
    run_prepare(output_file=str(temp_output), citation="Test Citation", print_only=True)

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule and parameters are present
    assert "rule prepare:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "output_file=" in content, "Missing output_file parameter in Snakefile"

    # Validate citation parameter is included if specified
    assert "params.citation=" in content, "Missing citation parameter in Snakefile"


def test_run_prepare(test_paths, tmp_path):
    """Test that the prepare tool runs successfully with test inputs."""
    from tools.paladin.mcp.run_prepare import run_prepare

    temp_output = tmp_path / "output.fasta"

    # Attempt to run the prepare tool
    result = run_prepare(output_file=str(temp_output), citation="Test Citation")

    # Verify that the tool runs successfully
    assert result.returncode == 0, "prepare run failed with non-zero exit code"
    assert temp_output.exists(), "Expected output file was not created by prepare"
