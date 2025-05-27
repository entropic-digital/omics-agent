import pytest
from pathlib import Path
from bioinformatics_mcp.gridss.mcp.run_assemble import run_assemble

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.bam",
        "reference_genome": test_dir / "test_reference.fasta",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_assemble(test_paths, tmp_path, capsys):
    """Test that assemble generates the expected Snakefile."""
    temp_output = tmp_path / "output.vcf"

    run_assemble(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        reference_genome=str(test_paths["reference_genome"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule assemble:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper specification in Snakefile"
    assert "input_file=" in content, "Missing input_file parameter in Snakefile"
    assert "reference_genome=" in content, "Missing reference_genome parameter in Snakefile"
    assert "output_file=" in content, "Missing output_file parameter in Snakefile"

def test_run_assemble(test_paths, tmp_path):
    """Test that assemble can be run with the test files."""
    temp_output = tmp_path / "output.vcf"

    result = run_assemble(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        reference_genome=str(test_paths["reference_genome"]),
        threads=2,
        memory_limit="4G"
    )

    assert result.returncode == 0, "assemble run failed"
    assert temp_output.exists(), "Output file was not created after assemble run"