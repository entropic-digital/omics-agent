import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_files": [test_dir / "sample1.rds", test_dir / "sample2.rds"],
        "output_file": test_dir / "output.rds",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_make_table(test_paths, tmp_path, capsys):
    """Test that make_table generates the expected Snakefile."""
    from bioinformatics_mcp.dada2.make_table.run_make_table import run_make_table

    temp_output = tmp_path / "output.rds"

    run_make_table(
        input_files=[str(f) for f in test_paths["input_files"]],
        output_file=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule make_table:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    for input_file in test_paths["input_files"]:
        assert str(input_file) in content, f"Missing input file {input_file} in Snakefile"
    assert str(temp_output) in content, "Missing output file in Snakefile"


def test_run_make_table(test_paths, tmp_path):
    """Test that make_table runs successfully with the test files."""
    from bioinformatics_mcp.dada2.make_table.run_make_table import run_make_table

    temp_output = tmp_path / "output.rds"

    result = run_make_table(
        input_files=[str(f) for f in test_paths["input_files"]],
        output_file=str(temp_output)
    )

    assert result.returncode == 0, "make_table run failed"
    assert temp_output.exists(), "Output file was not created"