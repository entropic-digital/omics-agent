import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "forward_reads": test_dir / "forward_reads.bam",
        "reverse_reads": test_dir / "reverse_reads.bam",
        "expected_output": test_dir / "output.sam",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_bellerophon(test_paths, tmp_path, capsys):
    """Test that bellerophon generates the expected Snakefile."""
    from bioinformatics_mcp.bellerophon.mcp.run_bellerophon import run_bellerophon
    temp_output = tmp_path / "output.sam"

    # Generate the Snakefile with print_only=True to capture the content
    run_bellerophon(
        forward_reads=str(test_paths["forward_reads"]),
        reverse_reads=str(test_paths["reverse_reads"]),
        output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule bellerophon:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify specific inputs
    assert "forward_reads=" in content, "Missing forward_reads parameter"
    assert "reverse_reads=" in content, "Missing reverse_reads parameter"

    # Verify specific output
    assert "output=" in content, "Missing output parameter"

    # Verify all required params
    assert "sort=" in content, "Missing sort parameter"
    assert "sort_extra=" in content, "Missing sort_extra parameter"
    assert "extra=" in content, "Missing extra parameter"


def test_run_bellerophon(test_paths, tmp_path):
    """Test that bellerophon can be run with the test files."""
    from bioinformatics_mcp.bellerophon.mcp.run_bellerophon import run_bellerophon
    temp_output = tmp_path / "output.sam"

    # Execute bellerophon with test data
    result = run_bellerophon(
        forward_reads=str(test_paths["forward_reads"]),
        reverse_reads=str(test_paths["reverse_reads"]),
        output=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "bellerophon run failed"

    # Verify output file is created
    assert temp_output.exists(), "Output file was not created"
