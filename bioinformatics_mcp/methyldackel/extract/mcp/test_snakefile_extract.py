import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).resolve().parent.parent
    test_dir = base_dir / "test"
    return {
        "ref": test_dir / "reference.fasta",
        "aln": test_dir / "aligned.bam",
        "cpg": test_dir / "cpg.bedGraph",
        "chg": test_dir / "chg.bedGraph",
        "chh": test_dir / "chh.bedGraph",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_extract(test_paths, tmp_path, capsys):
    """Test that extract generates the expected Snakefile."""
    from run_extract import run_extract

    temp_output_cpg = tmp_path / "output_cpg.bedGraph"
    temp_output_chg = tmp_path / "output_chg.bedGraph"
    temp_output_chh = tmp_path / "output_chh.bedGraph"

    # Generate the Snakefile with print_only=True to capture the content
    run_extract(
        ref=str(test_paths["ref"]),
        aln=str(test_paths["aln"]),
        cpg=str(temp_output_cpg),
        chg=str(temp_output_chg),
        chh=str(temp_output_chh),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule extract:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "ref=" in content, "Missing ref parameter"
    assert "aln=" in content, "Missing aln parameter"
    assert "cpg=" in content, "Missing cpg parameter"
    assert "chg=" in content, "Missing chg parameter"
    assert "chh=" in content, "Missing chh parameter"
    assert "file:tools/methyldackel/extract" in content, "Incorrect wrapper path"


def test_run_extract(test_paths, tmp_path):
    """Test that extract can be run with the test files."""
    from run_extract import run_extract

    temp_output_cpg = tmp_path / "output_cpg.bedGraph"
    temp_output_chg = tmp_path / "output_chg.bedGraph"
    temp_output_chh = tmp_path / "output_chh.bedGraph"

    result = run_extract(
        ref=str(test_paths["ref"]),
        aln=str(test_paths["aln"]),
        cpg=str(temp_output_cpg),
        chg=str(temp_output_chg),
        chh=str(temp_output_chh),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "extract run failed"

    # Verify that output files are generated
    assert temp_output_cpg.exists(), "Output CpG metrics file not generated"
    assert temp_output_chg.exists(), "Output CHG metrics file not generated"
    assert temp_output_chh.exists(), "Output CHH metrics file not generated"
