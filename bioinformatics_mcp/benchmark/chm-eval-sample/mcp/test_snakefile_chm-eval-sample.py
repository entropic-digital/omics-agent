import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam": test_dir / "test.bam",
        "bai": test_dir / "test.bai",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_chm_eval_sample(test_paths, tmp_path, capsys):
    """Test that chm-eval-sample generates the expected Snakefile."""
    from bioinformatics_mcp.benchmark.chm_eval_sample.run_chm_eval_sample import run_chm_eval_sample

    run_chm_eval_sample(
        bam=str(test_paths["bam"]),
        bai=str(test_paths["bai"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule chm_eval_sample:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "'bam':" in content, "Missing bam input parameter"
    assert "'bai':" in content, "Missing bai input parameter"
    assert "'bam':" in content, "Missing bam output parameter"
    assert "'bai':" in content, "Missing bai output parameter"


def test_run_chm_eval_sample(test_paths, tmp_path):
    """Test that chm-eval-sample can be run with the test files."""
    from bioinformatics_mcp.benchmark.chm_eval_sample.run_chm_eval_sample import run_chm_eval_sample

    temp_bam_output = tmp_path / "output.bam"
    temp_bai_output = tmp_path / "output.bai"

    result = run_chm_eval_sample(
        bam=str(temp_bam_output),
        bai=str(temp_bai_output)
    )

    assert result.returncode == 0, "chm-eval-sample run failed"
    assert temp_bam_output.exists(), "BAM output file not created"
    assert temp_bai_output.exists(), "BAI output file not created"