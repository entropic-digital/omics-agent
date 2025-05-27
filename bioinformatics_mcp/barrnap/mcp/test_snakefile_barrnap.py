import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test_files"
    return {
        "fasta": test_dir / "test.fasta",
        "gff": test_dir / "output.gff",
        "fasta_output": test_dir / "output.fasta",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_barrnap(test_paths, tmp_path, capsys):
    """Test that barrnap generates the expected Snakefile."""
    from bioinformatics_mcp.barrnap.run_barrnap import run_barrnap

    run_barrnap(
        fasta=str(test_paths["fasta"]),
        gff=str(test_paths["gff"]),
        fasta_output=str(test_paths["fasta_output"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule barrnap:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "fasta=" in content, "Missing `fasta` input parameter in Snakefile"
    assert "gff=" in content, "Missing `gff` output parameter in Snakefile"
    assert "fasta_output=" in content, "Missing `fasta_output` optional output parameter in Snakefile"


def test_run_barrnap(test_paths, tmp_path):
    """Test that barrnap runs successfully with the provided test files."""
    from bioinformatics_mcp.barrnap.run_barrnap import run_barrnap

    temp_gff = tmp_path / "output.gff"
    temp_fasta_output = tmp_path / "output.fasta"

    result = run_barrnap(
        fasta=str(test_paths["fasta"]),
        gff=str(temp_gff),
        fasta_output=str(temp_fasta_output),
        kingdom="bac",
    )

    assert result.returncode == 0, "Barrnap execution failed"
    assert temp_gff.exists(), "Expected GFF output file was not created"
    assert temp_fasta_output.exists(), "Expected FASTA output file was not created"