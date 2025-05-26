import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "kit": test_dir / "kit",
        "vcf": test_dir / "test.vcf",
        "summary": test_dir / "summary.txt",
        "bed": test_dir / "errors.bed",
    }


def test_snakefile_chm_eval(test_paths, tmp_path, capsys):
    """Test that chm-eval generates the expected Snakefile."""
    from tools.benchmark.chm_eval.run_chm_eval import run_chm_eval

    temp_output_summary = tmp_path / "summary.txt"
    temp_output_bed = tmp_path / "errors.bed"

    # Generate the Snakefile with print_only=True
    run_chm_eval(
        kit=str(test_paths["kit"]),
        vcf=str(test_paths["vcf"]),
        summary=str(temp_output_summary),
        bed=str(temp_output_bed),
        build="37",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assert the essential parts of the Snakefile are generated
    assert "rule chm-eval:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Verify inputs match meta.yaml
    assert "vcf=" in content, "Missing required input parameter: vcf"
    assert "kit=" in content, "Missing required input parameter: kit"
    # Verify outputs match meta.yaml
    assert "summary=" in content, "Missing required output parameter: summary"
    assert "bed=" in content, "Missing required output parameter: bed"
    # Verify parameters
    assert "build=" in content, "Missing required parameter: build"


def test_run_chm_eval(test_paths, tmp_path):
    """Test that chm-eval can be executed with the test files."""
    from tools.benchmark.chm_eval.run_chm_eval import run_chm_eval

    temp_output_summary = tmp_path / "summary.txt"
    temp_output_bed = tmp_path / "errors.bed"

    # Run the tool with the provided test paths
    result = run_chm_eval(
        kit=str(test_paths["kit"]),
        vcf=str(test_paths["vcf"]),
        summary=str(temp_output_summary),
        bed=str(temp_output_bed),
        build="37",
    )

    # Verify the tool executed successfully
    assert result.returncode == 0, "chm-eval execution failed"
    # Ensure the output files were created
    assert temp_output_summary.exists(), "Output summary file was not created"
    assert temp_output_bed.exists(), "Output BED file was not created"
