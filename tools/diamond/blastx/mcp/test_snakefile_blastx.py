import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fname_fastq": test_dir / "test_query.fastq",
        "fname_db": test_dir / "test_db.dmnd",
        "expected_output": test_dir / "expected_output.tsv",
    }


def test_snakefile_blastx(test_paths, tmp_path, capsys):
    """Test that blastx generates the expected Snakefile."""
    from tools.diamond.blastx.run_blastx import run_blastx

    temp_output = tmp_path / "output.tsv"

    run_blastx(
        fname_fastq=str(test_paths["fname_fastq"]),
        fname_db=str(test_paths["fname_db"]),
        fname=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule blastx:" in content, "Missing 'rule blastx' definition in Snakefile"
    assert "input:" in content, "Missing 'input' section in Snakefile"
    assert "output:" in content, "Missing 'output' section in Snakefile"
    assert "params:" in content, "Missing 'params' section in Snakefile"
    assert "wrapper:" in content, "Missing 'wrapper' section in Snakefile"
    assert f"query='{str(test_paths['fname_fastq'])}'" in content, "Missing input 'fname_fastq'"
    assert f"db='{str(test_paths['fname_db'])}'" in content, "Missing input 'fname_db'"
    assert f"out='{str(temp_output)}'" in content, "Missing output file"
    assert "tools/diamond/blastx" in content, "Incorrect or missing wrapper path"


def test_run_blastx(test_paths, tmp_path):
    """Test that blastx can be run with the test files."""
    from tools.diamond.blastx.run_blastx import run_blastx

    temp_output = tmp_path / "output.tsv"

    result = run_blastx(
        fname_fastq=str(test_paths["fname_fastq"]),
        fname_db=str(test_paths["fname_db"]),
        fname=str(temp_output),
    )

    assert result.returncode == 0, "blastx run failed"
    assert temp_output.exists(), "Output file not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"