import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "input_file": test_dir / "test_input.bam",
        "output_file": test_dir / "test_output.bam",
        "index_file": test_dir / "test_output.bam.bai",
        "expected_snakefile": test_dir / "expected_Snakefile"
    }

def test_snakefile_calmd(test_paths, tmp_path, capsys):
    """Test that calmd generates the expected Snakefile."""
    from tools.samtools.calmd.run_calmd import run_calmd
    temp_output = tmp_path / "output.bam"

    run_calmd(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    snakefile_content = captured.out

    assert "rule calmd:" in snakefile_content, "Missing rule definition for calmd"
    assert "input:" in snakefile_content, "Missing input section in Snakefile"
    assert "output:" in snakefile_content, "Missing output section in Snakefile"
    assert "wrapper:" in snakefile_content, "Missing wrapper section in Snakefile"
    assert f'input_file="{test_paths["input_file"]}"' in snakefile_content, "Missing input_file parameter"
    assert f'output_file="{temp_output}"' in snakefile_content, "Missing output_file parameter"

def test_run_calmd(test_paths, tmp_path):
    """Test that calmd can be executed with test files."""
    from tools.samtools.calmd.run_calmd import run_calmd
    temp_output = tmp_path / "output.bam"
    temp_index = tmp_path / "output.bam.bai"

    result = run_calmd(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        index_file=str(temp_index)
    )

    assert result.returncode == 0, "calmd tool execution failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_index.exists(), "Index file was not created"