import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "gtf_file": test_dir / "test_input.gtf",
        "gene_pred_table": test_dir / "expected_output.gp",
        "snakefile": test_dir / "Snakefile"  # Example snakefile location for capturing output
    }


def test_snakefile_gtfToGenePred(test_paths, tmp_path, capsys):
    """Test that gtfToGenePred generates the expected Snakefile."""
    from bioinformatics_mcp.ucsc.gtfToGenePred.run_gtfToGenePred import run_gtfToGenePred
    temp_output = tmp_path / "temp.gp"

    # Generate the Snakefile with print_only=True to capture the content
    run_gtfToGenePred(
        gtf_file=str(test_paths["gtf_file"]),
        gene_pred_table=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule components exist in the generated Snakefile
    assert "rule gtfToGenePred:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper directive in Snakefile"
    assert f"'{test_paths['gtf_file']}'" in content, "Missing gtf_file input in Snakefile"
    assert f"'{temp_output}'" in content, "Missing gene_pred_table output in Snakefile"


def test_run_gtfToGenePred(test_paths, tmp_path):
    """Test that gtfToGenePred runs successfully with test files."""
    from bioinformatics_mcp.ucsc.gtfToGenePred.run_gtfToGenePred import run_gtfToGenePred
    temp_output = tmp_path / "output.gp"

    result = run_gtfToGenePred(
        gtf_file=str(test_paths["gtf_file"]),
        gene_pred_table=str(temp_output),
    )

    # Verify that the process completes successfully and creates the output file
    assert result.returncode == 0, "gtfToGenePred run failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"