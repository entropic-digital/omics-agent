import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "genomic_assembly": test_dir / "test_genomic_assembly.fasta",
        "expected_output": test_dir / "expected_output.tsv",
    }


def test_snakefile_mlst(test_paths, tmp_path, capsys):
    """Test that mlst generates the expected Snakefile."""
    from tools.mlst.run_mlst import run_mlst
    temp_output = tmp_path / "output.tsv"

    # Generate the Snakefile with print_only=True
    run_mlst(
        genomic_assembly=str(test_paths["genomic_assembly"]),
        output_file=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential Snakemake rule elements
    assert "rule mlst:" in content, "Rule 'mlst' is missing in Snakefile."
    assert "input:" in content, "Input section is missing in Snakefile."
    assert "output:" in content, "Output section is missing in Snakefile."
    assert "params:" in content, "Params section is missing in Snakefile."
    assert "wrapper:" in content, "Wrapper section is missing in Snakefile."
    
    # Verify inputs and outputs
    assert "genomic_assembly=" in content, "Input genomic_assembly is missing."
    assert "output_file=" in content, "Output output_file is missing."


def test_run_mlst(test_paths, tmp_path):
    """Test that mlst can be run with the test files."""
    from tools.mlst.run_mlst import run_mlst
    temp_output = tmp_path / "output.tsv"

    result = run_mlst(
        genomic_assembly=str(test_paths["genomic_assembly"]),
        output_file=str(temp_output)
    )

    # Verify that the process completes successfully
    assert result.returncode == 0, "MLST run failed."
    
    # Verify that the output file is created
    assert temp_output.exists(), "Output file was not created."
    
    # Optionally, compare the contents with an expected output file
    with open(temp_output, 'r') as output, open(test_paths["expected_output"], 'r') as expected:
        assert output.read() == expected.read(), "Output content does not match expected content."