import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    test_data_dir = test_dir / "data"
    return {
        "input_protein_fasta": test_data_dir / "sample_protein.fasta",
        "expected_output_index": test_data_dir / "sample_index.idx",
        "expected_snakefile": test_data_dir / "Snakefile",
    }


def test_snakefile_index(test_paths, tmp_path, capsys):
    """Test that paladin index generates the expected Snakefile."""
    from bioinformatics_mcp.paladin.index.run_index import run_index
    temp_output_index = tmp_path / "output.idx"

    # Generate Snakefile with print_only=True
    run_index(
        protein_fasta_file=str(test_paths["input_protein_fasta"]),
        output_index_file=str(temp_output_index),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in generated Snakefile
    assert "rule index:" in content, "Missing 'rule index:' definition"
    assert "input:" in content, "Missing 'input:' section"
    assert "output:" in content, "Missing 'output:' section"
    assert "wrapper:" in content, "Missing 'wrapper:' section"

    # Verify all required inputs are present
    assert f"protein_fasta_file='{test_paths['input_protein_fasta']}'" in content, "Missing protein_fasta_file input"

    # Verify all required outputs are present
    assert f"output_index_file='{temp_output_index}'" in content, "Missing output_index_file output"


def test_run_index(test_paths, tmp_path):
    """Test that paladin index can be run with the test files."""
    from bioinformatics_mcp.paladin.index.run_index import run_index
    temp_output_index = tmp_path / "output.idx"

    # Run the tool with test files
    result = run_index(
        protein_fasta_file=str(test_paths["input_protein_fasta"]),
        output_index_file=str(temp_output_index),
    )

    # Verify the process completes successfully
    assert result.returncode == 0, "Paladin index run failed"
    
    # Verify the expected output file is generated
    assert temp_output_index.exists(), f"Output file {temp_output_index} not created"
    
    # Additional assertion to verify file content, if applicable
    assert temp_output_index.stat().st_size > 0, f"Output file {temp_output_index} is empty"