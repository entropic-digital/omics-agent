import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "test_input.bam",
        "expected_bed": test_dir / "expected_output.bed",
        "generated_snakefile": test_dir / "generated_Snakefile"
    }


def test_snakefile_bamtobed(test_paths, tmp_path, capsys):
    """Test that bamtobed generates the expected Snakefile."""
    from tools.bamtobed.mcp.run_bamtobed import run_bamtobed
    temp_output = tmp_path / "output.bed"

    # Generate the Snakefile with print_only=True to capture the content
    run_bamtobed(
        input_bam=str(test_paths["input_bam"]),
        output_bed=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential parameters in the Snakefile
    assert "rule bamtobed:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"input_bam='{test_paths['input_bam']}'" in content, "Missing input_bam parameter"
    assert f"output_bed='{temp_output}'" in content, "Missing output_bed parameter"


def test_run_bamtobed(test_paths, tmp_path):
    """Test that bamtobed can be run with the test files."""
    from tools.bamtobed.mcp.run_bamtobed import run_bamtobed
    output_bed = tmp_path / "output.bed"

    result = run_bamtobed(
        input_bam=str(test_paths["input_bam"]),
        output_bed=str(output_bed)
    )

    # Verify the command ran successfully
    assert result.returncode == 0, "bamtobed run failed"
    assert output_bed.exists(), "Output BED file was not created"

    # Verify the output BED contents if applicable (optional)
    with output_bed.open() as output_file:
        output_content = output_file.read()
    assert len(output_content) > 0, "Output BED file is empty"