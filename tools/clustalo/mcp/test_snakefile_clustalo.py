import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test_files"
    return {
        "input_sequences": test_dir / "test_input.fasta",
        "output_alignment": test_dir / "test_output.aln",
        "Snakefile": test_dir / "Snakefile",
    }

def test_snakefile_clustalo(test_paths, tmp_path, capsys):
    """Test that clustalo generates the expected Snakefile."""
    from tools.clustalo.mcp.run_clustalo import run_clustalo

    temp_output = tmp_path / "output.aln"

    run_clustalo(
        input_sequences=str(test_paths["input_sequences"]),
        output_alignment=str(temp_output),
        format="fasta",
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule clustalo:" in content, "Missing 'rule clustalo' definition"
    assert "input:" in content, "Missing input section in Snakefile"
    assert f"'{test_paths['input_sequences']}'" in content, "Missing input_sequences in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert f"'{temp_output}'" in content, "Missing output_alignment in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "'format'" in content, "Missing format parameter in Snakefile"
    assert "'threads'" in content, "Missing threads parameter in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "'file:tools/clustalo'" in content, "Missing correct wrapper path in Snakefile"

def test_run_clustalo(test_paths, tmp_path):
    """Test that clustalo can be run with the test files."""
    from tools.clustalo.mcp.run_clustalo import run_clustalo

    temp_output = tmp_path / "output.aln"

    result = run_clustalo(
        input_sequences=str(test_paths["input_sequences"]),
        output_alignment=str(temp_output),
        format="fasta",
    )

    assert result.returncode == 0, "clustalo run failed"
    assert temp_output.exists(), "Output alignment file was not created"
    assert temp_output.stat().st_size > 0, "Output alignment file is empty"