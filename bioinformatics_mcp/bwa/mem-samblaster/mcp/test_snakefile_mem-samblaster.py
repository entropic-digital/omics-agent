import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reads": test_dir / "reads.fastq",
        "ref": test_dir / "reference.fasta",
        "expected_bam": test_dir / "expected_output.bam"
    }


def test_snakefile_mem_samblaster(test_paths, tmp_path, capsys):
    """Test that mem-samblaster generates the expected Snakefile."""
    from bioinformatics_mcp.bwa.mem_samblaster.mcp.run_mem_samblaster import run_mem_samblaster
    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_mem_samblaster(
        reads=str(test_paths["reads"]),
        ref=str(test_paths["ref"]),
        out_bam=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements in the Snakefile
    assert "rule mem_samblaster:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "reads=" in content, "Missing reads input parameter"
    assert "ref=" in content, "Missing ref input parameter"
    assert "out_bam=" in content, "Missing output parameter"


def test_run_mem_samblaster(test_paths, tmp_path):
    """Test that mem-samblaster can be run with the test files."""
    from bioinformatics_mcp.bwa.mem_samblaster.mcp.run_mem_samblaster import run_mem_samblaster
    temp_output = tmp_path / "output.bam"

    result = run_mem_samblaster(
        reads=str(test_paths["reads"]),
        ref=str(test_paths["ref"]),
        out_bam=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "mem-samblaster run failed"
    assert temp_output.exists(), "Output BAM file was not created"
    assert temp_output.stat().st_size > 0, "Output BAM file is empty"