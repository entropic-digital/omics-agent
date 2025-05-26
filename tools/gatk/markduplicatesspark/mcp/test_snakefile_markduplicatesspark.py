import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "test.bam",
        "reference_file": test_dir / "reference.fasta",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_markduplicatesspark(test_paths, tmp_path, capsys):
    """Test that markduplicatesspark generates the expected Snakefile."""
    from tools.gatk.markduplicatesspark.mcp.run_markduplicatesspark import run_markduplicatesspark
    temp_output = tmp_path / "output.bam"

    run_markduplicatesspark(
        bam_file=str(test_paths["bam_file"]),
        reference_file=str(test_paths["reference_file"]),
        output_bam=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule markduplicatesspark:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam_file=" in content, "Missing bam_file parameter"
    assert "reference_file=" in content, "Missing reference_file parameter"
    assert "output_bam=" in content, "Missing output_bam parameter"


def test_run_markduplicatesspark(test_paths, tmp_path):
    """Test that markduplicatesspark can be run with the test files."""
    from tools.gatk.markduplicatesspark.mcp.run_markduplicatesspark import run_markduplicatesspark
    temp_output = tmp_path / "output.bam"

    result = run_markduplicatesspark(
        bam_file=str(test_paths["bam_file"]),
        reference_file=str(test_paths["reference_file"]),
        output_bam=str(temp_output)
    )

    assert result.returncode == 0, "markduplicatesspark run failed"
    assert temp_output.exists(), "Output BAM file not created"