import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "test_fasta_file": test_dir / "test_output.fasta",
        "expected_snakefile": test_dir / "expected_Snakefile"
    }


def test_snakefile_ensembl_sequence(test_paths, tmp_path, capsys):
    """Test that ensembl-sequence generates the expected Snakefile."""
    from bioinformatics_mcp.reference.ensembl_sequence.run_ensembl_sequence import run_ensembl_sequence

    # Dummy output file in a temporary path
    temp_fasta_file = tmp_path / "output.fasta"

    # Generate the Snakefile with print_only=True to capture the content
    run_ensembl_sequence(
        fasta_file=str(temp_fasta_file),
        url="ftp://ftp.ensembl.org/pub",
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential elements are present in the Snakefile
    assert "rule ensembl_sequence:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert f"output={str(temp_fasta_file)!r}" in content, "Missing or incorrect output parameter"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "params:" in content, "Missing params section"
    assert "url=" in content, "Missing 'url' parameter"
    assert "ftp://ftp.ensembl.org/pub" in content, "Wrong or missing default URL in params"


def test_run_ensembl_sequence(test_paths, tmp_path):
    """Test that ensembl-sequence can be run with the test files."""
    from bioinformatics_mcp.reference.ensembl_sequence.run_ensembl_sequence import run_ensembl_sequence

    # Temporary output file for storing the downloaded sequences
    temp_fasta_file = tmp_path / "test_output.fasta"

    # Run the ensembl-sequence tool
    result = run_ensembl_sequence(
        fasta_file=str(temp_fasta_file),
        url="ftp://ftp.ensembl.org/pub"
    )

    # Verify that the run was successful
    assert result.returncode == 0, "ensembl-sequence run failed"
    assert temp_fasta_file.exists(), "Output .fasta file was not created"
    assert temp_fasta_file.stat().st_size > 0, "Output .fasta file is empty"