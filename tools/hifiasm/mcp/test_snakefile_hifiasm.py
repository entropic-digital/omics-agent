import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "pacbio_hifi_reads": test_dir / "pacbio_hifi_reads.fasta",
        "hic_reads": test_dir / "hic_reads.fastq",
        "expected_snakefile": test_dir / "Snakefile_expected",
    }


def test_snakefile_hifiasm(test_paths, tmp_path, capsys):
    """Test that hifiasm generates the expected Snakefile."""
    from tools.hifiasm.mcp.run_hifiasm import run_hifiasm

    # Generate the Snakefile with print_only=True to capture the content
    run_hifiasm(
        pacbio_hifi_reads=str(test_paths["pacbio_hifi_reads"]),
        hic_reads=str(test_paths["hic_reads"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the Snakefile
    assert "rule hifiasm:" in content, "Missing rule definition in the Snakefile"
    assert "input:" in content, "Missing input section in the Snakefile"
    assert "output:" in content, "Missing output section in the Snakefile"
    assert "wrapper:" in content, "Missing wrapper usage in the Snakefile"

    # Verify all required inputs and outputs from the tool's meta.yaml
    assert "pacbio_hifi_reads=" in content, "Missing pacbio_hifi_reads parameter in the Snakefile"
    assert "hic_reads=" in content, "Missing hic_reads parameter in the Snakefile"
    assert "assembly graphs" in content, "Missing GFA output in the Snakefile"

    # Optionally compare with expected Snakefile (if an expected file exists)
    if test_paths["expected_snakefile"].exists():
        expected_content = test_paths["expected_snakefile"].read_text()
        assert content == expected_content, "Generated Snakefile does not match the expected content"


def test_run_hifiasm(test_paths, tmp_path):
    """Test that hifiasm can be run with the test files."""
    from tools.hifiasm.mcp.run_hifiasm import run_hifiasm

    temp_output = tmp_path / "output.gfa"

    # Execute the hifiasm tool with real inputs
    result = run_hifiasm(
        pacbio_hifi_reads=str(test_paths["pacbio_hifi_reads"]),
        hic_reads=str(test_paths["hic_reads"]),
        output=str(temp_output),
    )

    # Verify that the process completed successfully
    assert result.returncode == 0, "hifiasm run failed with non-zero exit code"

    # Check if output file is generated
    assert temp_output.exists(), "Output GFA file was not created by hifiasm"
    assert temp_output.stat().st_size > 0, "Output GFA file is empty"