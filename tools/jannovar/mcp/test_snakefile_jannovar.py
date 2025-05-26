import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_files"
    return {
        "input_vcf": base_dir / "test_input.vcf",
        "db_path": base_dir / "jannovar_db.ser",
        "expected_snakefile": base_dir / "expected_Snakefile",
        "output_vcf": base_dir / "output_annotated.vcf",
        "output_json": base_dir / "output_data.json",
    }


def test_snakefile_jannovar(test_paths, tmp_path, capsys):
    """Test that the jannovar Snakefile is generated correctly."""
    from tools.jannovar.run_jannovar import run_jannovar

    run_jannovar(
        input_vcf=str(test_paths["input_vcf"]),
        db_path=str(test_paths["db_path"]),
        output_vcf="output_annotated_sample.vcf",
        output_json="output_data_sample.json",
        print_only=True,
    )

    captured = capsys.readouterr()
    generated_snakefile = captured.out

    assert "rule jannovar:" in generated_snakefile, "Missing rule definition"
    assert "input:" in generated_snakefile, "Missing input section"
    assert "output:" in generated_snakefile, "Missing output section"
    assert "wrapper:" in generated_snakefile, "Missing wrapper section"
    assert "input_vcf=" in generated_snakefile, "Missing input_vcf parameter"
    assert "db_path=" in generated_snakefile, "Missing db_path parameter"
    assert "output_vcf=" in generated_snakefile, "Missing output_vcf parameter"
    assert "output_json=" in generated_snakefile, "Missing output_json parameter"


def test_run_jannovar(test_paths, tmp_path):
    """Test that jannovar runs successfully with the provided test files."""
    from tools.jannovar.run_jannovar import run_jannovar

    output_vcf = tmp_path / "output_annotated.vcf"
    output_json = tmp_path / "output_data.json"

    result = run_jannovar(
        input_vcf=str(test_paths["input_vcf"]),
        db_path=str(test_paths["db_path"]),
        output_vcf=str(output_vcf),
        output_json=str(output_json),
    )

    assert result.returncode == 0, "Jannovar execution failed"
    assert output_vcf.exists(), "Output VCF file was not created"
    assert output_json.exists(), "Output JSON file was not created"