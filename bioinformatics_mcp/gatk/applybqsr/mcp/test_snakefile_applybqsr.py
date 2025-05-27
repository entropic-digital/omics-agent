import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "test.bam",
        "fasta_reference": test_dir / "test.fasta",
        "recalibration_table": test_dir / "recal.table",
        "recalibrated_bam_file": test_dir / "recalibrated.bam",
        "expected_snakefile": test_dir / "expected_snakefile"
    }

def test_snakefile_applybqsr(test_paths, tmp_path, capsys):
    """Test that applybqsr generates the expected Snakefile."""
    from bioinformatics_mcp.gatk.applybqsr.run_applybqsr import run_applybqsr
    temp_output = tmp_path / "output.bam"

    run_applybqsr(
        bam_file=str(test_paths["bam_file"]),
        fasta_reference=str(test_paths["fasta_reference"]),
        recalibration_table=str(test_paths["recalibration_table"]),
        recalibrated_bam_file=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule applybqsr:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam_file=" in content, "Missing bam_file parameter"
    assert "fasta_reference=" in content, "Missing fasta_reference parameter"
    assert "recalibration_table=" in content, "Missing recalibration_table parameter"
    assert "recalibrated_bam_file=" in content, "Missing recalibrated_bam_file parameter"

def test_run_applybqsr(test_paths, tmp_path):
    """Test that applybqsr can be run with the test files."""
    from bioinformatics_mcp.gatk.applybqsr.run_applybqsr import run_applybqsr
    temp_output = tmp_path / "output.bam"

    result = run_applybqsr(
        bam_file=str(test_paths["bam_file"]),
        fasta_reference=str(test_paths["fasta_reference"]),
        recalibration_table=str(test_paths["recalibration_table"]),
        recalibrated_bam_file=str(temp_output)
    )

    assert result.returncode == 0, "applybqsr run failed"
    assert temp_output.exists(), "Output BAM file was not created"