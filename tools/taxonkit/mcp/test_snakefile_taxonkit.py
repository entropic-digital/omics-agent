import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.txt",
        "taxdump": test_dir / "test_taxdump",
        "expected_output": test_dir / "expected_output.txt",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_taxonkit(test_paths, tmp_path, capsys):
    """Test that taxonkit generates the expected Snakefile."""
    from tools.taxonkit.mcp.run_taxonkit import run_taxonkit
    temp_output = tmp_path / "output.txt"

    run_taxonkit(
        input_file=str(test_paths["input_file"]),
        taxdump=str(test_paths["taxdump"]),
        output_taxdump=str(temp_output),
        command="reformat",
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule taxonkit:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f"input_file='{test_paths['input_file']}'" in content, "Missing input_file parameter"
    assert f"taxdump='{test_paths['taxdump']}'" in content, "Missing taxdump parameter"
    assert f"output_taxdump='{temp_output}'" in content, "Missing output_taxdump parameter"
    assert "command='reformat'" in content, "Missing command parameter"


def test_run_taxonkit(test_paths, tmp_path):
    """Test that taxonkit can execute successfully with test files."""
    from tools.taxonkit.mcp.run_taxonkit import run_taxonkit
    temp_output = tmp_path / "output.txt"

    result = run_taxonkit(
        input_file=str(test_paths["input_file"]),
        taxdump=str(test_paths["taxdump"]),
        output_taxdump=str(temp_output),
        command="reformat",
    )

    assert result.returncode == 0, f"Taxonkit execution failed with return code: {result.returncode}"
    assert temp_output.exists(), "Output file was not created"
    # Add additional assertions to validate correct processing of test data if necessary