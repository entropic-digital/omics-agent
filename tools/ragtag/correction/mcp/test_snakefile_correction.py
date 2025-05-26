import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "ref": test_dir / "reference.fasta",
        "query": test_dir / "query.fasta",
        "fasta": test_dir / "corrected.fasta",
        "agp": test_dir / "corrected.agp",
    }


def test_snakefile_correction(test_paths, tmp_path, capsys):
    """Test that Snakefile for correction tool is generated correctly."""
    from tools.ragtag.correction.run_correction import run_correction

    # Generate the Snakefile with print_only=True
    run_correction(
        ref=str(test_paths["ref"]),
        query=str(test_paths["query"]),
        fasta=str(test_paths["fasta"]),
        agp=str(test_paths["agp"]),
        print_only=True,
    )

    # Capture the generated content
    captured = capsys.readouterr()
    content = captured.out

    # Assertions to verify essential rule components
    assert "rule correction:" in content, "Missing rule definition for correction"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    
    # Verify all inputs
    assert "ref=" in content, "Missing 'ref' input parameter in Snakefile"
    assert "query=" in content, "Missing 'query' input parameter in Snakefile"
    
    # Verify all outputs
    assert "fasta=" in content, "Missing 'fasta' output parameter in Snakefile"
    assert "agp=" in content, "Missing 'agp' output parameter in Snakefile"

    # Verify wrapper path
    assert "file:tools/ragtag/correction" in content, "Incorrect wrapper path"


def test_run_correction(test_paths, tmp_path):
    """Test that correction tool runs successfully with provided inputs."""
    from tools.ragtag.correction.run_correction import run_correction

    temp_fasta = tmp_path / "corrected_output.fasta"
    temp_agp = tmp_path / "corrected_output.agp"

    # Run the correction tool
    result = run_correction(
        ref=str(test_paths["ref"]),
        query=str(test_paths["query"]),
        fasta=str(temp_fasta),
        agp=str(temp_agp),
    )

    # Verify successful execution
    assert result.returncode == 0, "Correction tool failed to execute successfully"
    
    # Verify outputs are generated
    assert temp_fasta.exists(), f"Expected output FASTA file {temp_fasta} not created"
    assert temp_agp.exists(), f"Expected output AGP file {temp_agp} not created"