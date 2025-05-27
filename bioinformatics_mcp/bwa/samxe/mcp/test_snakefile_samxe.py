import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fastq1": test_dir / "test_fastq1.fastq",
        "fastq2": test_dir / "test_fastq2.fastq",
        "sai1": test_dir / "test_sai1.sai",
        "sai2": test_dir / "test_sai2.sai",
        "idx": test_dir / "ref_index",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_samxe(test_paths, tmp_path, capsys):
    """Test that samxe generates the expected Snakefile."""
    from bioinformatics_mcp.bwa.samxe.run_samxe import run_samxe
    temp_output = tmp_path / "output.sam"

    # Generate the Snakefile with print_only=True
    run_samxe(
        fastq=[str(test_paths["fastq1"]), str(test_paths["fastq2"])],
        sai=[str(test_paths["sai1"]), str(test_paths["sai2"])],
        idx=str(test_paths["idx"]),
        output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the generated Snakefile
    assert "rule samxe:" in content, "Missing rule definition for samxe"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify required input parameters
    assert "fastq=" in content, "Missing 'fastq' parameter in Snakefile"
    assert "sai=" in content, "Missing 'sai' parameter in Snakefile"
    assert "idx=" in content, "Missing 'idx' parameter in Snakefile"

    # Verify required output parameters
    assert "output=" in content, "Missing output parameter in Snakefile"


def test_run_samxe(test_paths, tmp_path):
    """Test that samxe can be run with the test files."""
    from bioinformatics_mcp.bwa.samxe.run_samxe import run_samxe
    temp_output = tmp_path / "output.sam"

    # Run the tool with test inputs
    result = run_samxe(
        fastq=[str(test_paths["fastq1"]), str(test_paths["fastq2"])],
        sai=[str(test_paths["sai1"]), str(test_paths["sai2"])],
        idx=str(test_paths["idx"]),
        output=str(temp_output)
    )

    # Verify that the tool executed successfully
    assert result.returncode == 0, "samxe execution failed"
    assert temp_output.exists(), "Output SAM/BAM file was not created successfully"