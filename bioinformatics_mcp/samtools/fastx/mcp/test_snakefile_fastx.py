import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "example.bam",
        "expected_output_file": test_dir / "example.fastq",
        "unexpected_output_file": test_dir / "example.fasta",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_fastx(test_paths, tmp_path, capsys):
    """Test that fastx generates the expected Snakefile."""
    from bioinformatics_mcp.samtools.fastx.mcp.run_fastx import run_fastx

    temp_output = tmp_path / "output.fastq"

    run_fastx(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule fastx:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f'"{str(test_paths["input_file"])}"' in content, "Missing input file path in Snakefile"
    assert f'"{str(temp_output)}"' in content, "Missing output file path in Snakefile"


def test_run_fastx(test_paths, tmp_path):
    """Test that fastx can be run with the test files."""
    from bioinformatics_mcp.samtools.fastx.mcp.run_fastx import run_fastx

    temp_output = tmp_path / "output.fastq"

    result = run_fastx(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output)
    )

    assert result.returncode == 0, "fastx run failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.suffix == ".fastq", "Output file should have .fastq extension"

    assert not Path(str(test_paths["unexpected_output_file"])).exists(), "Unexpected output file was created"