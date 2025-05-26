import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths for the merge tool."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input1": test_dir / "input1.vcf",
        "input2": test_dir / "input2.vcf",
        "expected_snakefile": test_dir / "expected_snakefile",
    }


def test_snakefile_merge(test_paths, tmp_path, capsys):
    """Test that merge generates the expected Snakefile."""
    from tools.bcftools.merge.run_merge import run_merge

    temp_output = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_merge(
        input_files=[str(test_paths["input1"]), str(test_paths["input2"])],
        output=str(temp_output),
        output_type="v",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile elements
    assert "rule merge:" in content, "Missing Snakefile rule definition"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    # Verify inputs/outputs from meta.yaml
    assert str(test_paths["input1"]) in content, "Input1 file is missing in Snakefile"
    assert str(test_paths["input2"]) in content, "Input2 file is missing in Snakefile"
    assert str(temp_output) in content, "Output file is missing in Snakefile"
    # Additional params verification
    assert "output_type=" in content, "Missing output_type parameter"
    assert "threads=" in content, "Missing threads parameter"


def test_run_merge(test_paths, tmp_path):
    """Test that merge can be run with valid test files."""
    from tools.bcftools.merge.run_merge import run_merge

    temp_output = tmp_path / "output.vcf"

    # Execute the merge process
    result = run_merge(
        input_files=[str(test_paths["input1"]), str(test_paths["input2"])],
        output=str(temp_output),
        output_type="v",
        threads=2,
    )

    # Verify that the process completes successfully
    assert result.returncode == 0, "Merge run failed with non-zero return code"
    assert temp_output.exists(), "Output file was not created"
    # Further checks can be added to validate output content if needed
