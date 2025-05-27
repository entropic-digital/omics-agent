import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "seqs": test_dir / "chimera_free_seqs.rds",
        "refFasta": test_dir / "genus_species_db.fasta",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "output": test_dir / "output.rds",
    }


def test_snakefile_assign_species(test_paths, tmp_path, capsys):
    """Test that assign-species tool generates the expected Snakefile."""
    from bioinformatics_mcp.dada2.assign_species.run_assign_species import run_assign_species

    run_assign_species(
        seqs=str(test_paths["seqs"]),
        refFasta=str(test_paths["refFasta"]),
        output=str(tmp_path / "dummy_output.rds"),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential params are present in the generated Snakefile
    assert "rule assign_species:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "seqs=" in content, "Missing seqs parameter in input"
    assert "refFasta=" in content, "Missing refFasta parameter in input"
    assert "output=" in content, "Missing output parameter"
    assert "params=" in content, "Missing params section"
    assert "thread: " in content, "Missing thread specification"


def test_run_assign_species(test_paths, tmp_path):
    """Test that assign-species tool runs successfully with test files."""
    from bioinformatics_mcp.dada2.assign_species.run_assign_species import run_assign_species

    output_path = tmp_path / "output.rds"

    result = run_assign_species(
        seqs=str(test_paths["seqs"]),
        refFasta=str(test_paths["refFasta"]),
        params={"minBoot": 50},
        output=str(output_path),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "assign-species tool execution failed"
    assert output_path.exists(), "Output file not generated"
