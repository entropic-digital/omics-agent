import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input1": test_dir / "input1.bam",
        "input2": test_dir / "input2.bam",
        "expected_snakefile": test_dir / "Snakefile",
        "output_file": test_dir / "merged_output.bam"
    }


def test_snakefile_mergesamfiles(test_paths, tmp_path, capsys):
    """Test that mergesamfiles generates the expected Snakefile."""
    from tools.mergesamfiles.mcp.run_mergesamfiles import run_mergesamfiles
    temp_output = tmp_path / "output.bam"

    run_mergesamfiles(
        input_files=[str(test_paths["input1"]), str(test_paths["input2"])],
        output_file=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule mergesamfiles:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert str(test_paths["input1"]) in content, "Missing first input file in Snakefile"
    assert str(test_paths["input2"]) in content, "Missing second input file in Snakefile"
    assert str(temp_output) in content, "Missing output file in Snakefile"


def test_run_mergesamfiles(test_paths, tmp_path):
    """Test that mergesamfiles can be run with the test files."""
    from tools.mergesamfiles.mcp.run_mergesamfiles import run_mergesamfiles
    temp_output = tmp_path / "merged_output.bam"

    result = run_mergesamfiles(
        input_files=[str(test_paths["input1"]), str(test_paths["input2"])],
        output_file=str(temp_output)
    )

    assert result.returncode == 0, "mergesamfiles run failed with non-zero return code"
    assert temp_output.exists(), "Output file was not created after mergesamfiles run"