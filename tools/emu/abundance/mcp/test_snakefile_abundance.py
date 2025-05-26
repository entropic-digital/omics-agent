import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test file paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reads": test_dir / "reads.fastq",
        "db": test_dir / "database.db",
        "abundances": test_dir / "abundances.tsv",
        "alignments": test_dir / "alignments.sam",
        "unclassified": test_dir / "unclassified.fasta",
        "unmapped": test_dir / "unmapped.fasta"
    }

def test_snakefile_abundance(test_paths, tmp_path, capsys):
    """Test that the abundance Snakefile is generated correctly."""
    from tools.emu.abundance.run_abundance import run_abundance

    temp_abundances = tmp_path / "abundances.tsv"
    temp_alignments = tmp_path / "alignments.sam"
    temp_unclassified = tmp_path / "unclassified.fasta"
    temp_unmapped = tmp_path / "unmapped.fasta"

    run_abundance(
        reads=str(test_paths["reads"]),
        db=str(test_paths["db"]),
        abundances=str(temp_abundances),
        alignments=str(temp_alignments),
        unclassified=str(temp_unclassified),
        unmapped=str(temp_unmapped),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule abundance:" in content, "Rule `abundance` is missing in the Snakefile"
    assert "input:" in content, "Input section is missing in the Snakefile"
    assert "output:" in content, "Output section is missing in the Snakefile"
    assert "wrapper:" in content, "Wrapper directive is missing in the Snakefile"

    assert "reads=" in content, "Missing `reads` input in Snakefile"
    assert "db=" in content, "Missing `db` parameter in Snakefile"
    assert "abundances=" in content, "Missing `abundances` output in Snakefile"
    assert "alignments=" in content, "Missing `alignments` output in Snakefile"
    assert "unclassified=" in content, "Missing `unclassified` output in Snakefile"
    assert "unmapped=" in content, "Missing `unmapped` output in Snakefile"

def test_run_abundance(test_paths, tmp_path):
    """Test that the abundance tool execution works with test files."""
    from tools.emu.abundance.run_abundance import run_abundance

    temp_abundances = tmp_path / "abundances.tsv"
    temp_alignments = tmp_path / "alignments.sam"
    temp_unclassified = tmp_path / "unclassified.fasta"
    temp_unmapped = tmp_path / "unmapped.fasta"

    result = run_abundance(
        reads=str(test_paths["reads"]),
        db=str(test_paths["db"]),
        abundances=str(temp_abundances),
        alignments=str(temp_alignments),
        unclassified=str(temp_unclassified),
        unmapped=str(temp_unmapped)
    )

    assert result.returncode == 0, "Abundance tool execution failed"
    assert temp_abundances.exists(), "Abundances output file was not created"
    assert temp_alignments.exists(), "Alignments output file was not created"
    assert temp_unclassified.exists(), "Unclassified output file was not created"
    assert temp_unmapped.exists(), "Unmapped output file was not created"