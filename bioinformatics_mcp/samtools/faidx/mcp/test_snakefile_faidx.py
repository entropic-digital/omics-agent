"""Module that tests if the faidx Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reference_sequence_file": test_dir / "reference.fa",
        "regions_file": test_dir / "regions.bed",
        "output_fai": test_dir / "reference.fa.fai",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_faidx(test_paths, tmp_path, capsys):
    """Test that faidx generates the expected Snakefile."""
    from bioinformatics_mcp.samtools.faidx.run_faidx import run_faidx

    # Generate the Snakefile with print_only=True to capture the content
    run_faidx(
        reference_sequence_file=str(test_paths["reference_sequence_file"]),
        regions=str(test_paths["regions_file"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule faidx:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Add assertions for all required inputs from meta.yaml
    assert "reference_sequence_file=" in content, (
        "Missing reference_sequence_file parameter in input"
    )
    assert "regions=" in content, "Missing regions parameter in input"

    # Add assertions for output
    assert "fai=" in content, "Missing fai output parameter"


def test_run_faidx(test_paths, tmp_path):
    """Test that faidx can be run with the test files."""
    from bioinformatics_mcp.samtools.faidx.run_faidx import run_faidx

    temp_fai_output = tmp_path / "reference.fa.fai"

    result = run_faidx(
        reference_sequence_file=str(test_paths["reference_sequence_file"]),
        regions=str(test_paths["regions_file"]),
        fai=str(temp_fai_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "faidx run failed"

    # Verify that the expected output file was created
    assert temp_fai_output.exists(), "Expected FAI output file was not created"
    assert temp_fai_output.stat().st_size > 0, "FAI output file is empty"
