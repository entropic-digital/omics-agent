import pytest
from pathlib import Path
from subprocess import CompletedProcess


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fastq": [test_dir / "test1.fastq", test_dir / "test2.fastq"],
        "index": test_dir / "test_index.idx",
        "output": test_dir / "output",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_quant(test_paths, tmp_path, capsys):
    """Test that quant generates the expected Snakefile."""
    from tools.kallisto.quant.run_quant import run_quant

    temp_output = tmp_path / "output"

    run_quant(
        fastq=[str(path) for path in test_paths["fastq"]],
        index=str(test_paths["index"]),
        output=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule quant:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    for fastq_file in test_paths["fastq"]:
        assert str(fastq_file) in content, f"Missing fastq file: {fastq_file}"

    assert str(test_paths["index"]) in content, "Missing index input"
    assert f"'{temp_output}'" in content, "Missing output directory"


def test_run_quant(test_paths, tmp_path):
    """Test that quant can be run with the test files."""
    from tools.kallisto.quant.run_quant import run_quant

    temp_output = tmp_path / "output"

    result = run_quant(
        fastq=[str(path) for path in test_paths["fastq"]],
        index=str(test_paths["index"]),
        output=str(temp_output),
    )

    assert isinstance(
        result, CompletedProcess
    ), "run_quant did not return a CompletedProcess object"
    assert result.returncode == 0, "quant run failed"
    assert temp_output.exists(), "Output directory was not created"