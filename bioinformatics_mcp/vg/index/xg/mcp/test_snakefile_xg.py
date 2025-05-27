import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "variation_graph": test_dir / "test_graph.vg",
        "output_xg": test_dir / "expected_output.xg",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_xg(test_paths, tmp_path, capsys):
    """Test that xg generates the expected Snakefile."""
    from bioinformatics_mcp.vg.index.xg.run_xg import run_xg
    temp_output = tmp_path / "output.xg"

    # Generate the Snakefile with print_only=True to capture the content
    run_xg(
        variation_graph=str(test_paths["variation_graph"]),
        output_xg=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential parameters are present
    assert "rule xg:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify inputs
    assert "variation_graph=" in content, "Missing variation_graph input"
    
    # Verify outputs
    assert "output_xg=" in content, "Missing output_xg output"
    

def test_run_xg(test_paths, tmp_path):
    """Test that xg can be run with the test files."""
    from bioinformatics_mcp.vg.index.xg.run_xg import run_xg
    temp_output = tmp_path / "output.xg"

    result = run_xg(
        variation_graph=str(test_paths["variation_graph"]),
        output_xg=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "xg run failed"
    assert temp_output.exists(), "Output file not created"
