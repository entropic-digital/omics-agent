import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "vcf": test_dir / "input.vcf",
        "reference_genome": test_dir / "reference.fasta",
        "filtered_vcf": test_dir / "filtered.vcf",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_selectvariants(test_paths, tmp_path, capsys):
    """Test that selectvariants generates the expected Snakefile."""
    from tools.gatk.selectvariants.run_selectvariants import run_selectvariants

    temp_output = tmp_path / "filtered.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_selectvariants(
        vcf=str(test_paths["vcf"]),
        reference_genome=str(test_paths["reference_genome"]),
        filtered_vcf=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule selectvariants:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Add assertions for all required input parameters
    assert "vcf=" in content, "Missing vcf input parameter"
    assert "reference_genome=" in content, "Missing reference_genome input parameter"
    # Add assertions for all required output parameters
    assert "filtered_vcf=" in content, "Missing filtered_vcf output parameter"


def test_run_selectvariants(test_paths, tmp_path):
    """Test that selectvariants can be run with the test files."""
    from tools.gatk.selectvariants.run_selectvariants import run_selectvariants

    temp_output = tmp_path / "filtered.vcf"

    result = run_selectvariants(
        vcf=str(test_paths["vcf"]),
        reference_genome=str(test_paths["reference_genome"]),
        filtered_vcf=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "selectvariants run failed"

    # Verify the filtered VCF file exists
    assert temp_output.exists(), "Filtered VCF output file is missing"
