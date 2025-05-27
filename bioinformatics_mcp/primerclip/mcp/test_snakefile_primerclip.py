"""Module that tests if the primerclip Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "sam_file": test_dir / "input.sam",
        "master_primer_file": test_dir / "master_primers.txt",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "output_sam_file": test_dir / "output.sam",
    }


def test_snakefile_primerclip(test_paths, tmp_path, capsys):
    """Test that primerclip generates the expected Snakefile."""
    from bioinformatics_mcp.primerclip.mcp.run_primerclip import run_primerclip

    temp_output = tmp_path / "output.sam"

    # Generate the Snakefile with print_only=True to capture the content
    run_primerclip(
        sam_file=str(test_paths["sam_file"]),
        master_primer_file=str(test_paths["master_primer_file"]),
        output_sam_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule primerclip:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Add assertions for all required input parameters
    assert "sam_file=" in content, "Missing sam_file input parameter"
    assert "master_primer_file=" in content, (
        "Missing master_primer_file input parameter"
    )
    # Add assertions for all required output parameters
    assert "output_sam_file=" in content, "Missing output_sam_file parameter"


def test_run_primerclip(test_paths, tmp_path):
    """Test that primerclip can be run with the test files."""
    from bioinformatics_mcp.primerclip.mcp.run_primerclip import run_primerclip

    temp_output = tmp_path / "output.sam"

    # Run primerclip tool
    result = run_primerclip(
        sam_file=str(test_paths["sam_file"]),
        master_primer_file=str(test_paths["master_primer_file"]),
        output_sam_file=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "primerclip run failed"

    # Verify output file exists
    assert temp_output.exists(), f"Expected output file {temp_output} was not created"
