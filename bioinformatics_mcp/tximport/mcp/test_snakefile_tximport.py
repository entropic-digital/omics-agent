import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_files": [test_dir / "input1.tsv", test_dir / "input2.tsv"],
        "expected_snakefile": test_dir / "Snakefile",
        "output_file": test_dir / "output.tximport.rds"
    }


def test_snakefile_tximport(test_paths, tmp_path, capsys):
    """Test that tximport generates the expected Snakefile."""
    from bioinformatics_mcp.tximport.mcp.run_tximport import run_tximport
    temp_output = tmp_path / "output.tximport.rds"

    run_tximport(
        input_files=[str(file) for file in test_paths["input_files"]],
        output_file=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule tximport:" in content, "Snakefile missing 'tximport' rule definition"
    assert "input:" in content, "Snakefile missing 'input' section"
    for input_file in test_paths["input_files"]:
        assert str(input_file) in content, f"Snakefile missing input file {input_file}"
    assert "output:" in content, "Snakefile missing 'output' section"
    assert str(temp_output) in content, "Snakefile missing output file"
    assert "wrapper:" in content, "Snakefile missing 'wrapper' section"


def test_run_tximport(test_paths, tmp_path):
    """Test that tximport can be run with the test files."""
    from bioinformatics_mcp.tximport.mcp.run_tximport import run_tximport
    temp_output = tmp_path / "output.tximport.rds"

    result = run_tximport(
        input_files=[str(file) for file in test_paths["input_files"]],
        output_file=str(temp_output)
    )

    assert result.returncode == 0, "tximport execution failed"
    assert temp_output.exists(), f"Expected output file {temp_output} was not created"