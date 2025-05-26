import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "npo_files": [test_dir / "test1.npo", test_dir / "test2.npo"],
        "pdf_output": test_dir / "test_output.pdf",
        "tsv_output": test_dir / "test_output.tsv",
        "json_output": test_dir / "test_output.json",
    }


def test_snakefile_plot(test_paths, tmp_path, capsys):
    """Test that the plot tool generates the expected Snakefile."""
    from tools.nonpareil.plot.run_plot import run_plot

    run_plot(
        npo_files=[str(path) for path in test_paths["npo_files"]],
        pdf_output=str(tmp_path / "output.pdf"),
        tsv_output=str(tmp_path / "output.tsv"),
        json_output=str(tmp_path / "output.json"),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule plot:" in content, "Missing rule definition in Snakefile."
    assert "input:" in content, "Missing input section in Snakefile."
    assert "output:" in content, "Missing output section in Snakefile."
    assert "wrapper:" in content, "Missing wrapper section in Snakefile."
    assert "npo_files=" in content, "Missing 'npo_files' parameter in Snakefile."
    assert "--pdf" in content, "Missing '--pdf' argument in Snakefile."
    assert "--tsv" in content, "Missing '--tsv' argument in Snakefile."
    assert "--json" in content, "Missing '--json' argument in Snakefile."


def test_run_plot(test_paths, tmp_path):
    """Test that the plot tool executes successfully with test files."""
    from tools.nonpareil.plot.run_plot import run_plot

    result = run_plot(
        npo_files=[str(path) for path in test_paths["npo_files"]],
        pdf_output=str(tmp_path / "output.pdf"),
        tsv_output=str(tmp_path / "output.tsv"),
        json_output=str(tmp_path / "output.json"),
    )

    assert result.returncode == 0, "Plot tool execution failed."
    assert (tmp_path / "output.pdf").exists(), "PDF output file was not created."
    assert (tmp_path / "output.tsv").exists(), "TSV output file was not created."
    assert (tmp_path / "output.json").exists(), "JSON output file was not created."