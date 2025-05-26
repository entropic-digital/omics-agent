import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_sequences": test_dir / "input_sequences.fasta",
        "primer_sequences": test_dir / "primer_sequences.fasta",
        "output_trimmed_sequences": test_dir / "output_trimmed_sequences.fasta",
    }

def test_snakefile_ptrimmer(test_paths, tmp_path, capsys):
    """Test that ptrimmer generates the expected Snakefile."""
    from tools.ptrimmer.mcp.run_ptrimmer import run_ptrimmer
    temp_output = tmp_path / "output_trimmed_sequences.fasta"

    run_ptrimmer(
        input_sequences=str(test_paths["input_sequences"]),
        primer_sequences=str(test_paths["primer_sequences"]),
        output_trimmed_sequences=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule ptrimmer:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "input_sequences=" in content, "Missing input_sequences parameter in Snakefile"
    assert "primer_sequences=" in content, "Missing primer_sequences parameter in Snakefile"
    assert "output_trimmed_sequences=" in content, "Missing output_trimmed_sequences parameter in Snakefile"

def test_run_ptrimmer(test_paths, tmp_path):
    """Test that ptrimmer can be run with the test files."""
    from tools.ptrimmer.mcp.run_ptrimmer import run_ptrimmer
    temp_output = tmp_path / "output_trimmed_sequences.fasta"

    result = run_ptrimmer(
        input_sequences=str(test_paths["input_sequences"]),
        primer_sequences=str(test_paths["primer_sequences"]),
        output_trimmed_sequences=str(temp_output),
    )

    assert result.returncode == 0, "ptrimmer run failed"
    assert temp_output.exists(), "Expected output file was not generated"