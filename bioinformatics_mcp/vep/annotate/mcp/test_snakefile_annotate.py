import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_vcf": test_dir / "input.vcf",
        "output_vcf": test_dir / "output.vcf",
        "cache_dir": test_dir / "vep_cache",
        "expected_snakefile": test_dir / "expected_snakefile.txt",
    }

def test_snakefile_annotate(test_paths, tmp_path, capsys):
    """Test that annotate generates the expected Snakefile."""
    from run_annotate import run_annotate

    temp_output = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True
    run_annotate(
        input_vcf=str(test_paths["input_vcf"]),
        output_vcf=str(temp_output),
        cache_dir=str(test_paths["cache_dir"]),
        species="homo_sapiens",
        assembly="GRCh38",
        offline=True,
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule annotate:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "input_vcf=" in content, "Missing input_vcf parameter"
    assert "output_vcf=" in content, "Missing output_vcf parameter"
    assert "cache_dir=" in content, "Missing cache_dir parameter"
    assert "species=" in content, "Missing species parameter"
    assert "assembly=" in content, "Missing assembly parameter"

def test_run_annotate(test_paths, tmp_path):
    """Test that annotate can be run successfully with test files."""
    from run_annotate import run_annotate

    temp_output = tmp_path / "output.vcf"

    result = run_annotate(
        input_vcf=str(test_paths["input_vcf"]),
        output_vcf=str(temp_output),
        cache_dir=str(test_paths["cache_dir"]),
        species="homo_sapiens",
        assembly="GRCh38",
        offline=True,
    )

    # Verify that the tool runs successfully
    assert result.returncode == 0, "Tool execution failed"
    assert temp_output.exists(), "Output VCF file was not generated"