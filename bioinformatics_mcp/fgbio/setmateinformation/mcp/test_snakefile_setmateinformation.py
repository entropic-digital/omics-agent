import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "input.bam",
        "output_bam": test_dir / "output.bam",
        "expected_snakefile": test_dir / "Snakefile",
    }

def test_snakefile_setmateinformation(test_paths, tmp_path, capsys):
    """Test that setmateinformation generates the expected Snakefile."""
    from bioinformatics_mcp.setmateinformation.mcp.run_setmateinformation import run_setmateinformation
    temp_output = tmp_path / "output.bam"

    # Generate Snakefile with print_only=True to capture content
    run_setmateinformation(
        input_bam=str(test_paths["input_bam"]),
        output_bam=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile elements
    assert "rule setmateinformation:" in content, "Missing rule definition for setmateinformation"
    assert "input:" in content, "Missing input section in setmateinformation rule"
    assert "output:" in content, "Missing output section in setmateinformation rule"
    assert "params:" in content, "Missing params section in setmateinformation rule"
    assert "wrapper:" in content, "Missing wrapper directive in setmateinformation rule"
    assert f"input_bam=" in content, "Missing input_bam parameter"
    assert f"output_bam=" in content, "Missing output_bam parameter"

def test_run_setmateinformation(test_paths, tmp_path):
    """Test that setmateinformation can be successfully run."""
    from bioinformatics_mcp.setmateinformation.mcp.run_setmateinformation import run_setmateinformation
    temp_output = tmp_path / "output.bam"

    # Execute the tool and check return
    result = run_setmateinformation(
        input_bam=str(test_paths["input_bam"]),
        output_bam=str(temp_output),
    )

    # Verify successful execution
    assert result.returncode == 0, "setmateinformation run failed"
    assert temp_output.exists(), "Output BAM file was not created"