import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_fname": test_dir / "test_input.fasta",
        "output_fname": test_dir / "test_output.dmnd",
        "expected_snakefile": test_dir / "expected_snakefile",
    }


def test_snakefile_makedb(test_paths, tmp_path, capsys):
    """Test that makedb generates the expected Snakefile."""
    from bioinformatics_mcp.diamond.makedb.run_makedb import run_makedb

    temp_output = tmp_path / "output.dmnd"

    # Generate the Snakefile with print_only=True
    run_makedb(
        input_fname=str(test_paths["input_fname"]),
        output_fname=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the Snakefile
    assert "rule makedb:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify required input parameter
    assert f"'{test_paths['input_fname']}'" in content, "Missing input_fname parameter"

    # Verify required output parameter
    assert f"'{temp_output}'" in content, "Missing output_fname parameter"


def test_run_makedb(test_paths, tmp_path):
    """Test that makedb can be run with the test files."""
    from bioinformatics_mcp.diamond.makedb.run_makedb import run_makedb

    temp_output = tmp_path / "output.dmnd"

    # Run the makedb tool
    result = run_makedb(
        input_fname=str(test_paths["input_fname"]), output_fname=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "makedb run failed"

    # Verify that output file is created
    assert temp_output.exists(), "Output file was not created"
