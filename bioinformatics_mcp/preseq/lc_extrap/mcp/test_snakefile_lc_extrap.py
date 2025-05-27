import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "test_input.bam",
        "input_bed": test_dir / "test_input.bed",
        "expected_output": test_dir / "test_output.lc_extrap",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_lc_extrap(test_paths, tmp_path, capsys):
    """Test that lc_extrap generates the expected Snakefile."""
    from bioinformatics_mcp.preseq.lc_extrap.run_lc_extrap import run_lc_extrap

    temp_output = tmp_path / "output.lc_extrap"

    run_lc_extrap(
        input_file=str(test_paths["input_bam"]),
        output_file=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule lc_extrap:" in content, "Snakefile is missing 'rule lc_extrap' definition"
    assert "input:" in content, "Snakefile is missing input section"
    assert "output:" in content, "Snakefile is missing output section"
    assert "wrapper:" in content, "Snakefile is missing wrapper section"
    assert f"'{test_paths['input_bam']}'" in content, "Input BAM file not found in Snakefile"
    assert f"'{temp_output}'" in content, "Output file not found in Snakefile"


def test_run_lc_extrap(test_paths, tmp_path):
    """Test that lc_extrap can be run with the test files."""
    from bioinformatics_mcp.preseq.lc_extrap.run_lc_extrap import run_lc_extrap

    temp_output = tmp_path / "output.lc_extrap"

    result = run_lc_extrap(
        input_file=str(test_paths["input_bam"]),
        output_file=str(temp_output)
    )

    assert result.returncode == 0, "lc_extrap execution failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"