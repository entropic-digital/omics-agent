import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_files"
    return {
        "tool_base_url": "ftp://ftp.ensembl.org/pub",  # Default base URL
        "test_output_file": base_dir / "test_output.gff3",  # Output file path
        "expected_snakefile": base_dir / "Snakefile",  # Expected Snakefile location
    }


def test_snakefile_ensembl_regulation(test_paths, tmp_path, capsys):
    """Test that ensembl-regulation generates the expected Snakefile."""
    from bioinformatics_mcp.reference.ensembl_regulation.run_ensembl_regulation import run_ensembl_regulation

    temp_output_file = tmp_path / "temp_output.gff3"

    # Generate the Snakefile with print_only=True to capture content
    run_ensembl_regulation(
        url=test_paths["tool_base_url"],
        output_file=str(temp_output_file),
        print_only=True,
    )

    # Capture printed Snakefile content
    captured = capsys.readouterr()
    snakefile_content = captured.out

    # Verify essential Snakefile elements
    assert "rule ensembl_regulation:" in snakefile_content, "Missing rule definition"
    assert "input:" in snakefile_content, "Missing input section"
    assert "output:" in snakefile_content, "Missing output section"
    assert "params:" in snakefile_content, "Missing params section for URL"
    assert "wrapper:" in snakefile_content, "Missing wrapper section"

    # Validate specific expected parameters
    assert "output_file=" in snakefile_content, "Missing 'output_file' parameter"
    assert test_paths["tool_base_url"] in snakefile_content, "Missing default URL in params"


def test_run_ensembl_regulation(test_paths, tmp_path):
    """Test that ensembl-regulation can be executed with the test files."""
    from bioinformatics_mcp.reference.ensembl_regulation.run_ensembl_regulation import run_ensembl_regulation

    temp_output_file = tmp_path / "produced_output.gff3"

    # Execute the tool and verify its success
    result = run_ensembl_regulation(
        url=test_paths["tool_base_url"],
        output_file=str(temp_output_file)
    )

    # Assert the Snakemake workflow completed successfully
    assert result.returncode == 0, "ensembl-regulation execution failed"

    # Validate output file is created
    assert temp_output_file.exists(), "Output file was not created"
    assert temp_output_file.stat().st_size > 0, "Output file is empty"