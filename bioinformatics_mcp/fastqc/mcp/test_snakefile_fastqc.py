import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test_data"
    return {
        "fastq_file": test_dir / "test.fastq",
        "html_file": test_dir / "output.html",
        "zip_file": test_dir / "output.zip",
    }


def test_snakefile_fastqc(test_paths, tmp_path, capsys):
    """Test that fastqc generates the expected Snakefile."""
    from bioinformatics_mcp.fastqc.mcp.run_fastqc import run_fastqc

    temp_html = tmp_path / "output.html"
    temp_zip = tmp_path / "output.zip"

    # Generate the Snakefile with print_only=True to capture the content
    run_fastqc(
        fastq_file=str(test_paths["fastq_file"]),
        html_file=str(temp_html),
        zip_file=str(temp_zip),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential components of the Snakefile
    assert "rule fastqc:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Validate inputs and outputs
    assert f"fastq='{test_paths['fastq_file']}'" in content, (
        "Missing FASTQ input parameter"
    )
    assert f"html='{temp_html}'" in content, "Missing HTML output parameter"
    assert f"zip='{temp_zip}'" in content, "Missing ZIP output parameter"


def test_run_fastqc(test_paths, tmp_path):
    """Test that fastqc can be run with the test files."""
    from bioinformatics_mcp.fastqc.mcp.run_fastqc import run_fastqc

    temp_html = tmp_path / "output.html"
    temp_zip = tmp_path / "output.zip"

    # Run the tool
    result = run_fastqc(
        fastq_file=str(test_paths["fastq_file"]),
        html_file=str(temp_html),
        zip_file=str(temp_zip),
    )

    # Verify the process completed successfully
    assert result.returncode == 0, "fastqc run failed"

    # Verify output files are created
    assert temp_html.exists(), "HTML output file was not created"
    assert temp_zip.exists(), "ZIP output file was not created"
