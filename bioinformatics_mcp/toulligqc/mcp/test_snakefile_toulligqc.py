import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths for toulligqc."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_path": test_dir / "test_input.fastq",
        "output_path": test_dir / "test_output",
        "expected_snakefile": test_dir / "expected_snakefile",
    }


def test_snakefile_toulligqc(test_paths, tmp_path, capsys):
    """Test that toulligqc generates the expected Snakefile."""
    from bioinformatics_mcp.toulligqc.mcp.run_toulligqc import run_toulligqc
    temp_output = tmp_path / "output"

    run_toulligqc(
        input_path=str(test_paths["input_path"]),
        output_path=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule toulligqc:" in content, "Snakefile is missing 'rule toulligqc' definition."
    assert "input:" in content, "Snakefile is missing an input section."
    assert "output:" in content, "Snakefile is missing an output section."
    assert "wrapper:" in content, "Snakefile is missing a wrapper section."
    assert f"'{test_paths['input_path']}'" in content, "Input path is not correctly specified in Snakefile."
    assert f"'{temp_output}'" in content, "Output path is not correctly specified in Snakefile."


def test_run_toulligqc(test_paths, tmp_path):
    """Test that toulligqc runs successfully with the test input files."""
    from bioinformatics_mcp.toulligqc.mcp.run_toulligqc import run_toulligqc
    temp_output = tmp_path / "output"

    result = run_toulligqc(
        input_path=str(test_paths["input_path"]),
        output_path=str(temp_output),
    )

    assert result.returncode == 0, "toulligqc run failed with a non-zero return code."
    assert temp_output.exists(), "Expected output file or directory was not created."