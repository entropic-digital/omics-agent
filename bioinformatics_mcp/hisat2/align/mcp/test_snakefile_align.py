import pytest
from pathlib import Path
import subprocess

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "data"
    return {
        "reads1": test_dir / "reads_1.fq",
        "reads2": test_dir / "reads_2.fq",
        "index": test_dir / "index",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "output": test_dir / "output.bam"
    }

def test_snakefile_align(test_paths, tmp_path, capsys):
    """Test align tool's generated Snakefile."""
    from bioinformatics_mcp.hisat2.align.run_align import run_align

    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True
    run_align(
        reads=[str(test_paths["reads1"]), str(test_paths["reads2"])],
        idx=str(test_paths["index"]),
        output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assertions for required fields in the Snakefile content
    assert "rule align:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "reads=" in content, "Missing input reads parameter"
    assert "idx=" in content, "Missing input idx parameter"
    assert "output=" in content, "Missing output parameter"

def test_run_align(test_paths, tmp_path):
    """Test align tool execution."""
    from bioinformatics_mcp.hisat2.align.run_align import run_align

    temp_output = tmp_path / "output.bam"

    # Run the align tool
    result = run_align(
        reads=[str(test_paths["reads1"]), str(test_paths["reads2"])],
        idx=str(test_paths["index"]),
        output=str(temp_output)
    )

    # Verify the tool ran successfully
    assert result.returncode == 0, "align tool execution failed"
    assert temp_output.exists(), "Output file not created"

    # Additional verification for expected output files
    assert temp_output.stat().st_size > 0, "Output BAM file is empty"