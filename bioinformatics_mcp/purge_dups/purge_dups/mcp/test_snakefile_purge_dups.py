import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_paf": test_dir / "test_input.paf",
        "output_bed": test_dir / "test_output.bed",
    }


def test_snakefile_purge_dups(test_paths, tmp_path, capsys):
    """Test that purge_dups generates the expected Snakefile."""
    from bioinformatics_mcp.purge_dups.mcp.run_purge_dups import run_purge_dups
    temp_output = tmp_path / "output.bed"

    # Generate Snakefile with print_only=True to capture content
    run_purge_dups(
        input_paf=str(test_paths["input_paf"]),
        output_bed=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    # Verify essential params in the Snakefile
    assert "rule purge_dups:" in content, "Missing rule definition for purge_dups"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f"'{str(test_paths['input_paf'])}'" in content, "Missing input_paf parameter in Snakefile"
    assert f"'{str(temp_output)}'" in content, "Missing output_bed parameter in Snakefile"


def test_run_purge_dups(test_paths, tmp_path):
    """Test that purge_dups can be run with the test files."""
    from bioinformatics_mcp.purge_dups.mcp.run_purge_dups import run_purge_dups
    temp_output = tmp_path / "output.bed"

    result = run_purge_dups(
        input_paf=str(test_paths["input_paf"]),
        output_bed=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "purge_dups execution failed"
    assert temp_output.exists(), "Output BED file was not created"