import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "test.bam",
        "reference_fasta": test_dir / "reference.fasta",
        "region": "chr1:1000-2000",
        "expected_snakefile": test_dir / "Snakefile",
        "expected_output": test_dir / "expected_output.pileup",
    }


def test_snakefile_mpileup(test_paths, tmp_path, capsys):
    """Test that mpileup generates the expected Snakefile."""
    from bioinformatics_mcp.samtools.mpileup.mcp.run_mpileup import run_mpileup

    temp_output = tmp_path / "output.pileup"

    # Generate the Snakefile with print_only=True to capture the content
    run_mpileup(
        bam_file=str(test_paths["bam_file"]),
        reference_fasta=str(test_paths["reference_fasta"]),
        region=test_paths["region"],
        output_path=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule mpileup:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam_file=" in content, "Missing bam_file parameter"
    assert "reference_fasta=" in content, "Missing reference_fasta parameter"
    assert "output_path=" in content, "Missing output_path parameter"
    assert f"'{test_paths['region']}'" in content, "Missing region parameter"


def test_run_mpileup(test_paths, tmp_path):
    """Test that mpileup can be run with the test files."""
    from bioinformatics_mcp.samtools.mpileup.mcp.run_mpileup import run_mpileup

    temp_output = tmp_path / "output.pileup"

    result = run_mpileup(
        bam_file=str(test_paths["bam_file"]),
        reference_fasta=str(test_paths["reference_fasta"]),
        region=test_paths["region"],
        output_path=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "mpileup run failed"

    # Verify that the output file is created
    assert temp_output.exists(), "Output pileup file was not created"

    # Verify the output is not empty
    assert temp_output.stat().st_size > 0, "Output pileup file is empty"
