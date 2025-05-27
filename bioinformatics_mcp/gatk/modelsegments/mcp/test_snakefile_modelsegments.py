import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "denoised_copy_ratios": test_dir / "denoised_copy_ratios.tsv",
        "allelic_counts": test_dir / "allelic_counts.tsv",
        "segments": test_dir / "segments.interval_list",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_modelsegments(test_paths, tmp_path, capsys):
    """Test that modelsegments generates the expected Snakefile."""
    from bioinformatics_mcp.gatk.modelsegments.run_modelsegments import run_modelsegments

    run_modelsegments(
        denoised_copy_ratios=str(test_paths["denoised_copy_ratios"]),
        allelic_counts=str(test_paths["allelic_counts"]),
        segments=str(test_paths["segments"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile elements
    assert "rule modelsegments:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper definition"

    # Verify input parameters
    assert "denoised_copy_ratios=" in content, "Missing denoised_copy_ratios input"
    assert "allelic_counts=" in content, "Missing allelic_counts input"
    assert "segments=" in content, "Missing segments input"

    # Verify rule outputs
    expected_outputs = [
        ".modelFinal.seq",
        ".cr.seg",
        ".af.igv.seg",
        ".cr.igv.seg",
        ".hets.tsv",
        ".modelBegin.cr.param",
        ".modelBegin.af.param",
        ".modelFinal.af.param",
        ".modelFinal.cr.param",
    ]
    for output in expected_outputs:
        assert output in content, f"Missing expected output: {output}"


def test_run_modelsegments(test_paths, tmp_path):
    """Test that modelsegments can be executed with test files."""
    from bioinformatics_mcp.gatk.modelsegments.run_modelsegments import run_modelsegments

    temp_output_dir = tmp_path / "output"
    temp_output_dir.mkdir()

    result = run_modelsegments(
        denoised_copy_ratios=str(test_paths["denoised_copy_ratios"]),
        allelic_counts=str(test_paths["allelic_counts"]),
        segments=str(test_paths["segments"]),
        output_dir=str(temp_output_dir),
    )

    # Verify successful execution
    assert result.returncode == 0, "modelsegments execution failed"

    # Verify output files
    expected_outputs = [
        temp_output_dir / "sample.modelFinal.seq",
        temp_output_dir / "sample.cr.seg",
        temp_output_dir / "sample.af.igv.seg",
        temp_output_dir / "sample.cr.igv.seg",
        temp_output_dir / "sample.hets.tsv",
        temp_output_dir / "sample.modelBegin.cr.param",
        temp_output_dir / "sample.modelBegin.af.param",
        temp_output_dir / "sample.modelFinal.af.param",
        temp_output_dir / "sample.modelFinal.cr.param",
    ]

    for output_file in expected_outputs:
        assert output_file.exists(), f"Missing output file: {output_file}"