import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "aln": test_dir / "test_alignment.bam",
        "refgene": test_dir / "test_refgene.bed",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }

def test_snakefile_infer_experiment(test_paths, tmp_path, capsys):
    """Test that the infer_experiment Snakefile is rendered correctly."""
    from bioinformatics_mcp.rseqc.infer_experiment.run_infer_experiment import run_infer_experiment
    temp_output = tmp_path / "output.txt"

    # Generate the Snakefile with print_only=True to capture its content
    run_infer_experiment(
        aln=str(test_paths["aln"]),
        refgene=str(test_paths["refgene"]),
        output=str(temp_output),
        print_only=True
    )

    # Capture printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify required rule elements and parameters
    assert "rule infer_experiment:" in content, "Missing rule definition in Snakefile."
    assert "input:" in content, "Missing input section in Snakefile."
    assert "output:" in content, "Missing output section in Snakefile."
    assert "params:" in content, "Missing params section in Snakefile."
    assert "wrapper:" in content, "Missing wrapper section in Snakefile."
    assert "aln=" in content, "Missing aln input in Snakefile."
    assert "refgene=" in content, "Missing refgene input in Snakefile."
    assert "output=" in content, "Missing output parameter in Snakefile."

def test_run_infer_experiment(test_paths, tmp_path):
    """Test the execution of the infer_experiment tool."""
    from bioinformatics_mcp.rseqc.infer_experiment.run_infer_experiment import run_infer_experiment
    temp_output = tmp_path / "output.txt"

    # Run the tool with test inputs
    result = run_infer_experiment(
        aln=str(test_paths["aln"]),
        refgene=str(test_paths["refgene"]),
        output=str(temp_output),
    )

    # Verify if the tool ran successfully
    assert result.returncode == 0, "infer_experiment execution failed."
    # Verify if the output file was generated
    assert temp_output.exists(), "Output file was not created during tool execution."