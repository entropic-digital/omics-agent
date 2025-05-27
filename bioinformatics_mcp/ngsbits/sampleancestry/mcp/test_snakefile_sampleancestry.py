import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_vcfs": test_dir / "sample.vcf",
        "expected_snakefile": test_dir / "Snakefile",
        "expected_output_tsv": test_dir / "expected_output.tsv"
    }

def test_snakefile_sampleancestry(test_paths, tmp_path, capsys):
    """Test that sampleancestry generates the expected Snakefile."""
    from bioinformatics_mcp.ngsbits.sampleancestry.run_sampleancestry import run_sampleancestry
    temp_output = tmp_path / "output.tsv"

    run_sampleancestry(
        input_vcfs=str(test_paths["input_vcfs"]),
        output_results_tsv=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule sampleancestry:" in content, "Missing Snakefile rule definition for sampleancestry"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    assert f"input_vcfs='{test_paths['input_vcfs']}'" in content, "Missing input_vcfs parameter in Snakefile"
    assert f"output_results_tsv='{temp_output}'" in content, "Missing output_results_tsv parameter in Snakefile"

def test_run_sampleancestry(test_paths, tmp_path):
    """Test that sampleancestry can be run with the provided test files."""
    from bioinformatics_mcp.ngsbits.sampleancestry.run_sampleancestry import run_sampleancestry
    temp_output = tmp_path / "output_results.tsv"

    result = run_sampleancestry(
        input_vcfs=str(test_paths["input_vcfs"]),
        output_results_tsv=str(temp_output)
    )

    assert result.returncode == 0, "sampleancestry execution failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"