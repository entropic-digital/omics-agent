import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "seqs": test_dir / "test_seqs.rds",
        "refFasta": test_dir / "test_ref.fasta",
        "expected_output": test_dir / "expected_output.rds",
    }


def test_snakefile_assign_taxonomy(test_paths, tmp_path, capsys):
    """Test that assign-taxonomy generates the expected Snakefile."""
    from tools.dada2.assign_taxonomy.run_assign_taxonomy import run_assign_taxonomy

    temp_output = tmp_path / "output.rds"

    run_assign_taxonomy(
        seqs=str(test_paths["seqs"]),
        refFasta=str(test_paths["refFasta"]),
        output=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule assign-taxonomy:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "seqs=" in content, "Missing seqs input parameter"
    assert "refFasta=" in content, "Missing refFasta input parameter"
    assert f"output={str(temp_output)}" in content, "Missing output parameter path"


def test_run_assign_taxonomy(test_paths, tmp_path):
    """Test that assign-taxonomy can be run with the test files."""
    from tools.dada2.assign_taxonomy.run_assign_taxonomy import run_assign_taxonomy

    temp_output = tmp_path / "output.rds"

    result = run_assign_taxonomy(
        seqs=str(test_paths["seqs"]),
        refFasta=str(test_paths["refFasta"]),
        output=str(temp_output),
    )

    assert result.returncode == 0, "assign-taxonomy run failed"
    assert temp_output.exists(), "Output file not created"
    # Additional validation of output content can be added here if needed.