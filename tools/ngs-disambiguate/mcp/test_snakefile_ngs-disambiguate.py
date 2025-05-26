import pytest
from pathlib import Path
from subprocess import CompletedProcess
from tools.ngs_disambiguate.run_ngs_disambiguate import run_ngs_disambiguate

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_data"
    return {
        "species_a_bam": base_dir / "species_a.bam",
        "species_b_bam": base_dir / "species_b.bam",
        "ambiguous_species_a_bam": base_dir / "ambiguous_species_a.bam",
        "ambiguous_species_b_bam": base_dir / "ambiguous_species_b.bam",
        "unambiguous_species_a_bam": base_dir / "unambiguous_species_a.bam",
        "unambiguous_species_b_bam": base_dir / "unambiguous_species_b.bam"
    }

def test_snakefile_ngs_disambiguate(test_paths, tmp_path, capsys):
    """Test that the ngs-disambiguate Snakefile is generated correctly."""
    run_ngs_disambiguate(
        species_a_bam=str(test_paths["species_a_bam"]),
        species_b_bam=str(test_paths["species_b_bam"]),
        ambiguous_species_a_bam=str(tmp_path / "ambiguous_species_a.bam"),
        ambiguous_species_b_bam=str(tmp_path / "ambiguous_species_b.bam"),
        unambiguous_species_a_bam=str(tmp_path / "unambiguous_species_a.bam"),
        unambiguous_species_b_bam=str(tmp_path / "unambiguous_species_b.bam"),
        print_only=True
    )
    
    captured = capsys.readouterr()
    content = captured.out

    assert "rule ngs_disambiguate:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper definition in Snakefile"
    assert "species_a_bam=" in content, "Missing species_a_bam input parameter in Snakefile"
    assert "species_b_bam=" in content, "Missing species_b_bam input parameter in Snakefile"
    assert "ambiguous_species_a_bam=" in content, "Missing ambiguous_species_a_bam output in Snakefile"
    assert "ambiguous_species_b_bam=" in content, "Missing ambiguous_species_b_bam output in Snakefile"
    assert "unambiguous_species_a_bam=" in content, "Missing unambiguous_species_a_bam output in Snakefile"
    assert "unambiguous_species_b_bam=" in content, "Missing unambiguous_species_b_bam output in Snakefile"

def test_run_ngs_disambiguate(test_paths, tmp_path):
    """Test that the ngs-disambiguate tool runs successfully."""
    result: CompletedProcess = run_ngs_disambiguate(
        species_a_bam=str(test_paths["species_a_bam"]),
        species_b_bam=str(test_paths["species_b_bam"]),
        ambiguous_species_a_bam=str(tmp_path / "test_ambiguous_species_a.bam"),
        ambiguous_species_b_bam=str(tmp_path / "test_ambiguous_species_b.bam"),
        unambiguous_species_a_bam=str(tmp_path / "test_unambiguous_species_a.bam"),
        unambiguous_species_b_bam=str(tmp_path / "test_unambiguous_species_b.bam"),
    )
    
    assert result.returncode == 0, "ngs-disambiguate run failed"
    output_files = [
        tmp_path / "test_ambiguous_species_a.bam",
        tmp_path / "test_ambiguous_species_b.bam",
        tmp_path / "test_unambiguous_species_a.bam",
        tmp_path / "test_unambiguous_species_b.bam",
    ]
    for output_file in output_files:
        assert output_file.exists(), f"Output file {output_file} not generated"