import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reference_fasta": test_dir / "reference.fasta",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "log_file": test_dir / "log.txt"
    }

def test_snakefile_index(test_paths, tmp_path, capsys):
    """Test that index generates the expected Snakefile."""
    from run_index import run_index
    temp_output_prefix = tmp_path / "output_prefix"

    # Generate the Snakefile with print_only=True to capture the content
    run_index(
        reference_fasta=str(test_paths["reference_fasta"]),
        output_prefix=str(temp_output_prefix),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential params are present in the Snakefile
    assert "rule index:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "reference_fasta=" in content, "Missing reference_fasta parameter in inputs"
    assert "output_prefix=" in content, "Missing output_prefix parameter in outputs"

def test_run_index(test_paths, tmp_path):
    """Test that index can be run with the test files."""
    from run_index import run_index
    temp_output_prefix = tmp_path / "output_prefix"

    # Execute the index function
    result = run_index(
        reference_fasta=str(test_paths["reference_fasta"]),
        output_prefix=str(temp_output_prefix),
        log_file=str(test_paths["log_file"]),
        threads=2
    )

    # Verify that the process completes successfully
    assert result.returncode == 0, "index run failed, non-zero return code"
    assert (tmp_path / "output_prefix").exists(), "Output prefix file was not generated"
    assert test_paths["log_file"].exists(), "Log file was not generated"