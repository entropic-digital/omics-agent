import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "cpg_context_file": test_dir / "CpG_context_sample.txt.gz",
        "chg_context_file": test_dir / "CHG_context_sample.txt.gz",
        "chh_context_file": test_dir / "CHH_context_sample.txt.gz",
        "expected_bedGraph": test_dir / "output_sample.bedGraph.gz",
        "expected_cov": test_dir / "output_sample.bismark.cov.gz",
    }


def test_snakefile_bismark2bedGraph(test_paths, tmp_path, capsys):
    """Test that bismark2bedGraph generates the expected Snakefile."""
    from tools.bismark.bismark2bedGraph.run_bismark2bedGraph import run_bismark2bedGraph

    temp_bedGraph = tmp_path / "output.bedGraph.gz"
    temp_cov = tmp_path / "output.bismark.cov.gz"

    run_bismark2bedGraph(
        cpg_context_file=str(test_paths["cpg_context_file"]),
        chg_context_file=str(test_paths["chg_context_file"]),
        chh_context_file=str(test_paths["chh_context_file"]),
        bedGraph=str(temp_bedGraph),
        cov=str(temp_cov),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule bismark2bedGraph:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    assert "cpg_context_file=" in content, "Missing cpg_context_file input in Snakefile"
    assert "chg_context_file=" in content, "Missing chg_context_file input in Snakefile"
    assert "chh_context_file=" in content, "Missing chh_context_file input in Snakefile"

    assert "bedGraph=" in content, "Missing bedGraph output in Snakefile"
    assert "cov=" in content, "Missing cov output in Snakefile"


def test_run_bismark2bedGraph(test_paths, tmp_path):
    """Test that bismark2bedGraph can be run with the test files."""
    from tools.bismark.bismark2bedGraph.run_bismark2bedGraph import run_bismark2bedGraph

    temp_bedGraph = tmp_path / "output.bedGraph.gz"
    temp_cov = tmp_path / "output.bismark.cov.gz"

    result = run_bismark2bedGraph(
        cpg_context_file=str(test_paths["cpg_context_file"]),
        chg_context_file=str(test_paths["chg_context_file"]),
        chh_context_file=str(test_paths["chh_context_file"]),
        bedGraph=str(temp_bedGraph),
        cov=str(temp_cov),
    )

    assert result.returncode == 0, "bismark2bedGraph execution failed"
    assert temp_bedGraph.exists(), "Output bedGraph file was not created"
    assert temp_cov.exists(), "Output cov file was not created"