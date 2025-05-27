import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "cmfile": test_dir / "test.cm",  # Input covariance model file
        "expected_output_dir": test_dir / "expected_output",  # Expected output directory
    }


def test_snakefile_cmpress(test_paths, tmp_path, capsys):
    """Test that cmpress generates the expected Snakefile."""
    from bioinformatics_mcp.infernal.cmpress.run_cmpress import run_cmpress

    # Generate the Snakefile with print_only=True to capture the content
    run_cmpress(
        cmfile=str(test_paths["cmfile"]),
        output_dir=str(tmp_path),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in the generated Snakefile
    assert "rule cmpress:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f"cmfile={str(test_paths['cmfile'])}" in content, "Missing cmfile input in Snakefile"
    assert f"output_dir={str(tmp_path)}" in content, "Missing output_dir parameter in Snakefile"


def test_run_cmpress(test_paths, tmp_path):
    """Test that cmpress can be executed with the test files."""
    from bioinformatics_mcp.infernal.cmpress.run_cmpress import run_cmpress

    # Run the cmpress tool
    result = run_cmpress(
        cmfile=str(test_paths["cmfile"]),
        output_dir=str(tmp_path)
    )

    # Verify that the command executed successfully
    assert result.returncode == 0, "cmpress execution failed"

    # Verify that expected output files were generated
    expected_files = ["test.cm.i1m", "test.cm.i1p", "test.cm.i1f", "test.cm.i1i"]
    for file in expected_files:
        assert (tmp_path / file).exists(), f"Missing expected output file: {file}"