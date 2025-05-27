import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "taxa": test_dir / "test_taxa.rds",
        "refFasta": test_dir / "test_reference.fasta",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_add_species(test_paths, tmp_path, capsys):
    """Test that add-species generates the expected Snakefile."""
    from bioinformatics_mcp.dada2.add_species.run_add_species import run_add_species

    temp_output = tmp_path / "output.rds"

    # Generate the Snakefile with print_only=True to capture the content
    run_add_species(
        taxa=str(test_paths["taxa"]),
        refFasta=str(test_paths["refFasta"]),
        params={},
        output=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements
    assert "rule add-species:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Verify inputs
    assert "taxa=" in content, "Missing taxa input parameter"
    assert "refFasta=" in content, "Missing refFasta input parameter"
    # Verify outputs
    assert "output=" in content, "Missing output parameter"


def test_run_add_species(test_paths, tmp_path):
    """Test that add-species can be run with the test files."""
    from bioinformatics_mcp.dada2.add_species.run_add_species import run_add_species

    temp_output = tmp_path / "output.rds"

    result = run_add_species(
        taxa=str(test_paths["taxa"]),
        refFasta=str(test_paths["refFasta"]),
        params={},
        output=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "add-species run failed"
    # Verify the output file is generated
    assert temp_output.exists(), "Output file was not created"