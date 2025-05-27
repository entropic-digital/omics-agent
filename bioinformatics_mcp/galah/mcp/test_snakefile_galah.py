import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fasta1": test_dir / "test_fasta1.fasta",
        "fasta2": test_dir / "test_fasta2.fasta",
        "clusters": test_dir / "test_clusters.txt",
        "repres": test_dir / "test_repres_dir",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_galah(test_paths, tmp_path, capsys):
    """Test that galah generates the expected Snakefile."""
    from bioinformatics_mcp.galah.mcp.run_galah import run_galah

    temp_clusters = tmp_path / "clusters.txt"
    temp_repres = tmp_path / "repres"

    # Generate the Snakefile with print_only=True to capture the content
    run_galah(
        fasta_files=[str(test_paths["fasta1"]), str(test_paths["fasta2"])],
        clusters=str(temp_clusters),
        repres=str(temp_repres),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out.strip()

    # Verify the essential params are present
    assert "rule galah:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify input files are correctly specified
    assert "fasta_files=" in content, "Missing fasta_files parameter in Snakefile"

    # Verify output files are correctly specified
    assert "clusters=" in content, "Missing clusters output in Snakefile"
    assert "repres=" in content, "Missing repres output in Snakefile"

    # Verify the wrapper path is included
    assert "wrapper: \"file:tools/galah\"" in content, "Incorrect or missing wrapper path"


def test_run_galah(test_paths, tmp_path):
    """Test that galah can be run with the test files."""
    from bioinformatics_mcp.galah.mcp.run_galah import run_galah

    temp_clusters = tmp_path / "clusters.txt"
    temp_repres = tmp_path / "repres_dir"
    temp_repres.mkdir(parents=True, exist_ok=True)

    # Run the galah tool
    result = run_galah(
        fasta_files=[str(test_paths["fasta1"]), str(test_paths["fasta2"])],
        clusters=str(temp_clusters),
        repres=str(temp_repres),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "GALAH tool execution failed"

    # Verify that the expected outputs are generated
    assert temp_clusters.exists(), "Clusters output file not created"
    assert temp_repres.exists() and any(temp_repres.iterdir()), "Repres output directory not populated"