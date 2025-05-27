import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_reads.fq",
        "reference_file": test_dir / "test_reference.fasta",
        "expected_snakefile": test_dir / "expected_snakefile",
        "temp_output_file": test_dir / "output.sam"
    }


def test_snakefile_mem(test_paths, tmp_path, capsys):
    """Test that mem generates the expected Snakefile."""
    from bioinformatics_mcp.bwa_meme.run_mem import run_mem
    temp_output = tmp_path / "output.sam"

    run_mem(
        input_file=str(test_paths["input_file"]),
        reference_file=str(test_paths["reference_file"]),
        output_file=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule bwa_meme:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "input_file=" in content, "Missing input_file parameter"
    assert "reference_file=" in content, "Missing reference_file parameter"
    assert "output_file=" in content, "Missing output_file parameter"


def test_run_mem(test_paths, tmp_path):
    """Test that mem can be run with the test files."""
    from bioinformatics_mcp.bwa_meme.run_mem import run_mem
    temp_output = tmp_path / "output.sam"

    result = run_mem(
        input_file=str(test_paths["input_file"]),
        reference_file=str(test_paths["reference_file"]),
        output_file=str(temp_output),
        threads=2
    )

    assert result.returncode == 0, "bwa-meme run failed"
    assert temp_output.exists(), "Output file was not generated"