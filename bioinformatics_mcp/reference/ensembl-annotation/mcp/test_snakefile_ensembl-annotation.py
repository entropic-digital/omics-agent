import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.txt",
        "expected_output_file": test_dir / "expected_output.txt",
        "snakefile": test_dir / "Snakefile",
    }


def test_snakefile_ensembl_annotation(test_paths, tmp_path, capsys):
    """Test that the Snakefile for ensembl-annotation is generated as expected."""
    from bioinformatics_mcp.reference.ensembl_annotation.run_ensembl_annotation import run_ensembl_annotation

    output_file = tmp_path / "test_output.gtf"

    # Generate Snakefile with print_only=True
    run_ensembl_annotation(
        url="ftp://ftp.ensembl.org/pub",
        output_file=str(output_file),
        print_only=True,
    )

    # Capture Snakefile content
    captured = capsys.readouterr()
    snakefile_content = captured.out

    # Assert essential elements in the Snakefile
    assert "rule ensembl_annotation:" in snakefile_content, "Missing rule definition in Snakefile."
    assert "input:" in snakefile_content, "Missing input section in Snakefile."
    assert "output:" in snakefile_content, "Missing output section in Snakefile."
    assert "wrapper:" in snakefile_content, "Missing wrapper section in Snakefile."

    # Assert input and output parameters
    assert "url=" in snakefile_content, "Missing 'url' parameter in Snakefile."
    assert "output_file=" in snakefile_content, "Missing 'output_file' parameter in Snakefile."


def test_run_ensembl_annotation(test_paths, tmp_path):
    """Test that the ensembl-annotation tool runs successfully."""
    from bioinformatics_mcp.reference.ensembl_annotation.run_ensembl_annotation import run_ensembl_annotation

    output_file = tmp_path / "test_output.gtf"

    result = run_ensembl_annotation(
        url="ftp://ftp.ensembl.org/pub",
        output_file=str(output_file),
    )

    # Assert successful execution
    assert result.returncode == 0, "ensembl-annotation tool execution failed."

    # Assert output file is created
    assert output_file.exists(), "Output file was not created by ensembl-annotation."
