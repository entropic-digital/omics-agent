import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reference_genome": test_dir / "reference_genome.fasta",
        "expected_snakefile": test_dir / "expected_Snakefile"
    }

def test_snakefile_prepare_reference(test_paths, tmp_path, capsys):
    """Test that prepare-reference generates the expected Snakefile."""
    from tools.rsem.prepare_reference.mcp.run_prepare_reference import run_prepare_reference
    temp_output = tmp_path / "output"

    # Generate the Snakefile with print_only=True to capture the content
    run_prepare_reference(
        reference_genome=str(test_paths["reference_genome"]),
        print_only=True,
        output_dir=str(temp_output)
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule prepare_reference:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "reference_genome=" in content, "Missing reference_genome input parameter"

def test_run_prepare_reference(test_paths, tmp_path):
    """Test that prepare-reference can be run with the test files."""
    from tools.rsem.prepare_reference.mcp.run_prepare_reference import run_prepare_reference
    temp_output = tmp_path / "output"

    # Run the tool with the test files
    result = run_prepare_reference(
        reference_genome=str(test_paths["reference_genome"]),
        output_dir=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "prepare-reference run failed"
    assert (tmp_path / "output").exists(), "Output directory not created"