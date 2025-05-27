import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reads": test_dir / "reads.fq",
        "assembly": test_dir / "assembly.fasta",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_rebaler(test_paths, tmp_path, capsys):
    """Test that rebaler generates the expected Snakefile."""
    from bioinformatics_mcp.rebaler.run_rebaler import run_rebaler
    temp_output_dir = tmp_path / "output_dir"

    # Generate the Snakefile with print_only=True to capture the content
    run_rebaler(
        reads=str(test_paths["reads"]),
        assembly=str(test_paths["assembly"]),
        output_dir=str(temp_output_dir),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule rebaler:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "reads=" in content, "Missing reads input parameter in Snakefile"
    assert "assembly=" in content, "Missing assembly input parameter in Snakefile"
    assert "output_dir=" in content, "Missing output_dir parameter in Snakefile"


def test_run_rebaler(test_paths, tmp_path):
    """Test that rebaler can be run with the test files."""
    from bioinformatics_mcp.rebaler.run_rebaler import run_rebaler
    temp_output_dir = tmp_path / "output_dir"

    # Run rebaler with test inputs
    result = run_rebaler(
        reads=str(test_paths["reads"]),
        assembly=str(test_paths["assembly"]),
        output_dir=str(temp_output_dir)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "rebaler run failed"
    
    # Check if output folder is created
    assert temp_output_dir.exists(), "Output directory was not created"
    
    # Verify that expected output files exist
    output_files = ["final_assembly.fasta", "log.txt"]
    for file in output_files:
        output_file = temp_output_dir / file
        assert output_file.exists(), f"Expected output file {file} is missing"