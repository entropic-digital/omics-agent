import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "vcf_file": test_dir / "input.vcf",
        "expected_snakefile": test_dir / "expected_snakefile",
        "expected_output": test_dir / "expected_output.txt",
    }

def test_snakefile_variantstotable(test_paths, tmp_path, capsys):
    """Test that variantstotable generates the expected Snakefile."""
    from tools.gatk.variantstotable import run_variantstotable
    temp_output = tmp_path / "output.txt"

    run_variantstotable(
        vcf_file=str(test_paths["vcf_file"]),
        output_file=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule variantstotable:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert f"'{test_paths['vcf_file']}'" in content, "Missing VCF input file"
    assert "output:" in content, "Missing output section"
    assert f"'{temp_output}'" in content, "Missing output file"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "file:tools/gatk/variantstotable" in content, "Missing correct wrapper path"

def test_run_variantstotable(test_paths, tmp_path):
    """Test that variantstotable can be run with the test files."""
    from tools.gatk.variantstotable import run_variantstotable
    temp_output = tmp_path / "output.txt"

    result = run_variantstotable(
        vcf_file=str(test_paths["vcf_file"]),
        output_file=str(temp_output),
    )

    assert result.returncode == 0, "variantstotable run failed"
    assert temp_output.exists(), "Output file was not created"
    with open(test_paths["expected_output"], "r") as expected, open(temp_output, "r") as output:
        assert expected.read() == output.read(), "Output content does not match the expected content"