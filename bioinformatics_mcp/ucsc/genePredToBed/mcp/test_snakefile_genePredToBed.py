import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input": test_dir / "test_input.genePred",
        "expected_output": test_dir / "test_output.bed",
        "expected_snakefile": test_dir / "expected_Snakefile"
    }


def test_snakefile_genePredToBed(test_paths, tmp_path, capsys):
    """Test that genePredToBed generates the expected Snakefile."""
    from bioinformatics_mcp.ucsc.genePredToBed.run_genePredToBed import run_genePredToBed
    temp_output = tmp_path / "output.bed"

    # Generate the Snakefile with print_only=True to capture the content
    run_genePredToBed(
        input_path=str(test_paths["input"]),
        output_path=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule genePredToBed:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Add assertions for required input/output parameters
    assert f"'{test_paths['input']}'" in content, "Missing input file reference"
    assert f"'{temp_output}'" in content, "Missing output file reference"


def test_run_genePredToBed(test_paths, tmp_path):
    """Test that genePredToBed can be run with the test files."""
    from bioinformatics_mcp.ucsc.genePredToBed.run_genePredToBed import run_genePredToBed
    temp_output = tmp_path / "output.bed"

    # Run the tool
    result = run_genePredToBed(
        input_path=str(test_paths["input"]),
        output_path=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "genePredToBed run failed"

    # Verify the output file is correctly generated
    assert temp_output.exists(), "Output file not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"