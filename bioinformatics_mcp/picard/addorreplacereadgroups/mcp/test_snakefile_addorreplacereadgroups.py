import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "input_bam": test_dir / "input.bam",
        "expected_output_bam": test_dir / "expected_output.bam",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }

def test_snakefile_addorreplacereadgroups(test_paths, tmp_path, capsys):
    """Test that addorreplacereadgroups generates the expected Snakefile."""
    from bioinformatics_mcp.picard.addorreplacereadgroups.run_addorreplacereadgroups import run_addorreplacereadgroups

    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_addorreplacereadgroups(
        input_bam=str(test_paths["input_bam"]),
        output_bam=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile elements
    assert "rule addorreplacereadgroups:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"bam='{test_paths['input_bam']}'" in content, "Missing or incorrect input BAM parameter"
    assert f"bam='{temp_output}'" in content, "Missing or incorrect output BAM parameter"

def test_run_addorreplacereadgroups(test_paths, tmp_path):
    """Test that addorreplacereadgroups can be run with the test files."""
    from bioinformatics_mcp.picard.addorreplacereadgroups.run_addorreplacereadgroups import run_addorreplacereadgroups

    temp_output = tmp_path / "output.bam"

    result = run_addorreplacereadgroups(
        input_bam=str(test_paths["input_bam"]),
        output_bam=str(temp_output)
    )

    # Verify the run is successful
    assert result.returncode == 0, "addorreplacereadgroups run failed"

    # Verify the output file is created
    assert temp_output.exists(), "Output BAM file not created"

    # Optional: Compare the output file with an expected file (if applicable)
    # assert filecmp.cmp(temp_output, test_paths["expected_output_bam"]), "Output BAM file does not match expected"
