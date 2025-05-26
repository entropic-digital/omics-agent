import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "genome_annotation": test_dir / "test_annotation.gtf",
        "expected_mapping": test_dir / "expected_output.tsv",
    }


def test_snakefile_idtoname(test_paths, tmp_path, capsys):
    """Test that the idtoname tool generates the expected Snakefile."""
    from tools.pyroe.idtoname.run_idtoname import run_idtoname
    
    temp_output = tmp_path / "output.tsv"

    # Generate the Snakefile with print_only=True to capture its content
    run_idtoname(
        genome_annotation=str(test_paths["genome_annotation"]),
        output_mapping=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements in the Snakefile
    assert "rule idtoname:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "genome_annotation=" in content, "Missing genome_annotation input in Snakefile"
    assert "output_mapping=" in content, "Missing output_mapping output in Snakefile"
    assert "tools/pyroe/idtoname" in content, "Missing wrapper path in Snakefile"
    

def test_run_idtoname(test_paths, tmp_path):
    """Test the execution of the idtoname tool with test files."""
    from tools.pyroe.idtoname.run_idtoname import run_idtoname
    
    temp_output = tmp_path / "generated_output.tsv"

    # Run the tool
    result = run_idtoname(
        genome_annotation=str(test_paths["genome_annotation"]),
        output_mapping=str(temp_output)
    )

    # Verify successful execution
    assert result.returncode == 0, "idtoname tool execution failed"
    assert temp_output.exists(), "Expected output file was not created"
    
    # Optional: Compare generated output to expected output
    with open(temp_output, "r") as generated, open(test_paths["expected_mapping"], "r") as expected:
        assert generated.read() == expected.read(), "Generated output does not match the expected output"