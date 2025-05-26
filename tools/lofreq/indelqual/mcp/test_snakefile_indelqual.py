import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "input.bam",
        "reference_genome": test_dir / "reference.fasta",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_indelqual(test_paths, tmp_path, capsys):
    """Test that indelqual generates the expected Snakefile."""
    from tools.lofreq.indelqual.run_indelqual import run_indelqual

    temp_output = tmp_path / "output.bam"

    run_indelqual(
        bam_file=str(test_paths["bam_file"]),
        reference_genome=str(test_paths["reference_genome"]),
        output_bam=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule indelqual:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam_file=" in content, "Missing bam_file parameter in input"
    assert "reference_genome=" in content, "Missing reference_genome parameter in input"
    assert "output_bam=" in content, "Missing output_bam parameter in output"

def test_run_indelqual(test_paths, tmp_path):
    """Test that indelqual can be run with the test files."""
    from tools.lofreq.indelqual.run_indelqual import run_indelqual

    temp_output = tmp_path / "output.bam"

    result = run_indelqual(
        bam_file=str(test_paths["bam_file"]),
        reference_genome=str(test_paths["reference_genome"]),
        output_bam=str(temp_output)
    )

    assert result.returncode == 0, "indelqual run failed"
    assert temp_output.exists(), "Output BAM file was not created"