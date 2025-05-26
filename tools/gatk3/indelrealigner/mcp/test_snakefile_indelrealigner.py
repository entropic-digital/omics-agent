import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_files"
    return {
        "bam_file": base_dir / "input.bam",
        "reference_genome": base_dir / "reference.fasta",
        "target_intervals": base_dir / "target.intervals",
        "indel_realigned_bam": base_dir / "output.realigned.bam",
        "expected_snakefile": base_dir / "Snakefile"
    }


def test_snakefile_indelrealigner(test_paths, tmp_path, capsys):
    """Test that indelrealigner generates the expected Snakefile."""
    from tools.gatk3.indelrealigner.mcp.run_indelrealigner import run_indelrealigner
    temp_bam = tmp_path / "output.bam"

    # Generate Snakefile content with print_only=True
    run_indelrealigner(
        bam_file=str(test_paths["bam_file"]),
        reference_genome=str(test_paths["reference_genome"]),
        target_intervals=str(test_paths["target_intervals"]),
        indel_realigned_bam=str(temp_bam),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assertions for Snakefile elements
    assert "rule indelrealigner:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam_file=" in content, "Missing bam_file in inputs"
    assert "reference_genome=" in content, "Missing reference_genome in inputs"
    assert "target_intervals=" in content, "Missing target_intervals in inputs"
    assert "output.indel_realigned_bam" in content, "Missing indel_realigned_bam in outputs"


def test_run_indelrealigner(test_paths, tmp_path):
    """Test that indelrealigner can be executed with test files."""
    from tools.gatk3.indelrealigner.mcp.run_indelrealigner import run_indelrealigner
    temp_bam = tmp_path / "realigned.bam"

    # Run the tool
    result = run_indelrealigner(
        bam_file=str(test_paths["bam_file"]),
        reference_genome=str(test_paths["reference_genome"]),
        target_intervals=str(test_paths["target_intervals"]),
        indel_realigned_bam=str(temp_bam)
    )

    # Assertions for tool execution
    assert result.returncode == 0, "indelrealigner execution failed"
    assert temp_bam.exists(), "Output BAM file not created"
