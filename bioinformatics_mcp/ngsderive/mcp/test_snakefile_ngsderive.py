import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "ngs": test_dir / "test.bam",
        "gene_model": test_dir / "test.gtf",
        "expected_tsv": test_dir / "expected_output.tsv",
        "junctions": test_dir / "test_junctions",
    }


def test_snakefile_ngsderive(test_paths, tmp_path, capsys):
    """Test that ngsderive generates the expected Snakefile."""
    from bioinformatics_mcp.ngsderive.mcp.run_ngsderive import run_ngsderive
    temp_output = tmp_path / "output.tsv"

    # Generate the Snakefile with print_only=True to capture the content
    run_ngsderive(
        ngs=str(test_paths["ngs"]),
        gene_model=str(test_paths["gene_model"]),
        tsv=str(temp_output),
        subcommand="analyze",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule ngsderive:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "ngs=" in content, "Missing ngs input parameter"
    assert "gene_model=" in content, "Missing gene_model input parameter"
    assert "tsv=" in content, "Missing tsv output parameter"
    assert "subcommand=" in content, "Missing subcommand parameter"
    

def test_run_ngsderive(test_paths, tmp_path):
    """Test that ngsderive can be run with the test files."""
    from bioinformatics_mcp.ngsderive.mcp.run_ngsderive import run_ngsderive
    temp_output = tmp_path / "output.tsv"

    result = run_ngsderive(
        ngs=str(test_paths["ngs"]),
        gene_model=str(test_paths["gene_model"]),
        tsv=str(temp_output),
        subcommand="analyze",
    )

    # Verify that the run is successful
    assert result.returncode == 0, "ngsderive run failed"

    # Verify that the output file is created
    assert temp_output.exists(), "Output TSV file not created"

    # Optionally, compare output file contents if a reference expected file exists
    if test_paths["expected_tsv"].exists():
        with open(temp_output) as generated, open(test_paths["expected_tsv"]) as expected:
            assert generated.read() == expected.read(), "Output file does not match the expected results"