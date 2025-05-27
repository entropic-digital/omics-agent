import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "input.bam",
        "reference_fasta": test_dir / "reference.fasta",
        "region_bed": test_dir / "regions.bed",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_extract(test_paths, tmp_path, capsys):
    """Test that extract generates the expected Snakefile."""
    from bioinformatics_mcp.strling.extract.mcp.run_extract import run_extract

    temp_output = tmp_path / "output.bin"

    # Generate the Snakefile with print_only=True to capture the content
    run_extract(
        input_bam=str(test_paths["input_bam"]),
        reference_fasta=str(test_paths["reference_fasta"]),
        region_bed=str(test_paths["region_bed"]),
        output_bin=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule extract:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Add assertions for all required input parameters
    assert "input_bam=" in content, "Missing input_bam parameter"
    assert "reference_fasta=" in content, "Missing reference_fasta parameter"
    if test_paths["region_bed"].exists():
        assert "region_bed=" in content, "Missing region_bed parameter"
    # Add assertions for all required output parameters
    assert "output_bin=" in content, "Missing output_bin parameter"


def test_run_extract(test_paths, tmp_path):
    """Test that extract can be run with the test files."""
    from bioinformatics_mcp.strling.extract.mcp.run_extract import run_extract

    temp_output = tmp_path / "output.bin"

    result = run_extract(
        input_bam=str(test_paths["input_bam"]),
        reference_fasta=str(test_paths["reference_fasta"]),
        region_bed=str(test_paths["region_bed"]),
        output_bin=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "extract run failed"
    # Verify that the output file is created
    assert temp_output.exists(), "Output binary file was not created"
