import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "vg_graph": test_dir / "test_graph.vg",
        "mapping_file": test_dir / "test_mapping.map",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_prune(test_paths, tmp_path, capsys):
    """Test that prune generates the expected Snakefile."""
    from bioinformatics_mcp.vg.prune.run_prune import run_prune
    temp_output = tmp_path / "output_graph.vg"

    # Generate the Snakefile with print_only=True to capture the content
    run_prune(
        vg_graph=str(test_paths["vg_graph"]),
        output_graph=str(temp_output),
        mapping_file=str(test_paths["mapping_file"]),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule prune:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Check specific inputs and outputs
    assert "vg_graph=" in content, "Missing 'vg_graph' input parameter"
    assert "output_graph=" in content, "Missing 'output_graph' output parameter"
    assert "threads=" in content, "Missing 'threads' parameter in params section"

    # Optional mapping file should also be included
    if test_paths["mapping_file"].exists():
        assert "mapping_file=" in content, "Missing 'mapping_file' parameter in params section"


def test_run_prune(test_paths, tmp_path):
    """Test that prune can be run with the test files."""
    from bioinformatics_mcp.vg.prune.run_prune import run_prune
    temp_output = tmp_path / "output_graph.vg"

    result = run_prune(
        vg_graph=str(test_paths["vg_graph"]),
        output_graph=str(temp_output),
        mapping_file=str(test_paths["mapping_file"]),
        threads=2
    )

    # Verify that the run is successful
    assert result.returncode == 0, "prune execution failed"
    assert temp_output.exists(), "Output graph file was not created"
