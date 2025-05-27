import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "fastq_file": test_dir / "test_input.fastq",
        "expected_snakefile": test_dir / "expected_snakefile",
        "output_png": test_dir / "output.png",
    }

def test_snakefile_quality_profile(test_paths, tmp_path, capsys):
    """Test that quality-profile generates the expected Snakefile."""
    from bioinformatics_mcp.dada2.quality_profile.run_quality_profile import run_quality_profile

    temp_output = tmp_path / "output.png"

    # Generate the Snakefile with print_only=True to capture the content
    run_quality_profile(
        fastq_file=str(test_paths["fastq_file"]),
        output_png=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule quality_profile:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Add assertions for required input/output parameters
    assert f"fastq_file='{test_paths['fastq_file']}'" in content, "Missing fastq_file parameter"
    assert f"output_png='{temp_output}'" in content, "Missing output_png parameter"

def test_run_quality_profile(test_paths, tmp_path):
    """Test that quality-profile can be run with the test files."""
    from bioinformatics_mcp.dada2.quality_profile.run_quality_profile import run_quality_profile

    temp_output = tmp_path / "output.png"

    # Run the tool with test files
    result = run_quality_profile(
        fastq_file=str(test_paths["fastq_file"]),
        output_png=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "quality-profile execution failed"

    # Verify that the output PNG file is created
    assert temp_output.exists(), "Output PNG file was not created"