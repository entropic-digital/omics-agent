import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "calls_file": test_dir / "test_calls.vcf",
        "gmt_file": test_dir / "test_annotations.gmt",
        "annotated_calls_file": test_dir / "output_annotated_calls.vcf",
    }


def test_snakefile_genesets(test_paths, tmp_path, capsys):
    """Test that the Snakefile is correctly generated for genesets."""
    from bioinformatics_mcp.snpsift.genesets.run_genesets import run_genesets

    # Temporary output for testing
    temp_output = tmp_path / "output_annotated_calls.vcf"

    # Generate the Snakefile with print_only=True
    run_genesets(
        calls_file=str(test_paths["calls_file"]),
        gmt_file=str(test_paths["gmt_file"]),
        annotated_calls_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements are present
    assert "rule genesets:" in content, "Missing 'genesets' rule definition"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper definition in Snakefile"
    assert "calls=" in content, "Missing 'calls' input parameter"
    assert "annotations=" in content, "Missing 'annotations' input parameter"
    assert "annotated_calls=" in content, "Missing 'annotated_calls' output parameter"


def test_run_genesets(test_paths, tmp_path):
    """Test the execution of the genesets tool with test files."""
    from bioinformatics_mcp.snpsift.genesets.run_genesets import run_genesets

    # Temporary output path
    temp_output = tmp_path / "output_annotated_calls.vcf"

    # Run the tool
    result = run_genesets(
        calls_file=str(test_paths["calls_file"]),
        gmt_file=str(test_paths["gmt_file"]),
        annotated_calls_file=str(temp_output),
    )

    # Assertions to verify successful execution
    assert result.returncode == 0, "genesets tool execution failed"
    assert temp_output.exists(), "Output file was not generated"
    assert temp_output.stat().st_size > 0, "Output file is empty"
