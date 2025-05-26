import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "aln": test_dir / "sample.bam",
        "fai": test_dir / "sample.fasta.fai",
        "html": test_dir / "output.html",
        "bed": test_dir / "output.bed",
        "ped": test_dir / "output.ped",
        "roc": test_dir / "output.roc",
    }


def test_snakefile_indexcov(test_paths, tmp_path, capsys):
    """Test that indexcov generates the expected Snakefile."""
    from tools.goleft.indexcov.mcp.run_indexcov import run_indexcov

    # Generate the Snakefile with print_only=True to capture the content
    run_indexcov(
        aln=str(test_paths["aln"]),
        fai=str(test_paths["fai"]),
        html=str(test_paths["html"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the Snakefile
    assert "rule indexcov:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "aln=" in content, "Missing aln input parameter"
    assert "fai=" in content, "Missing fai input parameter"
    assert "html=" in content, "Missing html output parameter"
    assert "file:tools/goleft/indexcov" in content, "Missing correct wrapper path"


def test_run_indexcov(test_paths, tmp_path):
    """Test that indexcov can be run with the provided test files."""
    from tools.goleft.indexcov.mcp.run_indexcov import run_indexcov

    # Define the output paths
    html_output = tmp_path / "output.html"
    bed_output = tmp_path / "output.bed"
    ped_output = tmp_path / "output.ped"
    roc_output = tmp_path / "output.roc"

    # Run the indexcov tool
    result = run_indexcov(
        aln=str(test_paths["aln"]),
        fai=str(test_paths["fai"]),
        html=str(html_output),
        bed=str(bed_output),
        ped=str(ped_output),
        roc=str(roc_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "indexcov run failed"
    assert html_output.exists(), "HTML output file not created"
    assert bed_output.exists(), "BED output file not created"
    assert ped_output.exists(), "PED output file not created"
    assert roc_output.exists(), "ROC output file not created"
