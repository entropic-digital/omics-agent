import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "ref": test_dir / "ref.fasta",
        "query": test_dir / "query.fasta",
        "fasta": test_dir / "output_patched.fasta",
        "agp": test_dir / "output_patched.agp",
    }


def test_snakefile_patch(test_paths, tmp_path, capsys):
    """Test that ragtag_patch generates the expected Snakefile."""
    from tools.ragtag.mcp.run_patch import run_patch
    temp_output_fasta = tmp_path / "output.fasta"
    temp_output_agp = tmp_path / "output.agp"

    # Generate the Snakefile with print_only=True to capture the content
    run_patch(
        ref=str(test_paths["ref"]),
        query=str(test_paths["query"]),
        fasta=str(temp_output_fasta),
        agp=str(temp_output_agp),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule patch:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    
    # Verify that required parameters are included as inputs
    assert "ref=" in content, "Missing ref parameter in input"
    assert "query=" in content, "Missing query parameter in input"

    # Verify the required outputs
    assert "fasta=" in content, "Missing fasta parameter in output"
    assert "agp=" in content, "Missing agp parameter in output"


def test_run_patch(test_paths, tmp_path):
    """Test that ragtag_patch can be run with the test files."""
    from tools.ragtag.mcp.run_patch import run_patch
    temp_output_fasta = tmp_path / "output.fasta"
    temp_output_agp = tmp_path / "output.agp"

    result = run_patch(
        ref=str(test_paths["ref"]),
        query=str(test_paths["query"]),
        fasta=str(temp_output_fasta),
        agp=str(temp_output_agp)
    )

    # Verify successful execution
    assert result.returncode == 0, "ragtag_patch run failed"

    # Verify the output files are created
    assert temp_output_fasta.exists(), "Output FASTA file not created"
    assert temp_output_agp.exists(), "Output AGP file not created"