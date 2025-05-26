import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fasta": test_dir / "test.fasta",
        "expected_output_prefix": test_dir / "expected_output",
    }

def test_snakefile_index(test_paths, tmp_path, capsys):
    """Test that hisat2 index generates the expected Snakefile."""
    from tools.hisat2.index.run_index import run_index

    temp_output_prefix = tmp_path / "output"
    run_index(
        sequence=[str(test_paths["fasta"])],
        output=[str(temp_output_prefix) + ".ht2"],
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule index:" in content, "Missing rule definition for index"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f"input: '{test_paths['fasta']}'" in content, "Missing input FASTA in Snakefile"
    assert f"output: '{str(temp_output_prefix)}.ht2'" in content, "Missing output file in Snakefile"

def test_run_index(test_paths, tmp_path):
    """Test that hisat2 index runs successfully with test files."""
    from tools.hisat2.index.run_index import run_index

    temp_output_prefix = tmp_path / "output"
    result = run_index(
        sequence=[str(test_paths["fasta"])],
        output=[str(temp_output_prefix) + ".ht2"]
    )

    assert result.returncode == 0, "Indexing run failed"
    for ext in [".1.ht2", ".2.ht2", ".3.ht2", ".4.ht2", ".5.ht2", ".6.ht2", ".7.ht2", ".8.ht2"]:
        assert (temp_output_prefix.with_suffix(ext)).exists(), f"Output file {ext} was not generated"