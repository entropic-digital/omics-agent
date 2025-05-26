import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "fasta": test_dir / "test.fasta",
        "meryldb": test_dir / "test.meryl",
        "meryldb_parents": test_dir / "test_parents.meryl",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_merqury(test_paths, tmp_path, capsys):
    """Test that the merqury Snakefile is generated correctly."""
    from tools.merqury.mcp.run_merqury import run_merqury

    # Generate the Snakefile with print_only=True to capture the output
    run_merqury(
        fasta=str(test_paths["fasta"]),
        meryldb=str(test_paths["meryldb"]),
        meryldb_parents=str(test_paths["meryldb_parents"]),
        output_dir=str(tmp_path),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule components are present
    assert "rule merqury:" in content, "Missing rule definition in Snakefile."
    assert "input:" in content, "Missing input section in Snakefile."
    assert "output:" in content, "Missing output section in Snakefile."
    assert "wrapper:" in content, "Missing wrapper section in Snakefile."

    # Verify required inputs
    assert "fasta=" in content, "Missing 'fasta' input parameter in Snakefile."
    assert "meryldb=" in content, "Missing 'meryldb' input parameter in Snakefile."
    if "meryldb_parents" in test_paths:
        assert "meryldb_parents=" in content, "Missing 'meryldb_parents' input parameter in Snakefile."

    # Verify output directory
    assert "output_dir=" in content, "Missing 'output_dir' output parameter in Snakefile."


def test_run_merqury(test_paths, tmp_path):
    """Test that the merqury tool runs successfully with test inputs."""
    from tools.merqury.mcp.run_merqury import run_merqury

    output_dir = tmp_path / "output"

    # Run the tool
    result = run_merqury(
        fasta=str(test_paths["fasta"]),
        meryldb=str(test_paths["meryldb"]),
        meryldb_parents=str(test_paths["meryldb_parents"]),
        output_dir=str(output_dir)
    )

    # Verify successful execution
    assert result.returncode == 0, "Merqury execution failed; non-zero return code."

    # Verify that output files are created as expected
    # Example: Check for essential PNG file as per the tool notes
    png_files = list(output_dir.glob("*.png"))
    assert len(png_files) > 0, "No PNG files generated in the output directory."
