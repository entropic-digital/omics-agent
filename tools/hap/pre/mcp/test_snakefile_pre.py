import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_vcf": test_dir / "input.vcf",
        "ref_file": test_dir / "reference.fasta",
        "ref_index": test_dir / "reference.fasta.fai",
        "expected_snakefile": test_dir / "Snakefile",
    }

def test_snakefile_pre(test_paths, tmp_path, capsys):
    """Test that pre.py generates the expected Snakefile."""
    from tools.hap.py.pre import run_pre
    temp_output = tmp_path / "output.vcf"

    run_pre(
        input_vcf=str(test_paths["input_vcf"]),
        output_vcf=str(temp_output),
        ref_file=str(test_paths["ref_file"]),
        ref_index=str(test_paths["ref_index"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule pre:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "input_vcf=" in content, "Missing input_vcf parameter"
    assert "ref_file=" in content, "Missing ref_file parameter"
    assert "ref_index=" in content, "Missing ref_index parameter"
    assert "output_vcf=" in content, "Missing output_vcf parameter"

def test_run_pre(test_paths, tmp_path):
    """Test that pre.py can be run with the test files."""
    from tools.hap.py.pre import run_pre
    temp_output = tmp_path / "output.vcf"

    result = run_pre(
        input_vcf=str(test_paths["input_vcf"]),
        output_vcf=str(temp_output),
        ref_file=str(test_paths["ref_file"]),
        ref_index=str(test_paths["ref_index"])
    )

    assert result.returncode == 0, "pre.py run failed"
    assert temp_output.exists(), "Output file was not created"