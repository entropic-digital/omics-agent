import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam": test_dir / "test.bam",
        "reference": test_dir / "test_reference.fasta",
        "reads": test_dir / "test_reads.fastq",
        "r1": test_dir / "test_r1.fastq",
        "r2": test_dir / "test_r2.fastq",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_bazam(test_paths, tmp_path, capsys):
    """Test that bazam generates the expected Snakefile."""
    from bioinformatics_mcp.bazam.mcp.run_bazam import run_bazam
    temp_output = tmp_path / "output.fastq"

    # Generate the Snakefile with print_only=True to capture the content
    run_bazam(
        bam=str(test_paths["bam"]),
        reference=str(test_paths["reference"]),
        reads=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule bazam:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam=" in content, "Missing bam parameter"
    assert "reference=" in content, "Missing reference parameter"
    assert "output.reads" in content, "Missing reads output parameter"


def test_run_bazam(test_paths, tmp_path):
    """Test that bazam can be run with the test files."""
    from bioinformatics_mcp.bazam.mcp.run_bazam import run_bazam
    temp_output = tmp_path / "output.fastq"

    result = run_bazam(
        bam=str(test_paths["bam"]),
        reference=str(test_paths["reference"]),
        reads=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "bazam run failed"
    assert temp_output.exists(), "Expected output FASTQ file not created"