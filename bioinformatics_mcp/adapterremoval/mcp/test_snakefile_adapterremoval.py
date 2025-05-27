import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_files"
    return {
        "sample": base_dir / "sample.fastq.gz",
        "fq": base_dir / "output.fq.gz",
        "fq1": base_dir / "output_R1.fq.gz",
        "fq2": base_dir / "output_R2.fq.gz",
        "singleton": base_dir / "singleton.fq.gz",
        "collapsed": base_dir / "collapsed.fq.gz",
        "collapsed_trunc": base_dir / "collapsed_trunc.fq.gz",
        "discarded": base_dir / "discarded.fq.gz",
        "settings": base_dir / "settings.txt",
    }


def test_snakefile_adapterremoval(test_paths, tmp_path, capsys):
    """Test that adapterremoval generates the expected Snakefile."""
    from bioinformatics_mcp.adapterremoval.mcp.run_adapterremoval import run_adapterremoval

    run_adapterremoval(
        sample=str(test_paths["sample"]),
        fq=str(test_paths["fq"]),
        fq1=str(test_paths["fq1"]),
        fq2=str(test_paths["fq2"]),
        singleton=str(test_paths["singleton"]),
        collapsed=str(test_paths["collapsed"]),
        collapsed_trunc=str(test_paths["collapsed_trunc"]),
        discarded=str(test_paths["discarded"]),
        settings=str(test_paths["settings"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule adapterremoval:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    assert "sample=" in content, "Missing sample input parameter in Snakefile"
    assert "fq=" in content, "Missing fq output parameter in Snakefile"
    assert "fq1=" in content, "Missing fq1 output parameter in Snakefile"
    assert "fq2=" in content, "Missing fq2 output parameter in Snakefile"
    assert "singleton=" in content, "Missing singleton output parameter in Snakefile"
    assert "collapsed=" in content, "Missing collapsed output parameter in Snakefile"
    assert (
        "collapsed_trunc=" in content
    ), "Missing collapsed_trunc output parameter in Snakefile"
    assert "discarded=" in content, "Missing discarded output parameter in Snakefile"
    assert "settings=" in content, "Missing settings output parameter in Snakefile"


def test_run_adapterremoval(test_paths, tmp_path):
    """Test that adapterremoval can be run with the test files."""
    from bioinformatics_mcp.adapterremoval.mcp.run_adapterremoval import run_adapterremoval

    fq_temp = tmp_path / "output.fq.gz"
    fq1_temp = tmp_path / "output_R1.fq.gz"
    fq2_temp = tmp_path / "output_R2.fq.gz"
    singleton_temp = tmp_path / "singleton.fq.gz"
    collapsed_temp = tmp_path / "collapsed.fq.gz"
    collapsed_trunc_temp = tmp_path / "collapsed_trunc.fq.gz"
    discarded_temp = tmp_path / "discarded.fq.gz"
    settings_temp = tmp_path / "settings.txt"

    result = run_adapterremoval(
        sample=str(test_paths["sample"]),
        fq=str(fq_temp),
        fq1=str(fq1_temp),
        fq2=str(fq2_temp),
        singleton=str(singleton_temp),
        collapsed=str(collapsed_temp),
        collapsed_trunc=str(collapsed_trunc_temp),
        discarded=str(discarded_temp),
        settings=str(settings_temp),
    )

    assert result.returncode == 0, "Adapterremoval execution failed"
    assert fq_temp.exists(), "Output fq file not generated"
    assert fq1_temp.exists(), "Output fq1 file not generated"
    assert fq2_temp.exists(), "Output fq2 file not generated"
    assert singleton_temp.exists(), "Output singleton file not generated"
    assert collapsed_temp.exists(), "Output collapsed file not generated"
    assert (
        collapsed_trunc_temp.exists()
    ), "Output collapsed_trunc file not generated"
    assert discarded_temp.exists(), "Output discarded file not generated"
    assert settings_temp.exists(), "Output settings file not generated"