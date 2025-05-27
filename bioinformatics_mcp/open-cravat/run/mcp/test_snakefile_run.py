import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "tests"
    return {
        "input_vcf": test_dir / "input.vcf",
        "output_dir": test_dir / "output",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_run(test_paths, tmp_path, capsys):
    """Test that OpenCRAVAT run generates the expected Snakefile."""
    from bioinformatics_mcp.open_cravat.run.mcp.run_run import run_run
    output_dir = tmp_path / "output"

    # Generate the Snakefile with print_only=True to capture the content
    run_run(
        input_vcf=str(test_paths["input_vcf"]),
        output_dir=str(output_dir),
        assembly="hg38",
        genome=None,
        modules=None,
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule run:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "input_vcf=" in content, "Missing input_vcf parameter"
    assert "output_dir=" in content, "Missing output_dir parameter"
    assert "assembly=" in content, "Missing assembly parameter"


def test_run_run(test_paths, tmp_path):
    """Test that OpenCRAVAT run can execute with test files."""
    from bioinformatics_mcp.open_cravat.run.mcp.run_run import run_run
    output_dir = tmp_path / "output"

    result = run_run(
        input_vcf=str(test_paths["input_vcf"]),
        output_dir=str(output_dir),
        assembly="hg38",
        genome=None,
        modules=None
    )

    # Verify the run is successful
    assert result.returncode == 0, "OpenCRAVAT run execution failed"
    assert output_dir.exists(), "Output directory was not created"
    # Additional checks can be added as needed to verify specific output files
