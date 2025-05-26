import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_vcf": test_dir / "input.vcf",
        "new_header": test_dir / "new_header.txt",
        "new_samples": test_dir / "new_samples.txt",
        "expected_snakefile": test_dir / "Snakefile",
        "expected_output": test_dir / "expected_output.vcf",
    }


def test_snakefile_reheader(test_paths, tmp_path, capsys):
    """Test that the reheader Snakefile is generated correctly."""
    from tools.bcftools.reheader.run_reheader import run_reheader
    temp_output = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True
    run_reheader(
        input_file=str(test_paths["input_vcf"]),
        output_file=str(temp_output),
        header=str(test_paths["new_header"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assertions to check for content in the Snakefile
    assert "rule reheader:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f"vcf_file={str(test_paths['input_vcf'])}" in content, "Missing input VCF file parameter"
    assert f"header={str(test_paths['new_header'])}" in content, "Missing header parameter"
    assert f"output_file={str(temp_output)}" in content, "Missing output file parameter"


def test_run_reheader(test_paths, tmp_path):
    """Test the reheader tool execution."""
    from tools.bcftools.reheader.run_reheader import run_reheader
    temp_output = tmp_path / "output.vcf"

    # Run the reheader tool
    result = run_reheader(
        input_file=str(test_paths["input_vcf"]),
        output_file=str(temp_output),
        header=str(test_paths["new_header"]),
    )

    # Assertions to verify tool execution
    assert result.returncode == 0, "Reheader tool execution failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"