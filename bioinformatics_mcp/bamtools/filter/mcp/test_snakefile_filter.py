import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths for the filter tool."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "input.bam",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_filter_tool(test_paths, tmp_path, capsys):
    """Test that the filter tool generates the expected Snakefile."""
    from bioinformatics_mcp.bamtools.filter.run_filter import run_filter
    temp_output_bam = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture its contents
    run_filter(
        bam_files=str(test_paths["bam_file"]),
        output_bam=str(temp_output_bam),
        tags="NM",
        min_size=100,
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    generated_snakefile = captured.out

    # Verify the essential rule elements are present
    assert "rule filter:" in generated_snakefile, "Missing rule definition"
    assert "input:" in generated_snakefile, "Missing input section"
    assert "output:" in generated_snakefile, "Missing output section"
    assert "params:" in generated_snakefile, "Missing params section"
    assert "wrapper:" in generated_snakefile, "Missing wrapper section"

    # Verify specific parameters and paths in the Snakefile
    assert str(test_paths["bam_file"]) in generated_snakefile, "Input BAM file not found in Snakefile"
    assert str(temp_output_bam) in generated_snakefile, "Output BAM file not found in Snakefile"
    assert "tags='NM'" in generated_snakefile, "Tag parameter missing or incorrect"
    assert "min_size=100" in generated_snakefile, "Min size parameter missing or incorrect"


def test_run_filter_tool(test_paths, tmp_path):
    """Test that the filter tool can be executed with the test files."""
    from bioinformatics_mcp.bamtools.filter.run_filter import run_filter
    temp_output_bam = tmp_path / "output.bam"

    # Execute the filter tool
    result = run_filter(
        bam_files=str(test_paths["bam_file"]),
        output_bam=str(temp_output_bam),
        tags="NM",
        min_size=100,
    )

    # Verify that the run is successful
    assert result.returncode == 0, "Filter tool execution failed"

    # Verify that the output BAM file is created
    assert temp_output_bam.is_file(), "Output BAM file was not created"
