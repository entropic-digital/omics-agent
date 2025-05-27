"""Module that tests if the fasttree Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "tests/fasttree"
    return {
        "input_file": test_dir / "example.fasta",
        "expected_tree": test_dir / "expected.tree",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_fasttree(test_paths, tmp_path, capsys):
    """Test that fasttree generates the expected Snakefile."""
    from bioinformatics_mcp.fasttree.mcp.run_fasttree import run_fasttree

    temp_output = tmp_path / "output.tree"

    # Generate the Snakefile with print_only=True to capture the content
    run_fasttree(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule fasttree:" in content, "Missing 'fasttree' rule definition."
    assert "input:" in content, "Missing 'input' section in Snakefile."
    assert "output:" in content, "Missing 'output' section in Snakefile."
    assert "wrapper:" in content, "Missing 'wrapper' section in Snakefile."

    # Verify inputs and outputs are correctly rendered
    assert str(test_paths["input_file"]) in content, (
        "Input file path missing in Snakefile."
    )
    assert str(temp_output) in content, "Output file path missing in Snakefile."


def test_run_fasttree(test_paths, tmp_path):
    """Test that fasttree can be run with the test files."""
    from bioinformatics_mcp.fasttree.mcp.run_fasttree import run_fasttree

    temp_output = tmp_path / "output.tree"

    result = run_fasttree(
        input_file=str(test_paths["input_file"]), output_file=str(temp_output)
    )

    # Verify the process completed successfully
    assert result.returncode == 0, "fasttree run failed with a non-zero return code."

    # Verify that the output file is created
    assert temp_output.exists(), "Expected output file was not created."

    # (Optional) Compare with expected output
    with (
        open(temp_output) as output_file,
        open(test_paths["expected_tree"]) as expected_file,
    ):
        assert output_file.read() == expected_file.read(), (
            "Output file does not match expected file."
        )
