import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "input_bam": test_dir / "test_input.bam",
        "output_bam": test_dir / "test_output.bam",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "umi_tag": "RX",
        "strategy": "adjacency",
    }


def test_snakefile_groupreadsbyumi(test_paths, tmp_path, capsys):
    """Test that groupreadsbyumi generates the expected Snakefile."""
    from bioinformatics_mcp.fgbio.groupreadsbyumi.mcp.run_groupreadsbyumi import run_groupreadsbyumi

    temp_output_bam = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_groupreadsbyumi(
        input_bam=str(test_paths["input_bam"]),
        output_bam=str(temp_output_bam),
        umi_tag=test_paths["umi_tag"],
        strategy=test_paths["strategy"],
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential parts of the generated Snakefile
    assert "rule groupreadsbyumi:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f"input_bam={test_paths['input_bam']}" in content, (
        "Missing input_bam parameter in Snakefile"
    )
    assert f"output_bam={temp_output_bam}" in content, (
        "Missing output_bam parameter in Snakefile"
    )
    assert f"umi_tag={test_paths['umi_tag']}" in content, (
        "Missing umi_tag parameter in Snakefile"
    )
    assert f"strategy={test_paths['strategy']}" in content, (
        "Missing strategy parameter in Snakefile"
    )


def test_run_groupreadsbyumi(test_paths, tmp_path):
    """Test that groupreadsbyumi can be run with the test files."""
    from bioinformatics_mcp.fgbio.groupreadsbyumi.mcp.run_groupreadsbyumi import run_groupreadsbyumi

    temp_output_bam = tmp_path / "output.bam"
    temp_output_stats = tmp_path / "output_stats.txt"

    result = run_groupreadsbyumi(
        input_bam=str(test_paths["input_bam"]),
        output_bam=str(temp_output_bam),
        output_stats=str(temp_output_stats),
        umi_tag=test_paths["umi_tag"],
        strategy=test_paths["strategy"],
        min_map_qual=10,
        annotate_family_size=True,
        family_size_threshold=5,
    )

    # Verify that the process ran successfully
    assert result.returncode == 0, "groupreadsbyumi tool execution failed"
    assert temp_output_bam.exists(), "Output BAM file was not created"
    assert temp_output_stats.exists(), "Output stats file was not created"
