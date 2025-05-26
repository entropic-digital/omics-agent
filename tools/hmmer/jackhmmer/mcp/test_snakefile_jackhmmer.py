import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "query": test_dir / "query.fasta",
        "db": test_dir / "db.fasta",
        "expected_hits_tbl": test_dir / "expected.hits_tbl",
        "expected_hits_aln": test_dir / "expected.hits_aln",
        "expected_dom_tbl": test_dir / "expected.dom_tbl",
        "expected_summary": test_dir / "expected.summary"
    }


def test_snakefile_jackhmmer(test_paths, tmp_path, capsys):
    """Test that jackhmmer generates the expected Snakefile."""
    from tools.hmmer.jackhmmer.run_jackhmmer import run_jackhmmer

    temp_hits_tbl = tmp_path / "hits_tbl.txt"
    temp_hits_aln = tmp_path / "hits_aln.sto"
    temp_dom_tbl = tmp_path / "dom_tbl.txt"
    temp_summary = tmp_path / "summary.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_jackhmmer(
        query=str(test_paths["query"]),
        db=str(test_paths["db"]),
        hits_tbl=str(temp_hits_tbl),
        hits_aln=str(temp_hits_aln),
        dom_tbl=str(temp_dom_tbl),
        summary=str(temp_summary),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule jackhmmer:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "query=" in content, "Missing query parameter"
    assert "db=" in content, "Missing db parameter"
    assert "output:" in content, "Missing output section"
    assert "hits_tbl=" in content, "Missing hits_tbl parameter"
    assert "hits_aln=" in content, "Missing hits_aln parameter"
    assert "dom_tbl=" in content, "Missing dom_tbl parameter"
    assert "summary=" in content, "Missing summary parameter"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "file:tools/hmmer/jackhmmer" in content, "Missing wrapper path"


def test_run_jackhmmer(test_paths, tmp_path):
    """Test that jackhmmer can be run with the test files."""
    from tools.hmmer.jackhmmer.run_jackhmmer import run_jackhmmer

    temp_hits_tbl = tmp_path / "hits_tbl.txt"
    temp_hits_aln = tmp_path / "hits_aln.sto"
    temp_dom_tbl = tmp_path / "dom_tbl.txt"
    temp_summary = tmp_path / "summary.txt"

    result = run_jackhmmer(
        query=str(test_paths["query"]),
        db=str(test_paths["db"]),
        hits_tbl=str(temp_hits_tbl),
        hits_aln=str(temp_hits_aln),
        dom_tbl=str(temp_dom_tbl),
        summary=str(temp_summary)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "jackhmmer run failed"

    # Verify output files are created
    assert temp_hits_tbl.exists(), "hits_tbl file was not created"
    assert temp_hits_aln.exists(), "hits_aln file was not created"
    assert temp_dom_tbl.exists(), "dom_tbl file was not created"
    assert temp_summary.exists(), "summary file was not created"