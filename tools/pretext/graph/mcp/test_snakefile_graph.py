import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bedgraph_file": test_dir / "test.bedgraph",
        "pretext_contact_map": test_dir / "test.pretext",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_graph_generation(test_paths, tmp_path, capsys):
    """Test that the graph tool generates a valid Snakefile."""
    from tools.pretext.graph.run_graph import run_graph
    temp_output = tmp_path / "output.pretext"

    # Generate the Snakefile with print_only=True
    run_graph(
        bedgraph_file=str(test_paths["bedgraph_file"]),
        pretext_contact_map=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in the Snakefile
    assert "rule graph:" in content, "Missing rule definition in Snakefile."
    assert "input:" in content, "Missing input section in Snakefile."
    assert "output:" in content, "Missing output section in Snakefile."
    assert "wrapper:" in content, "Missing wrapper section in Snakefile."

    # Verify inputs are specified correctly
    assert f"bedgraph_file='{test_paths['bedgraph_file']}'" in content, "Missing or incorrect BEDgraph input."

    # Verify outputs are specified correctly
    assert f"pretext_contact_map='{temp_output}'" in content, "Missing or incorrect Pretext contact map output."


def test_run_graph_tool_execution(test_paths, tmp_path):
    """Test that the graph tool executes successfully with test files."""
    from tools.pretext.graph.run_graph import run_graph
    temp_output = tmp_path / "output.pretext"

    # Run the tool
    result = run_graph(
        bedgraph_file=str(test_paths["bedgraph_file"]),
        pretext_contact_map=str(temp_output)
    )

    # Verify the run was successful
    assert result.returncode == 0, "Graph tool execution failed."
    assert temp_output.exists(), "Expected output file was not created."

    # Additional checks on the output, if necessary
    assert temp_output.stat().st_size > 0, "Output file is empty."