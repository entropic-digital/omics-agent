import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "graph": test_dir / "test_graph.vg",
        "gbwt": test_dir / "test_gbwt.gbwt",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_gcsa(test_paths, tmp_path, capsys):
    """Test that gcsa generates the expected Snakefile."""
    from tools.vg.index.gcsa.run_gcsa import run_gcsa

    temp_gcsa = tmp_path / "output.gcsa"
    temp_lcp = tmp_path / "output.lcp"

    # Generate the Snakefile with print_only=True to capture the content
    run_gcsa(
        graph=str(test_paths["graph"]),
        gbwt=str(test_paths["gbwt"]),
        out_gcsa=str(temp_gcsa),
        out_lcp=str(temp_lcp),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule components in the Snakefile
    assert "rule gcsa:" in content, "Missing rule definition for gcsa"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper definition in Snakefile"

    # Verify all required input parameters from meta.yaml
    assert "graph=" in content, "Missing 'graph' input parameter"
    assert "gbwt=" in content, "Missing 'gbwt' input parameter"

    # Verify all required output parameters from meta.yaml
    assert "out_gcsa=" in content, "Missing 'out_gcsa' output parameter"
    assert "out_lcp=" in content, "Missing 'out_lcp' output parameter"

    # Verify additional essential parameters
    assert "kmer_size=" in content, "Missing 'kmer_size' parameter"
    assert "doubling_steps=" in content, "Missing 'doubling_steps' parameter"


def test_run_gcsa(test_paths, tmp_path):
    """Test that gcsa can be run with the test files."""
    from tools.vg.index.gcsa.run_gcsa import run_gcsa

    temp_gcsa = tmp_path / "output.gcsa"
    temp_lcp = tmp_path / "output.lcp"

    # Run the gcsa tool with test inputs
    result = run_gcsa(
        graph=str(test_paths["graph"]),
        gbwt=str(test_paths["gbwt"]),
        out_gcsa=str(temp_gcsa),
        out_lcp=str(temp_lcp),
        kmer_size=16,
        doubling_steps=2,
    )

    # Verify that the run is successful
    assert result.returncode == 0, "GCSA tool execution failed"

    # Verify that the output files were created
    assert temp_gcsa.exists(), f"Expected output GCSA file not created: {temp_gcsa}"
    assert temp_lcp.exists(), f"Expected output LCP file not created: {temp_lcp}"