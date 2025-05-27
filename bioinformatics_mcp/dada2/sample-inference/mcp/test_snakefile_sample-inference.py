import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "derep": test_dir / "test_derep.rds",
        "err": test_dir / "test_err.rds",
        "expected_output": test_dir / "expected_output.rds",
        "snakefile_dir": test_dir / "Snakefile"
    }

def test_snakefile_sample_inference(test_paths, tmp_path, capsys):
    """Test that sample-inference generates the expected Snakefile."""
    from bioinformatics_mcp.dada2.sample_inference.run_sample_inference import run_sample_inference

    temp_output = tmp_path / "output.rds"

    run_sample_inference(
        derep=str(test_paths["derep"]),
        err=str(test_paths["err"]),
        output=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    snakefile_content = captured.out

    assert "rule sample_inference:" in snakefile_content, "Missing rule definition."
    assert "input:" in snakefile_content, "Missing input section."
    assert "'derep':" in snakefile_content, "Missing input derep parameter."
    assert "'err':" in snakefile_content, "Missing input err parameter."
    assert "output:" in snakefile_content, "Missing output section."
    assert "'output':" in snakefile_content, "Missing output parameter."
    assert "params:" in snakefile_content, "Missing params section."
    assert "wrapper:" in snakefile_content, "Missing wrapper section."

def test_run_sample_inference(test_paths, tmp_path):
    """Test that sample-inference runs successfully with test files."""
    from bioinformatics_mcp.dada2.sample_inference.run_sample_inference import run_sample_inference

    temp_output = tmp_path / "output.rds"

    result = run_sample_inference(
        derep=str(test_paths["derep"]),
        err=str(test_paths["err"]),
        output=str(temp_output)
    )

    assert result.returncode == 0, "sample-inference run failed."
    assert temp_output.exists(), "Output file was not created."