import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "vcf_input": test_dir / "test_input.vcf",
        "annotation_vcf": test_dir / "annotation_input.vcf",
        "expected_snakefile": test_dir / "Snakefile",
        "output_vcf": test_dir / "output.vcf",
    }


def test_snakefile_annotate(test_paths, tmp_path, capsys):
    """Test that the annotate tool generates the expected Snakefile."""
    from run_annotate import run_annotate

    temp_output = tmp_path / "output.vcf"

    run_annotate(
        vcf_input=str(test_paths["vcf_input"]),
        annotation_vcf=str(test_paths["annotation_vcf"]),
        output_vcf=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule annotate:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "vcf_input=" in content, "Missing vcf_input parameter in input section"
    assert "annotation_vcf=" in content, (
        "Missing annotation_vcf parameter in input section"
    )
    assert "output_vcf=" in content, "Missing output_vcf parameter in output section"
    assert (
        "tools/snpsift/annotate" in content,
        "Missing or incorrect wrapper path for snpsift annotate",
    )


def test_run_annotate(test_paths, tmp_path):
    """Test that the annotate tool correctly processes the input files."""
    from run_annotate import run_annotate

    temp_output = tmp_path / "output.vcf"

    result = run_annotate(
        vcf_input=str(test_paths["vcf_input"]),
        annotation_vcf=str(test_paths["annotation_vcf"]),
        output_vcf=str(temp_output),
    )

    assert result.returncode == 0, "annotate command failed"
    assert temp_output.exists(), "Output VCF file was not created"
    assert temp_output.stat().st_size > 0, "Output VCF file is empty"
