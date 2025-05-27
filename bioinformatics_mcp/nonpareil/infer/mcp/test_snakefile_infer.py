"""Module that tests if the infer Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reads": test_dir / "reads.fq.gz",
        "redund_sum": test_dir / "redundancy_summary.tsv",
        "redund_val": test_dir / "redundancy_values.tsv",
        "mate_distr": test_dir / "mate_distribution.txt",
        "log": test_dir / "process.log",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_infer(test_paths, tmp_path, capsys):
    """Test that infer generates the expected Snakefile."""
    from bioinformatics_mcp.nonpareil.infer.run_infer import run_infer

    temp_redund_sum = tmp_path / "redund_sum.tsv"
    temp_redund_val = tmp_path / "redund_val.tsv"
    temp_mate_distr = tmp_path / "mate_distr.txt"
    temp_log = tmp_path / "log.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_infer(
        reads=str(test_paths["reads"]),
        redund_sum=str(temp_redund_sum),
        redund_val=str(temp_redund_val),
        mate_distr=str(temp_mate_distr),
        log=str(temp_log),
        alg="kmer",
        infer_X=True,
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule and sections are present
    assert "rule infer:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify required inputs
    assert "reads=" in content, "Missing reads input parameter"

    # Verify required outputs
    assert "redund_sum=" in content, "Missing redund_sum output parameter"
    assert "redund_val=" in content, "Missing redund_val output parameter"
    assert "mate_distr=" in content, "Missing mate_distr output parameter"
    assert "log=" in content, "Missing log output parameter"

    # Verify required params
    assert "alg=" in content, "Missing alg param"
    assert "infer_X=" in content, "Missing infer_X param"

    # Verify known additional wrapper details
    assert "wrapper=" in content, "Missing wrapper path"


def test_run_infer(test_paths, tmp_path):
    """Test that infer can be run with the test files."""
    from bioinformatics_mcp.nonpareil.infer.run_infer import run_infer

    temp_redund_sum = tmp_path / "redund_sum.tsv"
    temp_redund_val = tmp_path / "redund_val.tsv"
    temp_mate_distr = tmp_path / "mate_distr.txt"
    temp_log = tmp_path / "log.txt"

    # Run the tool
    result = run_infer(
        reads=str(test_paths["reads"]),
        redund_sum=str(temp_redund_sum),
        redund_val=str(temp_redund_val),
        mate_distr=str(temp_mate_distr),
        log=str(temp_log),
        alg="kmer",
        infer_X=True,
    )

    # Verify that the run is successful
    assert result.returncode == 0, "infer run failed"

    # Verify that output files are created
    assert temp_redund_sum.exists(), "Missing redund_sum output file"
    assert temp_redund_val.exists(), "Missing redund_val output file"
    assert temp_mate_distr.exists(), "Missing mate_distr output file"
    assert temp_log.exists(), "Missing log output file"
