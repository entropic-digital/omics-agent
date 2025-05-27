import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_reads": test_dir / "test_reads.fastq",
        "output_bam": test_dir / "test_output.bam",
        "genome_dir": test_dir / "genome_dir",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_align(test_paths, tmp_path, capsys):
    """Test that align generates the expected Snakefile."""
    from bioinformatics_mcp.star.run_align import run_align

    temp_output_bam = tmp_path / "output.bam"

    run_align(
        input_reads=str(test_paths["input_reads"]),
        output_bam=str(temp_output_bam),
        genome_dir=str(test_paths["genome_dir"]),
        threads=4,
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule align:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper call in Snakefile"
    assert "reads=" in content, "Missing reads input parameter"
    assert "bam=" in content, "Missing BAM output parameter"
    assert "genome_dir=" in content, "Missing genome_dir parameter"
    assert "threads=" in content, "Missing threads parameter"


def test_run_align(test_paths, tmp_path):
    """Test that align can be run with the test files."""
    from bioinformatics_mcp.star.run_align import run_align

    temp_output_bam = tmp_path / "output.bam"

    result = run_align(
        input_reads=str(test_paths["input_reads"]),
        output_bam=str(temp_output_bam),
        genome_dir=str(test_paths["genome_dir"]),
        threads=4,
        print_only=False,
    )

    assert result.returncode == 0, "align tool execution failed"
    assert temp_output_bam.exists(), "Output BAM file was not generated"