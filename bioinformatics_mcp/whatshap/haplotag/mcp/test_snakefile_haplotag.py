import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "vcf": test_dir / "test.vcf.gz",
        "vcf_index": test_dir / "test.vcf.gz.tbi",
        "aln": test_dir / "test.bam",
        "aln_index": test_dir / "test.bam.bai",
        "ref": test_dir / "test.fasta",
        "ref_index": test_dir / "test.fasta.fai",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_haplotag(test_paths, tmp_path, capsys):
    """Test that haplotag generates the expected Snakefile."""
    from bioinformatics_mcp.whatshap.haplotag.mcp.run_haplotag import run_haplotag

    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_haplotag(
        vcf=str(test_paths["vcf"]),
        vcf_index=str(test_paths["vcf_index"]),
        aln=str(test_paths["aln"]),
        aln_index=str(test_paths["aln_index"]),
        ref=str(test_paths["ref"]),
        ref_index=str(test_paths["ref_index"]),
        output=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule haplotag:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify required inputs
    assert "vcf=" in content, "Missing vcf parameter"
    assert "vcf_index=" in content, "Missing vcf_index parameter"
    assert "aln=" in content, "Missing aln parameter"
    assert "aln_index=" in content, "Missing aln_index parameter"
    assert "ref=" in content, "Missing ref parameter"
    assert "ref_index=" in content, "Missing ref_index parameter"

    # Verify outputs
    assert "output=" in content, "Missing output parameter"


def test_run_haplotag(test_paths, tmp_path):
    """Test that haplotag can be run with the test files."""
    from bioinformatics_mcp.whatshap.haplotag.mcp.run_haplotag import run_haplotag

    temp_output = tmp_path / "output.bam"

    result = run_haplotag(
        vcf=str(test_paths["vcf"]),
        vcf_index=str(test_paths["vcf_index"]),
        aln=str(test_paths["aln"]),
        aln_index=str(test_paths["aln_index"]),
        ref=str(test_paths["ref"]),
        ref_index=str(test_paths["ref_index"]),
        output=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "haplotag run failed"
    assert temp_output.exists(), "Output BAM file was not created"
