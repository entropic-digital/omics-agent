import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_reads": test_dir / "reads.fastq",
        "expected_snakefile": test_dir / "expected_snakefile.txt",
        "output_assembly": test_dir / "output.fasta",
    }

def test_snakefile_unicycler(test_paths, tmp_path, capsys):
    """Test that unicycler generates the expected Snakefile."""
    from tools.unicycler.mcp.run_unicycler import run_unicycler
    temp_output = tmp_path / "output.fasta"

    run_unicycler(
        input_reads=str(test_paths["input_reads"]),
        output_assembly=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule unicycler:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "input_reads=" in content, "Missing input_reads parameter in Snakefile"
    assert "output_assembly=" in content, "Missing output_assembly parameter in Snakefile"

def test_run_unicycler(test_paths, tmp_path):
    """Test that unicycler can be run with the test files."""
    from tools.unicycler.mcp.run_unicycler import run_unicycler
    temp_output = tmp_path / "output.fasta"

    result = run_unicycler(
        input_reads=str(test_paths["input_reads"]),
        output_assembly=str(temp_output)
    )

    assert result.returncode == 0, "Unicycler execution failed"
    assert temp_output.exists(), "Output file was not created"