"""Module that tests if the mem Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).resolve().parent.parent
    test_dir = base_dir / "test"
    return {
        "reads": [test_dir / "test_reads_1.fastq", test_dir / "test_reads_2.fastq"],
        "idx": [
            test_dir / "ref.0123",
            test_dir / "ref.amb",
            test_dir / "ref.ann",
            test_dir / "ref.bwt.2bit.64",
            test_dir / "ref.pac",
        ],
        "output": test_dir / "test_output.sam",
    }


def test_snakefile_mem(test_paths, tmp_path, capsys):
    """Test that mem generates the expected Snakefile."""
    from tools.bwa_mem2.mcp.run_mem import run_mem

    output_path = tmp_path / "output.sam"

    run_mem(
        reads=[str(r) for r in test_paths["reads"]],
        idx=[str(i) for i in test_paths["idx"]],
        output=str(output_path),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule mem:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper directive in Snakefile"

    for read in test_paths["reads"]:
        assert str(read) in content, f"Missing read input file {read} in Snakefile"
    for idx in test_paths["idx"]:
        assert str(idx) in content, f"Missing index file {idx} in Snakefile"
    assert str(output_path) in content, "Missing output file path in Snakefile"

    assert "extra" in content, "Missing extra parameter in Snakefile"
    assert "sorting" in content, "Missing sorting option in Snakefile"
    assert "sort_extra" in content, "Missing sort_extra option in Snakefile"


def test_run_mem(test_paths, tmp_path):
    """Test that mem can be run with the provided test files."""
    from tools.bwa_mem2.mcp.run_mem import run_mem

    output_path = tmp_path / "output.sam"

    result = run_mem(
        reads=[str(r) for r in test_paths["reads"]],
        idx=[str(i) for i in test_paths["idx"]],
        output=str(output_path),
    )

    assert result.returncode == 0, "mem tool execution failed"
    assert output_path.exists(), "Output file was not created"
