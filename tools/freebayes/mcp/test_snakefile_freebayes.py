import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input1": test_dir / "test_input1.bam",
        "reference_genome": test_dir / "test_reference.fasta",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "expected_output": test_dir / "expected_output.vcf",
    }


def test_snakefile_freebayes(test_paths, tmp_path, capsys):
    """Test that freebayes generates the expected Snakefile."""
    from tools.freebayes.mcp.run_freebayes import run_freebayes
    temp_output = tmp_path / "test_output.vcf"

    run_freebayes(
        input_files=[str(test_paths["input1"])],
        reference_genome=str(test_paths["reference_genome"]),
        output_file=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule freebayes:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f"input_files={test_paths['input1']}" in content, "Missing input files parameter"
    assert f"reference_genome={test_paths['reference_genome']}" in content, "Missing reference genome parameter"
    assert f"output_file={temp_output}" in content, "Missing output file parameter"
    assert "params:" in content, "Missing params section in Snakefile"


def test_run_freebayes(test_paths, tmp_path):
    """Test that freebayes can be run with the test files."""
    from tools.freebayes.mcp.run_freebayes import run_freebayes
    temp_output = tmp_path / "test_output.vcf"

    result = run_freebayes(
        input_files=[str(test_paths["input1"])],
        reference_genome=str(test_paths["reference_genome"]),
        output_file=str(temp_output)
    )

    assert result.returncode == 0, "freebayes run failed"
    assert temp_output.exists(), "Output file was not created"
    # Verify content matches expectations if required
    with open(temp_output, 'r') as output, open(test_paths['expected_output'], 'r') as expected:
        assert output.readlines() == expected.readlines(), "Output content does not match expected results"