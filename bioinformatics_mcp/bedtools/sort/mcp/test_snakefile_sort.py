import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "in_file": test_dir / "test_input.bed",
        "genome": test_dir / "test_genome.txt",
        "faidx": test_dir / "test.faidx",
        "expected_snakefile": test_dir / "expected_Snakefile"
    }

def test_snakefile_sort(test_paths, tmp_path, capsys):
    """Test that sort generates the expected Snakefile."""
    from bioinformatics_mcp.bedtools.sort.run_sort import run_sort
    temp_output = tmp_path / "sorted_output.bed"

    run_sort(
        in_file=str(test_paths["in_file"]),
        output=str(temp_output),
        genome=str(test_paths["genome"]),
        faidx=str(test_paths["faidx"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule sort:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "resources:" in content, "Missing resources section in Snakefile"
    assert "in_file=" in content, "Missing in_file parameter"
    assert "output=" in content, "Missing output parameter"
    assert "genome=" in content, "Missing genome resource"
    assert "faidx=" in content, "Missing faidx resource"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

def test_run_sort(test_paths, tmp_path):
    """Test that sort can be run with the test files."""
    from bioinformatics_mcp.bedtools.sort.run_sort import run_sort
    temp_output = tmp_path / "sorted_output.bed"

    result = run_sort(
        in_file=str(test_paths["in_file"]),
        output=str(temp_output),
        genome=str(test_paths["genome"]),
        faidx=str(test_paths["faidx"])
    )

    assert result.returncode == 0, "Tool execution failed with non-zero return code"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"