import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Fixture to manage test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "test_encode_assay_accession": "ENCSRXXXXX",
        "test_encode_file_accession": "ENCFFXXXXX",
        "test_output": test_dir / "test_output.fastq.gz",
        "expected_snakefile": test_dir / "expected_snakefile.fastq"
    }


def test_snakefile_encode_fastq_downloader(test_paths, tmp_path, capsys):
    """Test the Snakefile generation for encode_fastq_downloader."""
    from bioinformatics_mcp.encode_fastq_downloader.run_encode_fastq_downloader import run_encode_fastq_downloader
    temp_output = tmp_path / "output.fastq.gz"

    # Generate the Snakefile using print_only=True to capture the content
    run_encode_fastq_downloader(
        encode_assay_accession=test_paths["test_encode_assay_accession"],
        output_file=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    assert "rule encode_fastq_downloader:" in content, "Missing `rule` section in Snakefile"
    assert "input:" in content, "Missing `input` section in Snakefile"
    assert "output:" in content, "Missing `output` section in Snakefile"
    assert "wrapper:" in content, "Missing `wrapper` section in Snakefile"
    assert "encode_assay_accession=" in content or "encode_file_accession=" in content, "Missing ENCODE accession parameter(s)"
    assert "output_file=" in content, "Missing `output_file` parameter in Snakefile"


def test_run_encode_fastq_downloader(test_paths, tmp_path):
    """Test the execution of encode_fastq_downloader with test inputs."""
    from bioinformatics_mcp.encode_fastq_downloader.run_encode_fastq_downloader import run_encode_fastq_downloader
    temp_output = tmp_path / "output.fastq.gz"

    result = run_encode_fastq_downloader(
        encode_assay_accession=test_paths["test_encode_assay_accession"],
        output_file=str(temp_output)
    )

    # Verify the process completes successfully
    assert result.returncode == 0, "encode_fastq_downloader execution failed"
    assert temp_output.exists(), "Output file not created after execution"