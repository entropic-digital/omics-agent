import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "transcriptome": test_dir / "transcriptome.fa",
        "genome": test_dir / "genome.fa",
        "gentrome": test_dir / "gentrome.fa",
        "decoys": test_dir / "decoys.txt",
    }


def test_snakefile_decoys(test_paths, tmp_path, capsys):
    """Test that the decoys tool generates the expected Snakefile."""
    from bioinformatics_mcp.salmon.decoys.run_decoys import run_decoys
    temp_gentrome = tmp_path / "gentrome.fa"
    temp_decoys = tmp_path / "decoys.txt"

    # Run with print_only=True to generate Snakefile content
    run_decoys(
        transcriptome=str(test_paths["transcriptome"]),
        genome=str(test_paths["genome"]),
        gentrome=str(temp_gentrome),
        decoys=str(temp_decoys),
        threads=1,
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Validate essential rule elements in the generated Snakefile
    assert "rule decoys:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "transcriptome=" in content, "Missing transcriptome input in Snakefile"
    assert "genome=" in content, "Missing genome input in Snakefile"
    assert "gentrome=" in content, "Missing gentrome output in Snakefile"
    assert "decoys=" in content, "Missing decoys output in Snakefile"
    assert "threads:" in content, "Missing threads parameter in Snakefile"


def test_run_decoys(test_paths, tmp_path):
    """Test that the decoys tool runs successfully with test inputs."""
    from bioinformatics_mcp.salmon.decoys.run_decoys import run_decoys
    temp_gentrome = tmp_path / "gentrome.fa"
    temp_decoys = tmp_path / "decoys.txt"

    # Execute the tool with test inputs and outputs
    result = run_decoys(
        transcriptome=str(test_paths["transcriptome"]),
        genome=str(test_paths["genome"]),
        gentrome=str(temp_gentrome),
        decoys=str(temp_decoys),
        threads=2,
    )

    # Verify that the process completes successfully
    assert result.returncode == 0, "Decoys tool run failed"
    assert temp_gentrome.exists(), "Gentrome output file not created"
    assert temp_decoys.exists(), "Decoys output file not created"