import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths for the bamtag tool."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test" / "bamtag"
    return {
        "input_bam": test_dir / "test_input.bam",
        "expected_bam": test_dir / "expected_output.bam",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_bamtag(test_paths, tmp_path, capsys):
    """Test that bamtag generates a valid Snakefile."""
    from tools.umis.bamtag.run_bamtag import run_bamtag
    temp_output = tmp_path / "output.bam"

    # Generate Snakefile with print_only=True
    run_bamtag(
        input_bam=str(test_paths["input_bam"]),
        output_bam=str(temp_output),
        umi_tag="UM",
        cell_tag="CB",
        umi_sep=":",
        print_only=True,
    )

    # Capture printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements
    assert "rule bamtag:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "input_bam=" in content, "Missing input_bam parameter"
    assert "output_bam=" in content, "Missing output_bam parameter"
    assert "umi_tag=" in content, "Missing umi_tag parameter"
    assert "cell_tag=" in content, "Missing cell_tag parameter"
    assert "umi_sep=" in content, "Missing umi_sep parameter"


def test_run_bamtag(test_paths, tmp_path):
    """Test that bamtag executes successfully with test files."""
    from tools.umis.bamtag.run_bamtag import run_bamtag
    temp_output = tmp_path / "output.bam"

    # Run the bamtag tool
    result = run_bamtag(
        input_bam=str(test_paths["input_bam"]),
        output_bam=str(temp_output),
        umi_tag="UM",
        cell_tag="CB",
        umi_sep=":",
    )

    # Verify successful run
    assert result.returncode == 0, "bamtag execution failed"

    # Check if output file is created
    assert temp_output.exists(), "Output BAM file not created"

    # Optionally compare with expected output (if provided)
    if test_paths["expected_bam"].exists():
        assert temp_output.read_bytes() == test_paths["expected_bam"].read_bytes(), "Output BAM does not match expected output"