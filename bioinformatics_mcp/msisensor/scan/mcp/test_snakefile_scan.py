import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_fasta": test_dir / "test_input.fasta",
        "expected_output": test_dir / "expected_output.txt",
    }


def test_snakefile_scan(test_paths, tmp_path, capsys):
    """Test that scan generates the expected Snakefile."""
    from bioinformatics_mcp.msisensor.scan.run_scan import run_scan
    temp_output = tmp_path / "output.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_scan(
        input_fasta=str(test_paths["input_fasta"]),
        output_txt=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements are present in the Snakefile
    assert "rule scan:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    # Verify all required inputs and outputs from meta.yaml
    assert "input_fasta=" in content, "Missing input_fasta parameter in Snakefile"
    assert "output_txt=" in content, "Missing output_txt parameter in Snakefile"


def test_run_scan(test_paths, tmp_path):
    """Test that scan can be run successfully with test files."""
    from bioinformatics_mcp.msisensor.scan.run_scan import run_scan
    temp_output = tmp_path / "output.txt"

    # Run the tool with test input and assert successful execution
    result = run_scan(
        input_fasta=str(test_paths["input_fasta"]),
        output_txt=str(temp_output)
    )

    # Verify tool execution succeeded
    assert result.returncode == 0, "MSIsensor scan run failed"
    # Verify output file was generated
    assert temp_output.exists(), "Output file was not generated"
    # Optional: Verify output content matches expectations
    with temp_output.open() as generated, test_paths["expected_output"].open() as expected:
        assert generated.read() == expected.read(), "Output content does not match expected output"