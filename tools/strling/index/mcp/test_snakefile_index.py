import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reference_genome": test_dir / "reference.fasta",
        "expected_bed": test_dir / "expected_output.bed",
        "output_bed": test_dir / "output.bed",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_index(test_paths, tmp_path, capsys):
    """Test that STRling index generates the expected Snakefile."""
    from run_index import run_index
    temp_output = tmp_path / "output.bed"

    # Generate the Snakefile with print_only=True to capture the content
    run_index(
        reference_genome=str(test_paths["reference_genome"]),
        output_bed=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule index:" in content, "Missing rule definition for 'index'"
    assert "input:" in content, "Missing 'input' section in Snakefile"
    assert "output:" in content, "Missing 'output' section in Snakefile"
    assert "wrapper:" in content, "Missing 'wrapper' section in Snakefile"
    # Add assertions for all required input/output parameters
    assert "reference_genome=" in content, "Missing 'reference_genome' parameter"
    assert "output_bed=" in content, "Missing 'output_bed' parameter"
    assert "threads=" in content, "Missing 'threads' parameter"


def test_run_index(test_paths, tmp_path):
    """Test that STRling index can be run with test files."""
    from run_index import run_index
    temp_output = tmp_path / "output.bed"

    result = run_index(
        reference_genome=str(test_paths["reference_genome"]),
        output_bed=str(temp_output),
        threads=1
    )

    # Verify that the run is successful
    assert result.returncode == 0, "STRling index run failed"
    # Verify that the output file is created
    assert temp_output.exists(), "Output BED file was not created"
    # Optionally compare the output with an expected result if needed
    expected_content = test_paths["expected_bed"].read_text()
    generated_content = temp_output.read_text()
    assert generated_content == expected_content, "Output BED content does not match expected"