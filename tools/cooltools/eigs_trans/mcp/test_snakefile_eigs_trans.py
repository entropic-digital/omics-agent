import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "mcool_file": test_dir / "test.mcool",
        "phasing_track": test_dir / "phasing_track.tsv",
        "vecs": test_dir / "output_vecs.tsv",
        "lams": test_dir / "output_lams.txt",
        "bigwig": test_dir / "output.bigwig"
    }

def test_snakefile_eigs_trans(test_paths, tmp_path, capsys):
    """Test that eigs_trans generates the expected Snakefile."""
    from tools.cooltools.eigs_trans.run_eigs_trans import run_eigs_trans

    run_eigs_trans(
        mcool_file=str(test_paths["mcool_file"]),
        vecs="temp_vecs.tsv",
        lams="temp_lams.txt",
        bigwig="temp.bigwig",
        phasing_track=str(test_paths["phasing_track"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule eigs_trans:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "mcool_file=" in content, "Missing mcool_file parameter"
    assert "vecs=" in content, "Missing vecs parameter"
    assert "lams=" in content, "Missing lams parameter"
    assert "bigwig=" in content, "Missing bigwig parameter"
    assert "phasing_track=" in content, "Missing phasing_track parameter"

def test_run_eigs_trans(test_paths, tmp_path):
    """Test that eigs_trans can be run with the test files."""
    from tools.cooltools.eigs_trans.run_eigs_trans import run_eigs_trans

    vecs_output = tmp_path / "output_vecs.tsv"
    lams_output = tmp_path / "output_lams.txt"
    bigwig_output = tmp_path / "output.bigwig"

    result = run_eigs_trans(
        mcool_file=str(test_paths["mcool_file"]),
        vecs=str(vecs_output),
        lams=str(lams_output),
        bigwig=str(bigwig_output),
        phasing_track=str(test_paths["phasing_track"])
    )

    assert result.returncode == 0, "eigs_trans run failed"
    assert vecs_output.exists(), "Vecs output file not created"
    assert lams_output.exists(), "Lams output file not created"
    assert bigwig_output.exists(), "BigWig output file not created"