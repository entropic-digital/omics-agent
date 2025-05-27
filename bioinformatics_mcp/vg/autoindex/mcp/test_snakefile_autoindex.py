import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "ref": test_dir / "test_ref.fasta",
        "vcf": test_dir / "test_haplotypes.vcf",
        "gbz": test_dir / "test_output.giraffe.gbz",
        "dist": test_dir / "test_output.dist",
        "min_idx": test_dir / "test_output.shortread.withzip.min",
        "zipcodes": test_dir / "test_output.shortread.zipcodes",
        "snakefile_expected": test_dir / "expected_snakefile"
    }

def test_snakefile_autoindex(test_paths, tmp_path, capsys):
    """Test that autoindex generates the expected Snakefile."""
    from bioinformatics_mcp.vg.autoindex.run_autoindex import run_autoindex

    # Generate the Snakefile with print_only=True
    run_autoindex(
        ref=str(test_paths["ref"]),
        vcf=str(test_paths["vcf"]),
        gbz=str(test_paths["gbz"]),
        dist=str(test_paths["dist"]),
        min_idx=str(test_paths["min_idx"]),
        zipcodes=str(test_paths["zipcodes"]),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify critical elements in the Snakefile
    assert "rule autoindex:" in content, "Snakefile missing rule definition"
    assert "input:" in content, "Snakefile missing input section"
    assert "output:" in content, "Snakefile missing output section"
    assert "wrapper:" in content, "Snakefile missing wrapper section"
    assert "ref=" in content, "Snakefile missing required input 'ref'"
    assert "gbz=" in content, "Snakefile missing required output 'gbz'"
    assert "dist=" in content, "Snakefile missing required output 'dist'"
    assert "min_idx=" in content, "Snakefile missing required output 'min_idx'"
    assert "zipcodes=" in content, "Snakefile missing required output 'zipcodes'"

def test_run_autoindex(test_paths, tmp_path):
    """Test that autoindex can be run with the test files."""
    from bioinformatics_mcp.vg.autoindex.run_autoindex import run_autoindex

    # Run the autoindex tool with required test inputs
    result = run_autoindex(
        ref=str(test_paths["ref"]),
        vcf=str(test_paths["vcf"]),
        gbz=str(test_paths["gbz"]),
        dist=str(test_paths["dist"]),
        min_idx=str(test_paths["min_idx"]),
        zipcodes=str(test_paths["zipcodes"])
    )

    # Assert that the process has completed successfully
    assert result.returncode == 0, "autoindex run failed"
    assert test_paths["gbz"].exists(), "Expected GBZ file was not created"
    assert test_paths["dist"].exists(), "Expected Distance index file was not created"
    assert test_paths["min_idx"].exists(), "Expected Minimizer index file was not created"
    assert test_paths["zipcodes"].exists(), "Expected Zipcodes file was not created"