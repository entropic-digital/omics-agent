import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "input.bam",
        "output_bam": test_dir / "output.bam",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_collapse_reads_to_fragments_bam(test_paths, tmp_path, capsys):
    """Test that collapse_reads_to_fragments-bam generates the expected Snakefile."""
    from bioinformatics_mcp.rbt.collapse_reads_to_fragments_bam.mcp.run_collapse_reads_to_fragments_bam import (
        run_collapse_reads_to_fragments_bam,
    )

    temp_output = tmp_path / "output.bam"

    run_collapse_reads_to_fragments_bam(
        input_bam=str(test_paths["input_bam"]),
        output_bam=str(temp_output),
        read_group="RG1",
        filter_mismatching_ids=False,
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule collapse_reads_to_fragments_bam:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "input_bam=" in content, "Missing input_bam parameter"
    assert "output_bam=" in content, "Missing output_bam parameter"
    assert "read_group=" in content, "Missing read_group parameter"


def test_run_collapse_reads_to_fragments_bam(test_paths, tmp_path):
    """Test that collapse_reads_to_fragments-bam can be run with the test files."""
    from bioinformatics_mcp.rbt.collapse_reads_to_fragments_bam.mcp.run_collapse_reads_to_fragments_bam import (
        run_collapse_reads_to_fragments_bam,
    )

    temp_output = tmp_path / "output.bam"

    result = run_collapse_reads_to_fragments_bam(
        input_bam=str(test_paths["input_bam"]),
        output_bam=str(temp_output),
        read_group="RG1",
        filter_mismatching_ids=False,
    )

    assert result.returncode == 0, "collapse_reads_to_fragments_bam run failed"
    assert temp_output.exists(), "Output BAM file was not created"
