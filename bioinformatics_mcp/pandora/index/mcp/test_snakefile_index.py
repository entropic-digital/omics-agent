import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "prg_file": test_dir / "test_prg.ext",
        "expected_index": test_dir / "expected_index.ext",
        "kmer_prgs_dir": test_dir / "expected_kmer_prgs",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_index(test_paths, tmp_path, capsys):
    """Test that pandora index generates the expected Snakefile."""
    from bioinformatics_mcp.pandora.index.run_index import run_index

    run_index(
        prg_file=str(test_paths["prg_file"]),
        index=str(tmp_path / "out_index.ext"),
        kmer_prgs=str(tmp_path / "out_kmer_prgs"),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule index:" in content, "Missing 'rule index' definition in Snakefile"
    assert "input:" in content, "Missing 'input' section in Snakefile"
    assert "output:" in content, "Missing 'output' section in Snakefile"
    assert "wrapper:" in content, "Missing 'wrapper' directive in Snakefile"
    assert "prg_file=" in content, "Missing 'prg_file' in input parameters"
    assert "index=" in content, "Missing 'index' in output parameters"
    assert "kmer_prgs=" in content, "Missing 'kmer_prgs' in output parameters"


def test_run_index(test_paths, tmp_path):
    """Test that pandora index can be run with the test files."""
    from bioinformatics_mcp.pandora.index.run_index import run_index

    output_index = tmp_path / "output_index.ext"
    output_kmer_prgs = tmp_path / "output_kmer_prgs"

    result = run_index(
        prg_file=str(test_paths["prg_file"]),
        index=str(output_index),
        kmer_prgs=str(output_kmer_prgs)
    )

    assert result.returncode == 0, "Pandora index run failed"
    assert output_index.exists(), "Output index file was not created"
    assert output_kmer_prgs.exists(), "Output kmer PRGs directory was not created"