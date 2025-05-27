import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "input.bam",
        "reference_fasta": test_dir / "reference.fasta",
        "output_vcf": test_dir / "output.vcf",
        "log_file": test_dir / "log.txt",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_call_call(test_paths, tmp_path, capsys):
    """Test that call generates the expected Snakefile."""
    from bioinformatics_mcp.gridss.call.run_call import run_call

    temp_output_vcf = tmp_path / "output.vcf"

    run_call(
        input_bam=str(test_paths["input_bam"]),
        reference_fasta=str(test_paths["reference_fasta"]),
        output_vcf=str(temp_output_vcf),
        log_file=str(test_paths["log_file"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule call:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "input_bam=" in content, "Missing input_bam parameter"
    assert "reference_fasta=" in content, "Missing reference_fasta parameter"
    assert "output_vcf=" in content, "Missing output_vcf parameter"


def test_run_call_call(test_paths, tmp_path):
    """Test that the call tool can execute with test files."""
    from bioinformatics_mcp.gridss.call.run_call import run_call

    temp_output_vcf = tmp_path / "output.vcf"

    result = run_call(
        input_bam=str(test_paths["input_bam"]),
        reference_fasta=str(test_paths["reference_fasta"]),
        output_vcf=str(temp_output_vcf),
        log_file=str(test_paths["log_file"])
    )

    assert result.returncode == 0, "call tool execution failed"
    assert temp_output_vcf.exists(), "Output VCF file was not created"