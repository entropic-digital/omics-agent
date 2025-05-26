import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "mcool_file": test_dir / "test.mcool",
        "phasing_track": test_dir / "test.phasing_track",
        "view": test_dir / "test.view",
        "vecs": test_dir / "output.vecs.tsv",
        "lams": test_dir / "output.lams.txt",
        "bigwig": test_dir / "output.bigwig"
    }


def test_snakefile_eigs_cis(test_paths, tmp_path, capsys):
    """Test that eigs_cis generates the expected Snakefile."""
    from tools.cooltools.eigs_cis.run_eigs_cis import run_eigs_cis

    temp_vecs = tmp_path / "output.vecs.tsv"
    temp_lams = tmp_path / "output.lams.txt"
    temp_bigwig = tmp_path / "output.bigwig"

    run_eigs_cis(
        mcool_file=str(test_paths["mcool_file"]),
        vecs=str(temp_vecs),
        lams=str(temp_lams),
        bigwig=str(temp_bigwig),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential elements in the Snakefile content
    assert "rule eigs_cis:" in content, "Missing rule definition for eigs_cis"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper declaration in Snakefile"
    assert "mcool_file=" in content, "Missing mcool_file input in Snakefile"
    assert "vecs=" in content, "Missing vecs output in Snakefile"
    assert "lams=" in content, "Missing lams output in Snakefile"
    assert "bigwig=" in content, "Missing bigwig output in Snakefile"


def test_run_eigs_cis(test_paths, tmp_path):
    """Test that eigs_cis runs successfully with test files."""
    from tools.cooltools.eigs_cis.run_eigs_cis import run_eigs_cis

    temp_vecs = tmp_path / "output.vecs.tsv"
    temp_lams = tmp_path / "output.lams.txt"
    temp_bigwig = tmp_path / "output.bigwig"

    result = run_eigs_cis(
        mcool_file=str(test_paths["mcool_file"]),
        vecs=str(temp_vecs),
        lams=str(temp_lams),
        bigwig=str(temp_bigwig)
    )

    # Verify the process completes successfully
    assert result.returncode == 0, "eigs_cis run failed"
    assert temp_vecs.exists(), "Output vecs file not generated"
    assert temp_lams.exists(), "Output lams file not generated"
    assert temp_bigwig.exists(), "Output bigwig file not generated"