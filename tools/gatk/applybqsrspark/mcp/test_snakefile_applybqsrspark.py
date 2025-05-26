import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam": test_dir / "test.bam",
        "fasta": test_dir / "test.fasta",
        "recal_table": test_dir / "test.recal.table",
        "expected_snakefile": test_dir / "Snakefile",
        "output_bam": test_dir / "output.bam",
    }


def test_snakefile_applybqsrspark(test_paths, tmp_path, capsys):
    """Test that applybqsrspark generates the expected Snakefile."""
    from tools.gatk.applybqsrspark.mcp.run_applybqsrspark import run_applybqsrspark
    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_applybqsrspark(
        bam=str(test_paths["bam"]),
        fasta=str(test_paths["fasta"]),
        recal_table=str(test_paths["recal_table"]),
        output_bam=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify rule definition and sections
    assert "rule applybqsrspark:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify inputs
    assert f"bam={test_paths['bam']}" in content, "Missing BAM input in Snakefile"
    assert f"fasta={test_paths['fasta']}" in content, "Missing FASTA input in Snakefile"
    assert (
        f"recal_table={test_paths['recal_table']}" in content
    ), "Missing recalibration table input in Snakefile"

    # Verify outputs
    assert f"output_bam={temp_output}" in content, "Missing output BAM in Snakefile"

    # Verify wrapper path
    assert (
        "wrapper: 'file:tools/gatk/applybqsrspark'" in content
    ), "Missing or incorrect wrapper path in Snakefile"


def test_run_applybqsrspark(test_paths, tmp_path):
    """Test that applybqsrspark can be run with the test files."""
    from tools.gatk.applybqsrspark.mcp.run_applybqsrspark import run_applybqsrspark
    temp_output = tmp_path / "output.bam"

    result = run_applybqsrspark(
        bam=str(test_paths["bam"]),
        fasta=str(test_paths["fasta"]),
        recal_table=str(test_paths["recal_table"]),
        output_bam=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "applybqsrspark run failed"

    # Verify that the output file was generated
    assert temp_output.exists(), "Output BAM file was not generated"
