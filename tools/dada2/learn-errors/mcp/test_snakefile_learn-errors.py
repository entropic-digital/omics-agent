import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"  # Assuming test files are in "test_files" folder
    return {
        "input_files": [
            test_dir / f"input{i}.fastq" for i in range(1, 3)
        ],  # Example input FASTQ files
        "expected_snakefile": test_dir / "expected_Snakefile",
        "temp_err": test_dir / "temp_err.rds",
        "temp_plot": test_dir / "temp_plot.pdf",
    }


def test_snakefile_learn_errors(test_paths, tmp_path, capsys):
    """Test that learn-errors generates the expected Snakefile."""
    from tools.dada2.learn_errors.run_learn_errors import run_learn_errors

    # Run with print_only=True to generate Snakefile without executing
    run_learn_errors(
        input_files=[str(path) for path in test_paths["input_files"]],
        err=str(tmp_path / "temp_err.rds"),
        plot=str(tmp_path / "temp_plot.pdf"),
        print_only=True,
    )

    # Capture printed Snakefile content
    captured = capsys.readouterr()
    snakefile_content = captured.out

    # Verify essential Snakefile elements
    assert "rule learn_errors:" in snakefile_content, (
        "Missing 'learn_errors' rule definition"
    )
    assert "input:" in snakefile_content, "Missing input section"
    assert "output:" in snakefile_content, "Missing output section"
    assert "params:" in snakefile_content, "Missing params section"
    assert "wrapper:" in snakefile_content, "Missing wrapper section"
    assert "input_files=" in snakefile_content, "Missing 'input_files' parameter"
    assert "err=" in snakefile_content, "Missing 'err' output parameter"
    assert "plot=" in snakefile_content, "Missing 'plot' output parameter"
    assert "tools/dada2/learn-errors" in snakefile_content, (
        "Missing correct wrapper for learn-errors"
    )


def test_run_learn_errors(test_paths, tmp_path):
    """Test execution of learn-errors using test files."""
    from tools.dada2.learn_errors.run_learn_errors import run_learn_errors

    # Temporary output paths
    temp_err = tmp_path / "temp_err.rds"
    temp_plot = tmp_path / "temp_plot.pdf"

    # Execute the learn-errors tool
    result = run_learn_errors(
        input_files=[str(path) for path in test_paths["input_files"]],
        err=str(temp_err),
        plot=str(temp_plot),
    )

    # Verify process executed successfully
    assert result.returncode == 0, "learn-errors execution failed"
    # Ensure output files are created
    assert temp_err.exists(), f"Output file {temp_err} was not created"
    assert temp_plot.exists(), f"Output file {temp_plot} was not created"
