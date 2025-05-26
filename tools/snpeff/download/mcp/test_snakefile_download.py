import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "test_species": "test_species",
        "test_version": "test_version",
        "expected_snakefile": test_dir / "Snakefile",
        "output_dir": test_dir / "output"
    }


def test_snakefile_download(test_paths, tmp_path, capsys):
    """Test that download generates the expected Snakefile."""
    from tools.snpeff.download.run_download import run_download

    run_download(
        species=test_paths["test_species"],
        version=test_paths["test_version"],
        out_db_dir=str(tmp_path),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule download:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "params:" in content, "Missing params section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"species='{test_paths['test_species']}'" in content, "Missing species parameter"
    assert f"version='{test_paths['test_version']}'" in content, "Missing version parameter"
    assert "out_db_dir=" in content, "Missing output directory parameter"


def test_run_download(test_paths, tmp_path):
    """Test that download can be run with the test files."""
    from tools.snpeff.download.run_download import run_download

    result = run_download(
        species=test_paths["test_species"],
        version=test_paths["test_version"],
        out_db_dir=str(tmp_path)
    )

    assert result.returncode == 0, "Download run failed"
    output_files = list(Path(tmp_path).glob("**/*"))
    assert len(output_files) > 0, "No files were downloaded"
    assert any(f.suffix in [".txt", ".db", ".config"] for f in output_files), "Expected file types are missing"