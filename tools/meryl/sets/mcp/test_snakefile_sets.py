import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input1": test_dir / "input1.meryl",
        "input2": test_dir / "input2.meryl",
        "expected_output": test_dir / "output.meryl"
    }


def test_snakefile_sets(test_paths, tmp_path, capsys):
    """Test that sets generates the expected Snakefile."""
    from tools.meryl.sets.run_sets import run_sets
    temp_output = tmp_path / "output.meryl"

    # Generate the Snakefile with print_only=True to capture the content
    run_sets(
        input_databases=[str(test_paths["input1"]), str(test_paths["input2"])],
        output_database=str(temp_output),
        command="union",
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential components and rule structure in the Snakefile
    assert "rule sets:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "command=" in content, "Missing command parameter in params"
    assert "input_databases=" in content, "Missing input_databases parameter"
    assert "output_database=" in content, "Missing output_database parameter"
    assert "tools/meryl/sets" in content, "Incorrect wrapper path"


def test_run_sets(test_paths, tmp_path):
    """Test that sets can be run with the test files."""
    from tools.meryl.sets.run_sets import run_sets
    temp_output = tmp_path / "output.meryl"

    # Run the tool using the provided test files
    result = run_sets(
        input_databases=[str(test_paths["input1"]), str(test_paths["input2"])],
        output_database=str(temp_output),
        command="union"
    )

    # Verify that the run is successful
    assert result.returncode == 0, "sets tool execution failed"
    assert temp_output.exists(), "Output file was not created"
    
    # Add additional checks if necessary (e.g., output file structure or content)