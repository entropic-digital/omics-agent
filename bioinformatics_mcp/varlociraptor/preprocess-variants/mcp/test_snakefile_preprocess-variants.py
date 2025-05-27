import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reference_genome": test_dir / "reference_genome.fa",
        "read_alignments": test_dir / "read_alignments.bam",
        "varlociraptor_alignment_properties": test_dir / "varlociraptor_alignment_properties.json",
        "candidate_variants": test_dir / "candidate_variants.vcf",
        "expected_preprocessed_variants": test_dir / "expected_preprocessed_variants.vcf",
    }


def test_snakefile_preprocess_variants(test_paths, tmp_path, capsys):
    """Test that preprocess-variants generates the expected Snakefile."""
    from bioinformatics_mcp.varlociraptor.preprocess_variants.mcp.run_preprocess_variants import run_preprocess_variants
    temp_output = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_preprocess_variants(
        reference_genome=str(test_paths["reference_genome"]),
        read_alignments=str(test_paths["read_alignments"]),
        varlociraptor_alignment_properties=str(test_paths["varlociraptor_alignment_properties"]),
        candidate_variants=str(test_paths["candidate_variants"]),
        preprocessed_variants=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule preprocess_variants:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Assert all required input parameters are present
    assert "reference_genome=" in content, "Missing 'reference_genome' input"
    assert "read_alignments=" in content, "Missing 'read_alignments' input"
    assert "varlociraptor_alignment_properties=" in content, "Missing 'varlociraptor_alignment_properties' input"
    assert "candidate_variants=" in content, "Missing 'candidate_variants' input"
    # Assert output is defined
    assert "preprocessed_variants=" in content, "Missing 'preprocessed_variants' output"


def test_run_preprocess_variants(test_paths, tmp_path):
    """Test that preprocess-variants can be run with the test files."""
    from bioinformatics_mcp.varlociraptor.preprocess_variants.mcp.run_preprocess_variants import run_preprocess_variants
    temp_output = tmp_path / "preprocessed_variants.vcf"

    # Run tool
    result = run_preprocess_variants(
        reference_genome=str(test_paths["reference_genome"]),
        read_alignments=str(test_paths["read_alignments"]),
        varlociraptor_alignment_properties=str(test_paths["varlociraptor_alignment_properties"]),
        candidate_variants=str(test_paths["candidate_variants"]),
        preprocessed_variants=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "preprocess_variants run failed"
    # Verify that the output file is created
    assert temp_output.exists(), "Preprocessed variants file was not created"
    # Additional checks can compare temp_output with expected_preprocessed_variants, if available