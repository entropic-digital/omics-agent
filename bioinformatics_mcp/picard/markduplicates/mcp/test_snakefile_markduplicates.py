import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input1": test_dir / "test_input1.bam",
        "expected_snakefile": test_dir / "expected_snakefile.smk",
        "dummy_output": test_dir / "dummy_output.bam"
    }

def test_snakefile_markduplicates(test_paths, tmp_path, capsys):
    """Test that the markduplicates Snakefile is rendered correctly."""
    from bioinformatics_mcp.picard.markduplicates.run_markduplicates import run_markduplicates
    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile (print_only=True to capture output to stdout)
    run_markduplicates(
        input_files=str(test_paths["input1"]),
        output_file=str(temp_output),
        print_only=True
    )

    # Capture generated Snakefile content
    captured = capsys.readouterr()
    snakefile_content = captured.out

    # Assertions to verify Snakefile generation
    assert "rule markduplicates:" in snakefile_content, "Snakefile is missing the 'markduplicates' rule definition."
    assert "input:" in snakefile_content, "Snakefile is missing the 'input:' section."
    assert f"'{test_paths['input1']}'" in snakefile_content, "Input file is missing in the Snakefile."
    assert "output:" in snakefile_content, "Snakefile is missing the 'output:' section."
    assert f"'{temp_output}'" in snakefile_content, "Output file is missing in the Snakefile."
    assert "wrapper:" in snakefile_content, "Snakefile is missing the 'wrapper:' section."
    assert "file:tools/picard/markduplicates" in snakefile_content, "Wrapper path is incorrect or missing in the Snakefile."

def test_run_markduplicates(test_paths, tmp_path):
    """Test that the markduplicates tool executes successfully."""
    from bioinformatics_mcp.picard.markduplicates.run_markduplicates import run_markduplicates
    temp_output = tmp_path / "output.bam"

    # Execute the tool
    result = run_markduplicates(
        input_files=str(test_paths["input1"]),
        output_file=str(temp_output),
        extra="--example-param"
    )

    # Assertions to verify execution
    assert result.returncode == 0, "markduplicates tool execution failed."
    assert temp_output.exists(), "Output file was not generated."
