import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_vcf": test_dir / "input.vcf",
        "expected_table": test_dir / "expected_table.txt",
    }


def test_snakefile_table(test_paths, tmp_path, capsys):
    """Test that table generates the expected Snakefile."""
    from tools.vembrane.table.run_table import run_table
    temp_output = tmp_path / "output_table.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_table(
        input_vcf=str(test_paths["input_vcf"]),
        output_table=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule table:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Add assertions for required input parameters
    assert "input_vcf=" in content, "Missing input_vcf parameter"
    # Add assertions for required output parameters
    assert "output_table=" in content, "Missing output_table parameter"


def test_run_table(test_paths, tmp_path):
    """Test that table can be run with the test files."""
    from tools.vembrane.table.run_table import run_table
    temp_output = tmp_path / "output_table.txt"

    result = run_table(
        input_vcf=str(test_paths["input_vcf"]),
        output_table=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "table run failed"

    # Verify that the output file is not empty and matches expected output
    assert temp_output.exists(), "Output table file was not created"
    assert temp_output.stat().st_size > 0, "Output table file is empty"

    # Optionally, compare contents of the generated file with the expected result
    with temp_output.open() as generated, test_paths["expected_table"].open() as expected:
        assert generated.read() == expected.read(), "Output table content does not match expected content"