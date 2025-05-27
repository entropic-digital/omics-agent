import pytest
from pathlib import Path
from bioinformatics_mcp.bwa_memx.mcp.run_index import run_index


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_files"
    return {
        "fasta_file": base_dir / "test.fasta",
        "expected_snakefile": base_dir / "expected_snakefile",
        "output_prefix": base_dir / "output_prefix"
    }


def test_snakefile_index(test_paths, tmp_path, capsys):
    """Test that the BWA-MEMX index tool generates the expected Snakefile."""
    temp_output = tmp_path / "test_output"

    # Run the index tool with print_only=True to simulate Snakefile generation
    run_index(
        fasta_file=str(test_paths["fasta_file"]),
        output_prefix=str(temp_output),
        bwa="bwa-mem",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assert essential rule elements are present in the generated Snakefile
    assert "rule index:" in content, "Missing rule definition in Snakefile."
    assert "input:" in content, "Missing input section in Snakefile."
    assert "fasta_file=" in content, "Missing fasta_file parameter in Snakefile."
    assert "output:" in content, "Missing output section in Snakefile."
    assert "wrapper:" in content, "Missing wrapper section in Snakefile."
    assert '"params.bwa": "bwa-mem"' in content, "Missing BWA type (bwa-mem) parameter in Snakefile."
    assert str(test_paths["output_prefix"]) in content, "Output prefix not found in Snakefile."


def test_run_index(test_paths, tmp_path):
    """Test BWA-MEMX index tool execution with test files."""
    temp_output = tmp_path / "output_test"

    result = run_index(
        fasta_file=str(test_paths["fasta_file"]),
        output_prefix=str(temp_output),
        bwa="bwa-mem"
    )

    # Assert the tool execution was successful
    assert result.returncode == 0, "BWA-MEMX index tool execution failed."
    # Assert expected output files are generated using the given output prefix
    assert temp_output.with_suffix(".amb").exists(), "Missing BWA index file (.amb)."
    assert temp_output.with_suffix(".ann").exists(), "Missing BWA index file (.ann)."
    assert temp_output.with_suffix(".bwt").exists(), "Missing BWA index file (.bwt)."
    assert temp_output.with_suffix(".pac").exists(), "Missing BWA index file (.pac)."
    assert temp_output.with_suffix(".sa").exists(), "Missing BWA index file (.sa)."