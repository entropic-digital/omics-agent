"""Module that tests if the kmers Snakefile is rendered and runnable"""

import pytest
from pathlib import Path
from bioinformatics_mcp.vg.kmers.run_kmers import run_kmers


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "input_vg": test_dir / "example_input.vg",
        "output_kmers": test_dir / "example_output.kmers",
    }


def test_snakefile_kmers(test_paths, tmp_path, capsys):
    """Test that the kmers Snakefile is generated correctly."""
    temp_output = tmp_path / "output.kmers"

    # Generate the Snakefile with print_only=True
    run_kmers(
        input_vg=str(test_paths["input_vg"]),
        output_kmers=str(temp_output),
        k=31,
        graph_name="example_graph",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    snakefile_content = captured.out

    # Check essential Snakefile elements
    assert "rule kmers:" in snakefile_content, "Missing 'rule kmers:' in Snakefile"
    assert "input:" in snakefile_content, "Missing 'input:' definition in Snakefile"
    assert "output:" in snakefile_content, "Missing 'output:' definition in Snakefile"
    assert "params:" in snakefile_content, "Missing 'params:' section in Snakefile"
    assert "wrapper:" in snakefile_content, "Missing wrapper section in Snakefile"

    # Verify inputs, outputs, and params match expectations
    assert "input_vg=" in snakefile_content, "Missing 'input_vg' in Snakefile input"
    assert "output_kmers=" in snakefile_content, (
        "Missing 'output_kmers' in Snakefile output"
    )
    assert "k=31" in snakefile_content, "Missing 'k=31' parameter in Snakefile"
    assert "graph_name=example_graph" in snakefile_content, (
        "Missing 'graph_name' in Snakefile params"
    )


def test_run_kmers(test_paths, tmp_path):
    """Test that the kmers tool executes successfully with test files."""
    temp_output = tmp_path / "output.kmers"

    # Run the tool
    result = run_kmers(
        input_vg=str(test_paths["input_vg"]),
        output_kmers=str(temp_output),
        k=31,
        graph_name="example_graph",
    )

    # Verify the tool executed successfully
    assert result.returncode == 0, "kmers tool run failed with a non-zero return code"

    # Verify the output file is created
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"
