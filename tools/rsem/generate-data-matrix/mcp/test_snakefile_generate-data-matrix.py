import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_files": [test_dir / "sample_1.rsem", test_dir / "sample_2.rsem"],
        "expected_output": test_dir / "expected_output_matrix.tsv",
        "expected_snakefile": test_dir / "expected_snakefile",
    }

def test_snakefile_generate_data_matrix(test_paths, tmp_path, capsys):
    """Test that generate-data-matrix generates the expected Snakefile."""
    from tools.rsem.generate_data_matrix import run_generate_data_matrix

    temp_output = tmp_path / "output_matrix.tsv"

    # Generate the Snakefile with print_only=True
    run_generate_data_matrix(
        input_files=[str(f) for f in test_paths["input_files"]],
        output_matrix=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    snakefile_content = captured.out

    # Validating essential Snakemake rule elements
    assert "rule generate_data_matrix:" in snakefile_content, "Missing rule definition"
    assert "input:" in snakefile_content, "Missing input section"
    assert "output:" in snakefile_content, "Missing output section"
    assert "wrapper:" in snakefile_content, "Missing wrapper section"

    # Verify inputs and outputs from meta.yaml
    for input_file in test_paths["input_files"]:
        assert str(input_file) in snakefile_content, f"Missing input file: {input_file}"
    assert str(temp_output) in snakefile_content, "Missing output file"

def test_run_generate_data_matrix(test_paths, tmp_path):
    """Test that generate-data-matrix can be run with the test files."""
    from tools.rsem.generate_data_matrix import run_generate_data_matrix

    temp_output = tmp_path / "output_matrix.tsv"

    # Execute the tool
    result = run_generate_data_matrix(
        input_files=[str(f) for f in test_paths["input_files"]],
        output_matrix=str(temp_output),
    )

    # Check if the process completes successfully
    assert result.returncode == 0, "generate-data-matrix run failed"
    assert temp_output.exists(), "Output matrix file not created"

    # Optionally, compare the output with an expected file (e.g., content matches)
    with open(temp_output, "r") as generated, open(test_paths["expected_output"], "r") as expected:
        assert generated.read() == expected.read(), "Generated output does not match expected output"