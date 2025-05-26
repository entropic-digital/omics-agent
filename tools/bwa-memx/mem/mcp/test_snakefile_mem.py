import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "reads": test_dir / "reads.fq",
        "index": test_dir / "index",
        "expected_bam": test_dir / "expected.bam",
        "expected_snakefile": test_dir / "expected_snakefile",
    }


def test_snakefile_mem(test_paths, tmp_path, capsys):
    """Test that mem generates the expected Snakefile."""
    from tools.bwa_memx.run_mem import run_mem

    temp_output_bam = tmp_path / "output.bam"

    run_mem(
        bwa="bwa-mem",
        reads=str(test_paths["reads"]),
        index=str(test_paths["index"]),
        output_bam=str(temp_output_bam),
        threads=4,
        read_group="@RG\tID:test\tSM:test",
        extra_params="--extra-flag",
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule mem:" in content, "Missing 'mem' rule definition in Snakefile"
    assert "input:" in content, "Missing 'input' section in Snakefile"
    assert f"reads={str(test_paths['reads'])}" in content, "Missing 'reads' input in Snakefile"
    assert f"index={str(test_paths['index'])}" in content, "Missing 'index' input in Snakefile"
    assert "output:" in content, "Missing 'output' section in Snakefile"
    assert f"output_bam={str(temp_output_bam)}" in content, "Missing 'output_bam' in Snakefile"
    assert "params:" in content, "Missing 'params' section in Snakefile"
    assert "bwa='bwa-mem'" in content, "Missing 'bwa' parameter in Snakefile"
    assert "threads=4" in content, "Missing 'threads' parameter in Snakefile"
    assert "read_group='@RG\tID:test\tSM:test'" in content, "Missing 'read_group' parameter in Snakefile"
    assert "extra_params='--extra-flag'" in content, "Missing 'extra_params' parameter in Snakefile"
    assert "wrapper:" in content, "Missing 'wrapper' section in Snakefile"
    assert "file:tools/bwa-memx/mem" in content, "Missing wrapper file path in Snakefile"


def test_run_mem(test_paths, tmp_path):
    """Test that mem runs successfully and produces expected output."""
    from tools.bwa_memx.run_mem import run_mem

    temp_output_bam = tmp_path / "output.bam"

    result = run_mem(
        bwa="bwa-mem",
        reads=str(test_paths["reads"]),
        index=str(test_paths["index"]),
        output_bam=str(temp_output_bam),
        threads=2,
    )

    assert result.returncode == 0, "mem execution failed"
    assert temp_output_bam.exists(), "Output BAM file was not created"
    # Add further validation to compare output with expected BAM if necessary
