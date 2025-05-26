import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "jf_file": test_dir / "test_kmer_count.jf",
        "expected_output": test_dir / "expected_dump_output.txt",
    }


def test_snakefile_dump(test_paths, tmp_path, capsys):
    """Test that jellyfish_dump generates the expected Snakefile."""
    from tools.jellyfish.dump.run_dump import run_jellyfish_dump
    temp_output = tmp_path / "dump_output.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_jellyfish_dump(
        kmer_count_jf_file=str(test_paths["jf_file"]),
        dump_output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential elements in the Snakefile
    assert "rule dump:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f'"{test_paths["jf_file"]}"' in content, "Missing Jellyfish kmer_count_jf_file input"
    assert f'"{temp_output}"' in content, "Missing dump_output output"


def test_run_jellyfish_dump(test_paths, tmp_path):
    """Test that jellyfish_dump can be executed with test files."""
    from tools.jellyfish.dump.run_dump import run_jellyfish_dump
    temp_output = tmp_path / "dump_output.txt"

    # Run the tool
    result = run_jellyfish_dump(
        kmer_count_jf_file=str(test_paths["jf_file"]),
        dump_output=str(temp_output)
    )

    # Verify run success
    assert result.returncode == 0, "jellyfish_dump run failed"

    # Validate output file content or existence
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"