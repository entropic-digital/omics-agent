import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "reference_genome": test_dir / "test_genome.fasta",
        "expected_index": test_dir / "expected.index",
        "test_output": test_dir / "test_output.index",
    }

def test_snakefile_index_bwa_mem2(test_paths, tmp_path, capsys):
    """Test that bwa-mem2 index generates the expected Snakefile."""
    from tools.bwa_mem2.index.run_index import run_index

    temp_output = tmp_path / "test_output.index"

    run_index(
        reference_genome=str(test_paths["reference_genome"]),
        indexed_reference_genome=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule index:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "reference_genome=" in content, "Missing reference_genome input parameter"
    assert "indexed_reference_genome=" in content, "Missing indexed_reference_genome output parameter"

def test_run_index_bwa_mem2(test_paths, tmp_path):
    """Test that bwa-mem2 index can be executed with test files."""
    from tools.bwa_mem2.index.run_index import run_index

    temp_output = tmp_path / "test_output.index"

    result = run_index(
        reference_genome=str(test_paths["reference_genome"]),
        indexed_reference_genome=str(temp_output)
    )

    assert result.returncode == 0, "bwa-mem2 index run failed"
    assert temp_output.exists(), "Indexed reference genome was not generated"