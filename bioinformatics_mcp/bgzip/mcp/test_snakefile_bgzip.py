import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths for bgzip tests."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "example.txt",
        "expected_snakefile": test_dir / "Snakefile",
        "compressed_output": test_dir / "example.txt.gz",
        "decompressed_output": test_dir / "example_decompressed.txt",
    }


def test_snakefile_bgzip(test_paths, tmp_path, capsys):
    """Test that bgzip generates the expected Snakefile."""
    from bioinformatics_mcp.bgzip.mcp.run_bgzip import run_bgzip

    temp_output = tmp_path / "output.txt.gz"

    # Generate the Snakefile with print_only=True
    run_bgzip(
        file=str(test_paths["input_file"]),
        output=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile elements
    assert "rule bgzip:" in content, (
        "The Snakefile is missing the rule definition for bgzip."
    )
    assert "input:" in content, "The Snakefile is missing the input section."
    assert "output:" in content, "The Snakefile is missing the output section."
    assert "wrapper:" in content, "The Snakefile is missing the wrapper section."

    # Verify required input/output fields from meta.yaml
    assert f"'{str(test_paths['input_file'])}'" in content, (
        "The input file is missing in the Snakefile."
    )
    assert f"'{str(temp_output)}'" in content, (
        "The output file is missing in the Snakefile."
    )


def test_run_bgzip(test_paths, tmp_path):
    """Test that bgzip can run successfully and produce expected results."""
    from bioinformatics_mcp.bgzip.mcp.run_bgzip import run_bgzip

    compressed_output = tmp_path / "compressed.txt.gz"
    decompressed_output = tmp_path / "decompressed.txt"

    # Test compression
    result_compress = run_bgzip(
        file=str(test_paths["input_file"]),
        output=str(compressed_output),
    )

    # Verify compression success
    assert result_compress.returncode == 0, "bgzip compression run failed."
    assert compressed_output.exists(), "Compressed output file was not created."

    # Test decompression
    result_decompress = run_bgzip(
        file=str(compressed_output),
        output=str(decompressed_output),
    )

    # Verify decompression success
    assert result_decompress.returncode == 0, "bgzip decompression run failed."
    assert decompressed_output.exists(), "Decompressed output file was not created."

    # Verify the decompressed file matches the original file
    with (
        open(test_paths["input_file"], "rb") as original,
        open(decompressed_output, "rb") as decompressed,
    ):
        original_content = original.read()
        decompressed_content = decompressed.read()

    assert original_content == decompressed_content, (
        "Decompressed file content does not match the original file."
    )
