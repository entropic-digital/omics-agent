import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.fasta",
        "expected_output_file": test_dir / "expected_output.fasta",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_replace_bases(test_paths, tmp_path, capsys):
    """Test that replace_bases generates the expected Snakefile."""
    from bioinformatics_mcp.pyfastaq.replace_bases.run_replace_bases import run_replace_bases
    temp_output = tmp_path / "output.fasta"

    # Generate the Snakefile with print_only=True to capture the content
    run_replace_bases(
        infile=str(test_paths["input_file"]),
        outfile=str(temp_output),
        from_base="A",
        to_base="T",
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify all essential Snakefile elements are present
    assert "rule replace_bases:" in content, "Missing 'replace_bases' rule definition"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "infile=" in content, "Missing infile parameter in input"
    assert "outfile=" in content, "Missing outfile parameter in output"
    assert "from_base=" in content, "Missing from_base parameter in params"
    assert "to_base=" in content, "Missing to_base parameter in params"


def test_run_replace_bases(test_paths, tmp_path):
    """Test that replace_bases executes correctly and produces the expected output."""
    from bioinformatics_mcp.pyfastaq.replace_bases.run_replace_bases import run_replace_bases
    temp_output = tmp_path / "output.fasta"

    # Run the tool using the test input
    result = run_replace_bases(
        infile=str(test_paths["input_file"]),
        outfile=str(temp_output),
        from_base="A",
        to_base="T"
    )

    # Verify that the tool executed successfully
    assert result.returncode == 0, "replace_bases execution failed"

    # Verify the output matches the expected output
    assert temp_output.exists(), "Output file was not created"
    with open(temp_output, "r") as output_file, open(test_paths["expected_output_file"], "r") as expected_file:
        assert output_file.read() == expected_file.read(), "Output file content does not match expected output"