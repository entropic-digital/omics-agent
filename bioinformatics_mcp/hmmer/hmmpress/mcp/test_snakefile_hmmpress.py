import pytest
from pathlib import Path
from bioinformatics_mcp.hmmpress.mcp.run_hmmpress import run_hmmpress

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "hmm_database": test_dir / "example.hmm",
        "binary_format_hmm_database": test_dir / "example.h3m",
    }


def test_snakefile_hmmpress(test_paths, tmp_path, capsys):
    """Test that hmmpress generates the expected Snakefile."""
    temp_output = tmp_path / "example.h3m"

    # Generate the Snakefile with print_only=True to capture the content
    run_hmmpress(
        hmm_database=str(test_paths["hmm_database"]),
        binary_format_hmm_database=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule hmmpress:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify inputs from meta.yaml
    assert "hmm_database=" in content, "Missing hmm_database input in Snakefile"

    # Verify outputs from meta.yaml
    assert "binary_format_hmm_database=" in content, "Missing binary_format_hmm_database output in Snakefile"


def test_run_hmmpress(test_paths, tmp_path):
    """Test that hmmpress can be run with the test files."""
    temp_output = tmp_path / "example.h3m"

    result = run_hmmpress(
        hmm_database=str(test_paths["hmm_database"]),
        binary_format_hmm_database=str(temp_output)
    )

    # Verify that the process runs successfully
    assert result.returncode == 0, "hmmpress execution failed"

    # Verify that the expected output file is created
    assert temp_output.exists(), "Output file not created by hmmpress"