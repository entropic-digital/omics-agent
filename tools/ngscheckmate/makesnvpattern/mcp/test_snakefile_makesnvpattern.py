import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_files"
    return {
        "bed": base_dir / "test.bed",
        "fasta": base_dir / "test.fasta",
        "index": [
            base_dir / "bowtie_index_1",
            base_dir / "bowtie_index_2",
        ],
        "expected_snakefile": base_dir / "expected_Snakefile",
        "output_fasta": base_dir / "output.fasta",
        "output_pattern_uncompressed": base_dir / "output_pattern_uncompressed.txt",
        "output_pattern": base_dir / "output_pattern.bin",
    }


def test_snakefile_makesnvpattern(test_paths, capsys):
    """Test that makesnvpattern generates the expected Snakefile."""
    from tools.ngscheckmate.makesnvpattern.run_makesnvpattern import run_makesnvpattern

    run_makesnvpattern(
        bed=str(test_paths["bed"]),
        fasta=str(test_paths["fasta"]),
        index=[str(idx) for idx in test_paths["index"]],
        output_fasta=str(test_paths["output_fasta"]),
        output_pattern_uncompressed=str(test_paths["output_pattern_uncompressed"]),
        output_pattern=str(test_paths["output_pattern"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in the Snakefile
    assert "rule makesnvpattern:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper directive"
    assert "bed=" in content, "Missing `bed` input parameter"
    assert "fasta=" in content, "Missing `fasta` input parameter"
    assert "index=" in content, "Missing `index` input parameter"
    assert "fasta=" in content, "Missing `fasta` output parameter"
    assert "pattern_uncompressed=" in content, "Missing `pattern_uncompressed` output parameter"
    assert "pattern=" in content, "Missing `pattern` output parameter"


def test_run_makesnvpattern(test_paths, tmp_path):
    """Test that makesnvpattern can be run with the test files."""
    from tools.ngscheckmate.makesnvpattern.run_makesnvpattern import run_makesnvpattern

    temp_output_fasta = tmp_path / "output.fasta"
    temp_output_pattern_uncompressed = tmp_path / "output_pattern_uncompressed.txt"
    temp_output_pattern = tmp_path / "output_pattern.bin"

    result = run_makesnvpattern(
        bed=str(test_paths["bed"]),
        fasta=str(test_paths["fasta"]),
        index=[str(idx) for idx in test_paths["index"]],
        output_fasta=str(temp_output_fasta),
        output_pattern_uncompressed=str(temp_output_pattern_uncompressed),
        output_pattern=str(temp_output_pattern),
    )

    # Verify successful execution
    assert result.returncode == 0, "makesnvpattern run failed"
    # Verify outputs are created
    assert temp_output_fasta.exists(), "Output fasta file was not created"
    assert temp_output_pattern_uncompressed.exists(), "Output uncompressed pattern file was not created"
    assert temp_output_pattern.exists(), "Output compressed pattern file was not created"