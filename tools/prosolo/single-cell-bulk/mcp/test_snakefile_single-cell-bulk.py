import pytest
from pathlib import Path
from tools.prosolo.single_cell_bulk import run_single_cell_bulk


@pytest.fixture
def test_paths():
    """Set up test paths for single-cell-bulk."""
    base_dir = Path(__file__).parent / "test_data"
    return {
        "single_cell_bam": base_dir / "single_cell.bam",
        "single_cell_bam_index": base_dir / "single_cell.bai",
        "bulk_bam": base_dir / "bulk.bam",
        "bulk_bam_index": base_dir / "bulk.bai",
        "reference_genome": base_dir / "reference.fasta",
        "reference_genome_index": base_dir / "reference.fasta.fai",
        "candidate_sites": base_dir / "candidate_sites.vcf",
        "expected_snakefile": base_dir / "expected_snakefile",
        "output_bcf": base_dir / "output.bcf",
    }


def test_snakefile_single_cell_bulk(test_paths, tmp_path, capsys):
    """Test that single-cell-bulk generates the expected Snakefile."""
    temp_output = tmp_path / "output.bcf"

    # Generate the Snakefile with print_only=True
    run_single_cell_bulk(
        single_cell_bam=str(test_paths["single_cell_bam"]),
        single_cell_bam_index=str(test_paths["single_cell_bam_index"]),
        bulk_bam=str(test_paths["bulk_bam"]),
        bulk_bam_index=str(test_paths["bulk_bam_index"]),
        reference_genome=str(test_paths["reference_genome"]),
        reference_genome_index=str(test_paths["reference_genome_index"]),
        candidate_sites=str(test_paths["candidate_sites"]),
        output_bcf=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Validate essential elements of the Snakefile
    assert "rule single_cell_bulk:" in content, "Missing rule 'single_cell_bulk'"
    assert "input:" in content, "Missing 'input' section"
    assert "output:" in content, "Missing 'output' section"
    assert "wrapper:" in content, "Missing 'wrapper' directive"

    # Validate required inputs
    assert "single_cell_bam=" in content, "Missing 'single_cell_bam' input"
    assert "single_cell_bam_index=" in content, "Missing 'single_cell_bam_index' input"
    assert "bulk_bam=" in content, "Missing 'bulk_bam' input"
    assert "bulk_bam_index=" in content, "Missing 'bulk_bam_index' input"
    assert "reference_genome=" in content, "Missing 'reference_genome' input"
    assert "reference_genome_index=" in content, (
        "Missing 'reference_genome_index' input"
    )
    assert "candidate_sites=" in content, "Missing 'candidate_sites' input"

    # Validate required outputs
    assert "output_bcf=" in content, "Missing 'output_bcf' output"


def test_run_single_cell_bulk(test_paths, tmp_path):
    """Test that single-cell-bulk can be executed successfully with test inputs."""
    temp_output = tmp_path / "output.bcf"

    # Run the single_cell_bulk tool
    result = run_single_cell_bulk(
        single_cell_bam=str(test_paths["single_cell_bam"]),
        single_cell_bam_index=str(test_paths["single_cell_bam_index"]),
        bulk_bam=str(test_paths["bulk_bam"]),
        bulk_bam_index=str(test_paths["bulk_bam_index"]),
        reference_genome=str(test_paths["reference_genome"]),
        reference_genome_index=str(test_paths["reference_genome_index"]),
        candidate_sites=str(test_paths["candidate_sites"]),
        output_bcf=str(temp_output),
    )

    # Assert run was successful
    assert result.returncode == 0, "single-cell-bulk execution failed"
    assert temp_output.exists(), "Output BCF file was not generated"
