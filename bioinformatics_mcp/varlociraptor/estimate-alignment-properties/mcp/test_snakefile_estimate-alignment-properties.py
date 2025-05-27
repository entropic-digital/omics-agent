import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "tests"
    return {
        "reference_genome": test_dir / "reference.fa",
        "read_alignment1": test_dir / "read1.bam",
        "read_alignment2": test_dir / "read2.bam",
        "alignment_properties": test_dir / "alignment_properties.json",
    }


def test_snakefile_estimate_alignment_properties(test_paths, tmp_path, capsys):
    """Test that estimate-alignment-properties generates the expected Snakefile."""
    from bioinformatics_mcp.varlociraptor.estimate_alignment_properties.mcp.run_estimate_alignment_properties import run_estimate_alignment_properties

    temp_output = tmp_path / "alignment_properties.json"

    run_estimate_alignment_properties(
        reference_genome=str(test_paths["reference_genome"]),
        read_alignments=[
            str(test_paths["read_alignment1"]),
            str(test_paths["read_alignment2"]),
        ],
        alignment_properties=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule estimate_alignment_properties:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "reference_genome=" in content, "Missing reference_genome parameter"
    assert "read_alignments=" in content, "Missing read_alignments parameter"
    assert "alignment_properties=" in content, "Missing alignment_properties parameter"


def test_run_estimate_alignment_properties(test_paths, tmp_path):
    """Test that estimate-alignment-properties can be run with the test files."""
    from bioinformatics_mcp.varlociraptor.estimate_alignment_properties.mcp.run_estimate_alignment_properties import run_estimate_alignment_properties

    temp_output = tmp_path / "alignment_properties.json"

    result = run_estimate_alignment_properties(
        reference_genome=str(test_paths["reference_genome"]),
        read_alignments=[
            str(test_paths["read_alignment1"]),
            str(test_paths["read_alignment2"]),
        ],
        alignment_properties=str(temp_output),
    )

    assert result.returncode == 0, "estimate-alignment-properties run failed"
    assert temp_output.exists(), "Expected output file was not created"