import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "input.bam",
        "split_bam_file": test_dir / "output.split.bam",
        "expected_snakefile": test_dir / "Snakefile",
        "expected_split_bam": test_dir / "expected_output.split.bam"
    }


def test_snakefile_splitncigarreads(test_paths, tmp_path, capsys):
    """Test that splitncigarreads generates the expected Snakefile."""
    from tools.gatk.splitncigarreads.run_splitncigarreads import run_splitncigarreads
    outputs = tmp_path / "output.split.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_splitncigarreads(
        bam_file=str(test_paths["bam_file"]),
        split_bam_file=str(outputs),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements are present in the generated Snakefile
    assert "rule splitncigarreads:" in content, "Missing rule definition."
    assert "input:" in content, "Missing input section."
    assert "output:" in content, "Missing output section."
    assert "params:" in content, "Missing params section."
    assert "wrapper:" in content, "Missing wrapper section."
    assert f"bam_file='{test_paths['bam_file']}'" in content, "Missing bam_file input."
    assert f"split_bam_file='{outputs}'" in content, "Missing split_bam_file output."
    assert "tools/gatk/splitncigarreads" in content, "Missing wrapper path."


def test_run_splitncigarreads(test_paths, tmp_path):
    """Test that splitncigarreads runs successfully with the test files."""
    from tools.gatk.splitncigarreads.run_splitncigarreads import run_splitncigarreads
    temp_output = tmp_path / "output.split.bam"

    result = run_splitncigarreads(
        bam_file=str(test_paths["bam_file"]),
        split_bam_file=str(temp_output)
    )

    # Verify that the tool run is successful
    assert result.returncode == 0, "splitncigarreads run failed."

    # Verify the output file is created
    assert temp_output.exists(), "Expected output file was not created."

    # Optionally, compare the output file with an expected output
    expected_output = test_paths["expected_split_bam"]
    assert temp_output.read_bytes() == expected_output.read_bytes(), "Output file does not match expected file."