import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reference_genome": test_dir / "reference_genome.fasta",
        "target_genome": test_dir / "target_genome.fasta",
        "annotations": test_dir / "annotations.gff",
        "mapped_annotations": test_dir / "mapped_annotations.gff",
        "unmapped_annotations": test_dir / "unmapped_annotations.gff",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_liftoff(test_paths, tmp_path, capsys):
    """Test that liftoff generates the expected Snakefile."""
    from bioinformatics_mcp.liftoff.mcp.run_liftoff import run_liftoff
    temp_mapped = tmp_path / "mapped_annotations.gff"
    temp_unmapped = tmp_path / "unmapped_annotations.gff"

    # Generate the Snakefile with print_only=True to capture the content
    run_liftoff(
        reference_genome=str(test_paths["reference_genome"]),
        target_genome=str(test_paths["target_genome"]),
        annotations=str(test_paths["annotations"]),
        mapped_annotations=str(temp_mapped),
        unmapped_annotations=str(temp_unmapped),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify all required rule elements are present in the Snakefile
    assert "rule liftoff:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    
    # Verify all required input parameters
    assert "reference_genome=" in content, "Missing reference_genome parameter"
    assert "target_genome=" in content, "Missing target_genome parameter"
    assert "annotations=" in content, "Missing annotations parameter"
    
    # Verify all required output parameters
    assert "mapped_annotations=" in content, "Missing mapped_annotations parameter"
    assert "unmapped_annotations=" in content, "Missing unmapped_annotations parameter"


def test_run_liftoff(test_paths, tmp_path):
    """Test that liftoff can be run with the test files."""
    from bioinformatics_mcp.liftoff.mcp.run_liftoff import run_liftoff
    temp_mapped = tmp_path / "mapped_annotations.gff"
    temp_unmapped = tmp_path / "unmapped_annotations.gff"

    result = run_liftoff(
        reference_genome=str(test_paths["reference_genome"]),
        target_genome=str(test_paths["target_genome"]),
        annotations=str(test_paths["annotations"]),
        mapped_annotations=str(temp_mapped),
        unmapped_annotations=str(temp_unmapped)
    )

    # Verify that the process completed successfully
    assert result.returncode == 0, "liftoff tool execution failed"
    # Verify that output files were created
    assert temp_mapped.exists(), "Mapped annotations output file not created"
    assert temp_unmapped.exists(), "Unmapped annotations output file not created"