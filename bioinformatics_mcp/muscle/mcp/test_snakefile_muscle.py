import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fasta_file": test_dir / "test.fasta",
        "expected_alignment_file": test_dir / "expected_alignment.fasta",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_muscle(test_paths, tmp_path, capsys):
    """Test that muscle generates the expected Snakefile."""
    from bioinformatics_mcp.muscle.mcp.run_muscle import run_muscle
    temp_alignment = tmp_path / "alignment.fasta"

    # Generate the Snakefile with print_only=True to capture the content
    run_muscle(
        fasta_file=str(test_paths["fasta_file"]),
        alignment_file=str(temp_alignment),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements
    assert "rule muscle:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "fasta_file=" in content, "Missing fasta_file parameter in Snakefile"
    assert "alignment_file=" in content, "Missing alignment_file parameter in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"


def test_run_muscle(test_paths, tmp_path):
    """Test that muscle can be run with the test files."""
    from bioinformatics_mcp.muscle.mcp.run_muscle import run_muscle
    temp_alignment = tmp_path / "alignment.fasta"

    result = run_muscle(
        fasta_file=str(test_paths["fasta_file"]),
        alignment_file=str(temp_alignment)
    )

    # Verify that the process completed successfully
    assert result.returncode == 0, "muscle run failed"

    # Verify that the output alignment file is created
    assert temp_alignment.exists(), "Output alignment file was not created"
    assert temp_alignment.stat().st_size > 0, "Output alignment file is empty"