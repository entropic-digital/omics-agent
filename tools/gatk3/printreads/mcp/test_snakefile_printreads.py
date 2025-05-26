import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "bam_file": test_dir / "test.bam",
        "recalibration_table": test_dir / "recalibration.table",
        "reference_genome": test_dir / "reference.fasta",
        "output_bam": test_dir / "output.bam",
        "expected_snakefile": test_dir / "expected_snakefile.txt",
    }

def test_snakefile_printreads(test_paths, tmp_path, capsys):
    """Test that printreads generates the correct Snakefile."""
    from tools.gatk3.printreads.mcp.run_printreads import run_printreads
    
    temp_output = tmp_path / "output.bam"

    run_printreads(
        bam_file=str(test_paths["bam_file"]),
        recalibration_table=str(test_paths["recalibration_table"]),
        reference_genome=str(test_paths["reference_genome"]),
        output_bam=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule printreads:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam_file=" in content, "Missing bam_file parameter"
    assert "recalibration_table=" in content, "Missing recalibration_table parameter"
    assert "reference_genome=" in content, "Missing reference_genome parameter"
    assert "output_bam=" in content, "Missing output_bam parameter"

def test_run_printreads(test_paths, tmp_path):
    """Test that printreads runs correctly with the provided test files."""
    from tools.gatk3.printreads.mcp.run_printreads import run_printreads

    temp_output = tmp_path / "output.bam"

    result = run_printreads(
        bam_file=str(test_paths["bam_file"]),
        recalibration_table=str(test_paths["recalibration_table"]),
        reference_genome=str(test_paths["reference_genome"]),
        output_bam=str(temp_output),
    )
    
    assert result.returncode == 0, "printreads execution failed"
    assert temp_output.exists(), "Output BAM file was not created"