"""Module that tests if the plass Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fastq1": test_dir / "test1.fastq",
        "fastq2": test_dir / "test2.fastq",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_plass(test_paths, tmp_path, capsys):
    """Test that plass generates the expected Snakefile."""
    from tools.plass.mcp.run_plass import run_plass

    output_fasta = tmp_path / "output.fasta"

    # Generate the Snakefile with print_only=True to capture the content
    run_plass(
        fastq_files=[str(test_paths["fastq1"]), str(test_paths["fastq2"])],
        output_fasta=str(output_fasta),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule plass:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert (
        f"fastq_files={str([str(test_paths['fastq1']), str(test_paths['fastq2'])])}"
        in content
    ), "Missing or incorrect fastq_files parameter"
    assert f"output_fasta={str(output_fasta)}" in content, (
        "Missing or incorrect output_fasta parameter"
    )


def test_run_plass(test_paths, tmp_path):
    """Test that plass can be run with the test files."""
    from tools.plass.mcp.run_plass import run_plass

    output_fasta = tmp_path / "output.fasta"

    result = run_plass(
        fastq_files=[str(test_paths["fastq1"]), str(test_paths["fastq2"])],
        output_fasta=str(output_fasta),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "Plass run failed"
    assert Path(output_fasta).exists(), "Output FASTA file not generated"
