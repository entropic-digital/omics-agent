import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fastq": test_dir / "example.fastq",
        "idx": test_dir / "reference.idx",
        "expected_sai": test_dir / "expected.sai",
    }


def test_snakefile_aln(test_paths, tmp_path, capsys):
    """Test that aln generates the expected Snakefile."""
    from tools.bwa.aln.run_aln import run_aln

    temp_sai = tmp_path / "temp.sai"

    # Generate the Snakefile using print_only=True
    run_aln(
        fastq=str(test_paths["fastq"]),
        idx=str(test_paths["idx"]),
        sai=str(temp_sai),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assert that essential elements exist in the generated Snakefile
    assert "rule aln:" in content, "Missing 'rule aln' in Snakefile"
    assert "input:" in content, "Missing 'input' section in Snakefile"
    assert "output:" in content, "Missing 'output' section in Snakefile"
    assert "params:" in content, "Missing 'params' section in Snakefile"
    assert "wrapper:" in content, "Missing 'wrapper' section in Snakefile"

    # Verify required inputs are present
    assert f"fastq='{test_paths['fastq']}'" in content, "Missing 'fastq' input in Snakefile"
    assert f"idx='{test_paths['idx']}'" in content, "Missing 'idx' input in Snakefile"

    # Verify required outputs are present
    assert f"sai='{temp_sai}'" in content, "Missing 'sai' output in Snakefile"


def test_run_aln(test_paths, tmp_path):
    """Test that aln can be executed successfully."""
    from tools.bwa.aln.run_aln import run_aln

    temp_sai = tmp_path / "temp.sai"

    # Run the tool
    result = run_aln(
        fastq=str(test_paths["fastq"]),
        idx=str(test_paths["idx"]),
        sai=str(temp_sai),
    )

    # Verify tool execution was successful
    assert result.returncode == 0, f"aln run failed with return code {result.returncode}"
    assert temp_sai.exists(), "SAI file was not created"

    # Additional verification can be included here if needed, e.g., file content validation.