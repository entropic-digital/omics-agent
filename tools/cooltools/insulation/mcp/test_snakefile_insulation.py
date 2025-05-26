"""Module that tests if the insulation Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths for testing the insulation tool."""
    base_dir = Path(__file__).parent / "test_data"
    return {
        "mcool_file": base_dir / "test.mcool",
        "view_file": base_dir / "test_view.bed",
        "expected_output": base_dir / "expected_output.tsv",
        "output_tsv": base_dir / "output.tsv",
    }


def test_snakefile_insulation(test_paths, tmp_path, capsys):
    """Test that the insulation tool generates the expected Snakefile."""
    from tools.cooltools.insulation.run_insulation import run_insulation

    temp_output = tmp_path / "output.tsv"

    # Generate the Snakefile with print_only=True to capture its content
    run_insulation(
        mcool_file=str(test_paths["mcool_file"]),
        output_tsv=str(temp_output),
        window=[10000, 25000],
        resolution=10000,
        chunksize=1000000,
        extra="--some-flag",
        print_only=True,
    )

    # Capture the printed output
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in the generated Snakefile
    assert "rule insulation:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper definition in Snakefile"

    # Verify all required inputs and outputs are specified
    assert "mcool_file=" in content, "Missing mcool_file input parameter in Snakefile"
    assert "output_tsv=" in content, "Missing output_tsv output parameter in Snakefile"
    assert "window=" in content, "Missing window parameter in Snakefile"
    assert "resolution=" in content, "Missing resolution parameter in Snakefile"

    # Additional assertions
    assert "--some-flag" in content, "Missing extra argument in Snakefile"


def test_run_insulation(test_paths, tmp_path):
    """Test that the insulation tool can be executed with the test files."""
    from tools.cooltools.insulation.run_insulation import run_insulation

    temp_output = tmp_path / "output.tsv"

    # Execute the tool with test file inputs
    result = run_insulation(
        mcool_file=str(test_paths["mcool_file"]),
        output_tsv=str(temp_output),
        window=[10000, 25000],
        resolution=10000,
        chunksize=1000000,
        extra=None,
    )

    # Verify the process completes successfully
    assert result.returncode == 0, "insulation tool execution failed"
    assert temp_output.exists(), "Output .tsv file was not created"

    # Optional: Verify the contents of the generated output file
    with open(temp_output, "r") as output_file:
        content = output_file.read()
        assert "insulation_score" in content, "Output file is missing insulation scores"
        assert "boundary" in content, "Output file is missing boundary"
