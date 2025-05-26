import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "ref": test_dir / "test_ref.fasta",
        "agps": test_dir / "test_agps.agp",
        "bam": test_dir / "test_bam.bam",        # Optional in meta.yaml
        "fasta": test_dir / "expected_output.fasta",
        "agp": test_dir / "expected_output.agp",
        "links": test_dir / "expected_links.txt" # Optional in meta.yaml
    }

def test_snakefile_merge(test_paths, tmp_path, capsys):
    """Test that merge generates the expected Snakefile."""
    from tools.ragtag.merge.run_merge import run_merge

    temp_fasta = tmp_path / "output.fasta"
    temp_agp = tmp_path / "output.agp"

    # Generate the Snakefile with print_only=True to capture the content
    run_merge(
        ref=str(test_paths["ref"]),
        agps=str(test_paths["agps"]),
        fasta=str(temp_fasta),
        agp=str(temp_agp),
        bam=str(test_paths["bam"]),  # Optional, include for testing
        links=str(test_paths["links"]),  # Optional, include for testing
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assertions for Snakefile structure
    assert "rule merge:" in content, "Missing rule definition for merge"
    assert "input:" in content, "Missing input section for merge rule"
    assert "output:" in content, "Missing output section for merge rule"
    assert "wrapper:" in content, "Missing wrapper section for merge rule"

    # Assertions for required inputs as per meta.yaml
    assert "ref=" in content, "Missing 'ref' input parameter in Snakefile"
    assert "agps=" in content, "Missing 'agps' input parameter in Snakefile"
    if "bam=" in content:
        assert "bam=" in content, "Missing 'bam' optional parameter in Snakefile"

    # Assertions for required outputs as per meta.yaml
    assert "fasta=" in content, "Missing 'fasta' output parameter in Snakefile"
    assert "agp=" in content, "Missing 'agp' output parameter in Snakefile"
    if "links=" in content:
        assert "links=" in content, "Missing 'links' optional parameter in Snakefile"

def test_run_merge(test_paths, tmp_path):
    """Test that merge can be run with the test files."""
    from tools.ragtag.merge.run_merge import run_merge

    temp_fasta = tmp_path / "output.fasta"
    temp_agp = tmp_path / "output.agp"

    result = run_merge(
        ref=str(test_paths["ref"]),
        agps=str(test_paths["agps"]),
        fasta=str(temp_fasta),
        agp=str(temp_agp),
        bam=str(test_paths["bam"]),  # Optional, include for testing
        links=str(test_paths["links"])  # Optional, include for testing
    )

    # Verify that the run is successful
    assert result.returncode == 0, "merge tool execution failed"
    assert temp_fasta.exists(), "Output FASTA file was not generated"
    assert temp_agp.exists(), "Output AGP file was not generated"