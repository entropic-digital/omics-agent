import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bed_file": test_dir / "test.bed",
        "fasta_file": test_dir / "test.fasta",
        "fasta_index_file": test_dir / "test.fasta.fai",
        "polished_assembly_fasta": test_dir / "polished_assembly.fasta",
        "polished_assembly_agp": test_dir / "polished_assembly.agp",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_salsa2(test_paths, tmp_path, capsys):
    """Test that salsa2 generates the expected Snakefile."""
    from tools.salsa2.mcp.run_salsa2 import run_salsa2

    run_salsa2(
        bed_file=str(test_paths["bed_file"]),
        fasta_file=str(test_paths["fasta_file"]),
        fasta_index_file=str(test_paths["fasta_index_file"]),
        polished_assembly_fasta=str(test_paths["polished_assembly_fasta"]),
        polished_assembly_agp=str(test_paths["polished_assembly_agp"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule salsa2:" in content, "Missing rule definition for Salsa2"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "bed_file=" in content, "Missing BED file parameter in input"
    assert "fasta_file=" in content, "Missing FASTA file parameter in input"
    assert "fasta_index_file=" in content, "Missing FASTA index file parameter in input"
    assert "polished_assembly_fasta=" in content, "Missing polished FASTA output in output"
    assert "polished_assembly_agp=" in content, "Missing polished AGP output in output"


def test_run_salsa2(test_paths, tmp_path):
    """Test that salsa2 can be run with the test files."""
    from tools.salsa2.mcp.run_salsa2 import run_salsa2

    temp_fasta_output = tmp_path / "output.fasta"
    temp_agp_output = tmp_path / "output.agp"

    result = run_salsa2(
        bed_file=str(test_paths["bed_file"]),
        fasta_file=str(test_paths["fasta_file"]),
        fasta_index_file=str(test_paths["fasta_index_file"]),
        polished_assembly_fasta=str(temp_fasta_output),
        polished_assembly_agp=str(temp_agp_output),
    )

    assert result.returncode == 0, "Salsa2 run failed"
    assert temp_fasta_output.exists(), "Polished FASTA output file was not created"
    assert temp_agp_output.exists(), "Polished AGP output file was not created"