import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_files"
    return {
        "bam_file": base_dir / "test.bam",
        "fasta_reference": base_dir / "reference.fasta",
        "vcf_gz": base_dir / "variants.vcf.gz",
        "expected_recal_table": base_dir / "expected.recal_table",
    }


def test_snakefile_baserecalibratorspark(test_paths, tmp_path, capsys):
    """Test that baserecalibratorspark generates the expected Snakefile."""
    from tools.gatk.baserecalibratorspark.mcp.run_baserecalibratorspark import run_baserecalibratorspark

    temp_output = tmp_path / "output.recal_table"

    # Generate the Snakefile with print_only=True to capture the content
    run_baserecalibratorspark(
        bam_file=str(test_paths["bam_file"]),
        fasta_reference=str(test_paths["fasta_reference"]),
        vcf_gz=str(test_paths["vcf_gz"]),
        recal_table=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential Snakefile elements
    assert "rule baserecalibratorspark:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam_file=" in content, "Missing bam_file parameter in input"
    assert "fasta_reference=" in content, "Missing fasta_reference parameter in input"
    assert "vcf_gz=" in content, "Missing vcf_gz parameter in input"
    assert "recal_table=" in content, "Missing recal_table parameter in output"


def test_run_baserecalibratorspark(test_paths, tmp_path):
    """Test that baserecalibratorspark can be run with the test files."""
    from tools.gatk.baserecalibratorspark.mcp.run_baserecalibratorspark import run_baserecalibratorspark
    
    temp_output = tmp_path / "output.recal_table"

    result = run_baserecalibratorspark(
        bam_file=str(test_paths["bam_file"]),
        fasta_reference=str(test_paths["fasta_reference"]),
        vcf_gz=str(test_paths["vcf_gz"]),
        recal_table=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "baserecalibratorspark execution failed"

    # Validate the output recalibration table was generated
    assert temp_output.exists(), "Output recal_table file was not generated"