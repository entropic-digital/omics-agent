import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "reads": test_dir / "reads.fastq",
        "idx": test_dir / "index.ht",
        "expected_output": test_dir / "expected_output.bam",
    }


def test_snakefile_align(test_paths, tmp_path, capsys):
    """Test that the Snakefile for align is generated correctly."""
    from tools.dragmap.align.run_align import run_align

    temp_output = tmp_path / "output.bam"

    run_align(
        reads=[str(test_paths["reads"])],
        idx=str(test_paths["idx"]),
        output=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule align:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper definition in Snakefile"

    assert f"'{test_paths['reads']}'" in content, "Missing reads input in Snakefile"
    assert f"'{test_paths['idx']}'" in content, "Missing idx input in Snakefile"
    assert f"'{temp_output}'" in content, "Missing output file in Snakefile"


def test_run_align(test_paths, tmp_path):
    """Test that the align tool runs successfully."""
    from tools.dragmap.align.run_align import run_align

    temp_output = tmp_path / "output.bam"

    result = run_align(
        reads=[str(test_paths["reads"])],
        idx=str(test_paths["idx"]),
        output=str(temp_output),
    )

    assert result.returncode == 0, "Align tool execution failed"
    assert temp_output.exists(), "Output file was not created"