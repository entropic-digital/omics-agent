import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fasta_file": test_dir / "test.fasta",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_index(test_paths, tmp_path, capsys):
    """Test that the BWA index Snakefile is generated correctly."""
    from bioinformatics_mcp.bwa.index.run_index import run_index

    # Generate the Snakefile with print_only=True to capture the content
    run_index(fasta_file=str(test_paths["fasta_file"]), print_only=True)

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present in the Snakefile
    assert "rule index:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Assertions specific to inputs
    assert f'fasta_file="{test_paths["fasta_file"]}"' in content, "Missing fasta_file parameter in Snakefile"

    # Assertions specific to outputs
    assert "temp(" in content, "Missing temp() output in Snakefile"
    assert "fasta.amb" in content, "Missing BWA output file .amb in Snakefile"
    assert "fasta.ann" in content, "Missing BWA output file .ann in Snakefile"
    assert "fasta.bwt" in content, "Missing BWA output file .bwt in Snakefile"
    assert "fasta.pac" in content, "Missing BWA output file .pac in Snakefile"
    assert "fasta.sa" in content, "Missing BWA output file .sa in Snakefile"


def test_run_index(test_paths, tmp_path):
    """Test that the BWA index tool executes successfully with test files."""
    from bioinformatics_mcp.bwa.index.run_index import run_index

    # Run the index tool
    temp_output = tmp_path / "output"
    result = run_index(fasta_file=str(test_paths["fasta_file"]), workdir=tmp_path)

    # Verify that the command ran successfully
    assert result.returncode == 0, "BWA index tool exited with a non-zero return code"

    # Verify all expected output files are created
    output_files = [
        f"test.fasta.{ext}" for ext in ["amb", "ann", "bwt", "pac", "sa"]
    ]
    for output_file in output_files:
        assert (tmp_path / output_file).exists(), f"Expected output file {output_file} was not created"