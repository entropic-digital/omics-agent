import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "vcf": test_dir / "test.vcf",
        "db_config": test_dir / "test_db.yaml",
        "var_config": test_dir / "test_var.yaml",
        "bed": test_dir / "test.bed",
        "output_res": test_dir / "output_res.txt",
        "vcf_output": test_dir / "output_vcf.txt"
    }


def test_snakefile_pytmb(test_paths, tmp_path, capsys):
    """Test that pytmb generates the expected Snakefile."""
    from tools.tmb.pytmb.run_pytmb import run_pytmb

    run_pytmb(
        vcf=str(test_paths["vcf"]),
        db_config=str(test_paths["db_config"]),
        var_config=str(test_paths["var_config"]),
        bed=str(test_paths["bed"]),
        res=str(test_paths["output_res"]),
        vcf_output=str(test_paths["vcf_output"]),
        print_only=True
    )
    captured = capsys.readouterr()
    content = captured.out

    assert "rule pytmb:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f"vcf='{str(test_paths['vcf'])}'" in content, "Missing vcf input in Snakefile"
    assert f"db_config='{str(test_paths['db_config'])}'" in content, "Missing db_config input in Snakefile"
    assert f"var_config='{str(test_paths['var_config'])}'" in content, "Missing var_config input in Snakefile"
    assert f"bed='{str(test_paths['bed'])}'" in content, "Missing bed input in Snakefile"
    assert f"res='{str(test_paths['output_res'])}'" in content, "Missing primary output in Snakefile"
    assert f"vcf='{str(test_paths['vcf_output'])}'" in content, "Missing vcf_output in Snakefile"


def test_run_pytmb(test_paths, tmp_path):
    """Test that pytmb can be run with the test files."""
    from tools.tmb.pytmb.run_pytmb import run_pytmb

    temp_res_output = tmp_path / "output_res.txt"
    temp_vcf_output = tmp_path / "output_vcf.txt"

    result = run_pytmb(
        vcf=str(test_paths["vcf"]),
        db_config=str(test_paths["db_config"]),
        var_config=str(test_paths["var_config"]),
        bed=str(test_paths["bed"]),
        res=str(temp_res_output),
        vcf_output=str(temp_vcf_output)
    )

    assert result.returncode == 0, "pytmb execution failed"
    assert temp_res_output.exists(), "Result output file was not created"
    assert temp_vcf_output.exists(), "VCF output file was not created"