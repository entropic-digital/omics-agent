import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths for the chm-eval-kit tests."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test" / "chm_eval_kit"
    return {
        "input1": test_dir / "input1.txt",
        "input2": test_dir / "input2.txt",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "output_dir": test_dir / "output"
    }

def test_snakefile_chm_eval_kit(test_paths, tmp_path, capsys):
    """Test that chm-eval-kit generates the expected Snakefile."""
    from tools.benchmark.chm_eval_kit.run_chm_eval_kit import run_chm_eval_kit

    temp_output = tmp_path / "output_dir"

    # Generate the Snakefile with print_only=True to capture the content
    run_chm_eval_kit(
        tag="v1.0",
        version="1.0.0",
        output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile components
    assert "rule chm_eval_kit:" in content, "Missing rule definition for chm_eval_kit"
    assert "params:" in content, "Missing parameters section"
    assert "tag=" in content, "Missing 'tag' parameter"
    assert "version=" in content, "Missing 'version' parameter"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper definition"
    assert "file:tools/benchmark/chm-eval-kit" in content, "Missing correct wrapper path"
    assert "CHM-eval" in content, "Missing reference to CHM-eval in the comments"

def test_run_chm_eval_kit(test_paths, tmp_path):
    """Test that chm-eval-kit runs successfully and produces outputs."""
    from tools.benchmark.chm_eval_kit.run_chm_eval_kit import run_chm_eval_kit

    temp_output = tmp_path / "output_dir"
    temp_output.mkdir()

    result = run_chm_eval_kit(
        tag="v1.0",
        version="1.0.0",
        output=str(temp_output)
    )

    # Verify the process completed successfully
    assert result.returncode == 0, "chm-eval-kit process failed to complete successfully"

    # Verify output directory is created
    assert temp_output.exists(), "Output directory was not created"

    # Verify expected output files
    expected_file = temp_output / "chm_eval_kit_output.txt"
    assert expected_file.exists(), "Expected output file was not created"
    assert expected_file.stat().st_size > 0, "Output file is empty"