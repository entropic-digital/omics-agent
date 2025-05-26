import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "neopeptides_fasta": test_dir / "neopeptides.fasta",
        "information_tsv": test_dir / "information.tsv",
        "sample_specific_normal_binary": test_dir / "normal.binary",
        "filtered_neopeptides_fasta": test_dir / "filtered_neopeptides.fasta",
        "corresponding_normal_peptides_fasta": test_dir / "corresponding_normal_peptides.fasta",
        "filtered_information_tsv": test_dir / "filtered_information.tsv",
        "removed_self_identical_peptides_tsv": test_dir / "removed_self_identical.tsv"
    }

def test_snakefile_filter(test_paths, tmp_path, capsys):
    """Test that filter generates the expected Snakefile."""
    from tools.microphaser.filter.run_filter import run_filter

    temp_output_dir = tmp_path
    run_filter(
        neopeptides_fasta=str(test_paths["neopeptides_fasta"]),
        information_tsv=str(test_paths["information_tsv"]),
        sample_specific_normal_binary=str(test_paths["sample_specific_normal_binary"]),
        filtered_neopeptides_fasta=str(temp_output_dir / "filtered_neopeptides.fasta"),
        corresponding_normal_peptides_fasta=str(temp_output_dir / "corresponding_normal_peptides.fasta"),
        filtered_information_tsv=str(temp_output_dir / "filtered_information.tsv"),
        removed_self_identical_peptides_tsv=str(temp_output_dir / "removed_self_identical.tsv"),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule filter:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "neopeptides_fasta=" in content, "Missing 'neopeptides_fasta' parameter in Snakefile"
    assert "information_tsv=" in content, "Missing 'information_tsv' parameter in Snakefile"
    assert "sample_specific_normal_binary=" in content, "Missing 'sample_specific_normal_binary' parameter in Snakefile"
    assert "filtered_neopeptides_fasta=" in content, "Missing 'filtered_neopeptides_fasta' parameter in Snakefile"
    assert "corresponding_normal_peptides_fasta=" in content, "Missing 'corresponding_normal_peptides_fasta' parameter in Snakefile"
    assert "filtered_information_tsv=" in content, "Missing 'filtered_information_tsv' parameter in Snakefile"
    assert "removed_self_identical_peptides_tsv=" in content, "Missing 'removed_self_identical_peptides_tsv' parameter in Snakefile"

def test_run_filter(test_paths, tmp_path):
    """Test that filter can be executed successfully with the test files."""
    from tools.microphaser.filter.run_filter import run_filter

    temp_output_dir = tmp_path
    result = run_filter(
        neopeptides_fasta=str(test_paths["neopeptides_fasta"]),
        information_tsv=str(test_paths["information_tsv"]),
        sample_specific_normal_binary=str(test_paths["sample_specific_normal_binary"]),
        filtered_neopeptides_fasta=str(temp_output_dir / "filtered_neopeptides.fasta"),
        corresponding_normal_peptides_fasta=str(temp_output_dir / "corresponding_normal_peptides.fasta"),
        filtered_information_tsv=str(temp_output_dir / "filtered_information.tsv"),
        removed_self_identical_peptides_tsv=str(temp_output_dir / "removed_self_identical.tsv")
    )

    assert result.returncode == 0, "Filter tool execution failed"
    assert (temp_output_dir / "filtered_neopeptides.fasta").exists(), "Filtered neopeptides file not generated"
    assert (temp_output_dir / "corresponding_normal_peptides.fasta").exists(), "Corresponding normal peptides file not generated"
    assert (temp_output_dir / "filtered_information.tsv").exists(), "Filtered information TSV file not generated"
    assert (temp_output_dir / "removed_self_identical.tsv").exists(), "Removed self-identical peptides TSV file not generated"