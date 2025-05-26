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
        "expected_output": test_dir / "expected_output.bed",
    }


def test_snakefile_complement(test_paths, tmp_path, capsys):
    """Test Snakefile generation for the complement tool."""
    from tools.bedtools.complement.run_complement import run_complement
    temp_output = tmp_path / "output.bed"

    run_complement(
        in_file=str(test_paths["in_file"]),
        genome=str(test_paths["genome"]),
        out_file=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule complement:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper directive in Snakefile"
    assert f"in_file='{test_paths['in_file']}'" in content, "Missing in_file parameter in Snakefile"
    assert f"genome='{test_paths['genome']}'" in content, "Missing genome parameter in Snakefile"
    assert f"out_file='{temp_output}'" in content, "Missing out_file parameter in Snakefile"


def test_run_complement(test_paths, tmp_path):
    """Test the complement tool execution with test data."""
    from tools.bedtools.complement.run_complement import run_complement
    temp_output = tmp_path / "output.bed"

    result = run_complement(
        in_file=str(test_paths["in_file"]),
        genome=str(test_paths["genome"]),
        out_file=str(temp_output),
    )

    assert result.returncode == 0, "Tool execution failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"
