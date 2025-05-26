import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam": test_dir / "test.bam",
        "intervals": test_dir / "test.intervals",
        "ref": test_dir / "test.fa",
        "counts": test_dir / "test.counts",
    }


def test_snakefile_collectalleliccounts(test_paths, tmp_path, capsys):
    """Test that collectalleliccounts generates the expected Snakefile."""
    from tools.collectalleliccounts.mcp.run_collectalleliccounts import run_collectalleliccounts

    # Generate the Snakefile with print_only=True
    run_collectalleliccounts(
        bam=str(test_paths["bam"]),
        intervals=str(test_paths["intervals"]),
        ref=str(test_paths["ref"]),
        counts=str(tmp_path / "output.counts"),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify Snakefile structure
    assert "rule collectalleliccounts:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input definition in Snakefile"
    assert "output:" in content, "Missing output definition in Snakefile"
    assert "wrapper:" in content, "Missing wrapper definition in Snakefile"

    # Verify required inputs from meta.yaml
    assert "bam=" in content, "Missing BAM input parameter in Snakefile"
    assert "intervals=" in content, "Missing intervals input parameter in Snakefile"
    assert "ref=" in content, "Missing reference input parameter in Snakefile"

    # Verify required output from meta.yaml
    assert "counts=" in content, "Missing counts output parameter in Snakefile"

    # Verify wrapper path
    assert "file:tools/gatk/collectalleliccounts" in content, "Incorrect wrapper path in Snakefile"


def test_run_collectalleliccounts(test_paths, tmp_path):
    """Test that collectalleliccounts can be executed successfully."""
    from tools.collectalleliccounts.mcp.run_collectalleliccounts import run_collectalleliccounts

    output_file = tmp_path / "output.counts"

    # Run the tool
    result = run_collectalleliccounts(
        bam=str(test_paths["bam"]),
        intervals=str(test_paths["intervals"]),
        ref=str(test_paths["ref"]),
        counts=str(output_file),
    )

    # Verify that the process completes successfully
    assert result.returncode == 0, "collectalleliccounts run failed"

    # Verify the output file is created
    assert output_file.exists(), "Output file was not created"

    # Optionally, verify the output file content (example check)
    with output_file.open() as f:
        content = f.read()
        assert "CONTIG" in content, "Expected header not found in output file"
        assert "POSITION" in content, "Expected header not found in output file"
        assert "REF_COUNT" in content, "Expected header not found in output file"
        assert "ALT_COUNT" in content, "Expected header not found in output file"