import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "f1r2": [test_dir / "test_f1r2_1.tar.gz", test_dir / "test_f1r2_2.tar.gz"],  # Example test files
        "expected_snakefile": test_dir / "Snakefile",  # Path to expected Snakefile location
    }


def test_snakefile_learnreadorientationmodel(test_paths, tmp_path, capsys):
    """Test that learnreadorientationmodel generates the expected Snakefile."""
    from tools.gatk.learnreadorientationmodel.run_learnreadorientationmodel import run_learnreadorientationmodel
    temp_output = tmp_path / "artifact_prior_tables.tar.gz"

    # Generate the Snakefile with print_only=True to capture the content
    run_learnreadorientationmodel(
        f1r2=[str(fp) for fp in test_paths["f1r2"]],
        output=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    snakefile_content = captured.out

    # Verify essential rule elements in the Snakefile
    assert "rule learnreadorientationmodel:" in snakefile_content, "Missing rule definition in Snakefile"
    assert "input:" in snakefile_content, "Missing input section in Snakefile"
    assert "output:" in snakefile_content, "Missing output section in Snakefile"
    assert "wrapper:" in snakefile_content, "Missing wrapper section in Snakefile"

    # Verify input file presence in the Snakefile
    for f1r2_path in test_paths["f1r2"]:
        assert str(f1r2_path) in snakefile_content, f"Missing input file path: {f1r2_path}"

    # Verify output file presence in the Snakefile
    assert str(temp_output) in snakefile_content, "Missing output file path in Snakefile"

    # Verify presence of the wrapper reference
    assert "file:tools/gatk/learnreadorientationmodel" in snakefile_content, "Missing wrapper reference in Snakefile"


def test_run_learnreadorientationmodel(test_paths, tmp_path):
    """Test that learnreadorientationmodel can be run with the test files."""
    from tools.gatk.learnreadorientationmodel.run_learnreadorientationmodel import run_learnreadorientationmodel

    temp_output = tmp_path / "artifact_prior_tables.tar.gz"

    # Execute the tool
    result = run_learnreadorientationmodel(
        f1r2=[str(fp) for fp in test_paths["f1r2"]],
        output=str(temp_output),
    )

    # Verify the run was successful
    assert result.returncode == 0, "learnreadorientationmodel run failed"
    assert temp_output.exists(), "Expected output file was not generated"
