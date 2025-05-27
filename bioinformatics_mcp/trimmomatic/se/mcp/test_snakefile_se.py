"""Module that tests if the trimmomatic_se Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths for trimmomatic_se tool."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_fastq": test_dir / "test_input.fastq",
        "adapter_sequences": test_dir / "test_adapters.fa",
        "expected_output_fastq": test_dir / "expected_output.fastq",
    }


def test_snakefile_se(test_paths, tmp_path, capsys):
    """Test that trimmomatic_se generates the expected Snakefile."""
    from bioinformatics_mcp.trimmomatic_se.mcp.run_se import run_se

    temp_output_fastq = tmp_path / "output.fastq"

    # Generate the Snakefile with print_only=True to capture the content
    run_se(
        input_fastq=str(test_paths["input_fastq"]),
        output_fastq=str(temp_output_fastq),
        adapter_sequences=str(test_paths["adapter_sequences"]),
        min_length=36,
        phred_quality=20,
        threads=4,
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule trimmomatic_se:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "input_fastq=" in content, "Missing input_fastq parameter"
    assert "output_fastq=" in content, "Missing output_fastq parameter"
    assert "adapter_sequences=" in content, "Missing adapter_sequences parameter"
    assert "min_length=" in content, "Missing min_length parameter"
    assert "phred_quality=" in content, "Missing phred_quality parameter"
    assert "threads=" in content, "Missing threads parameter"


def test_run_se(test_paths, tmp_path):
    """Test that trimmomatic_se can be run with the test files."""
    from bioinformatics_mcp.trimmomatic_se.mcp.run_se import run_se

    temp_output_fastq = tmp_path / "output.fastq"

    result = run_se(
        input_fastq=str(test_paths["input_fastq"]),
        output_fastq=str(temp_output_fastq),
        adapter_sequences=str(test_paths["adapter_sequences"]),
        min_length=36,
        phred_quality=20,
        threads=4,
    )

    # Verify that the run is successful
    assert result.returncode == 0, "trimmomatic_se execution failed"

    # Optionally, verify output file creation and correctness
    assert temp_output_fastq.exists(), "Expected output FASTQ file was not created"
