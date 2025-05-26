import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "microsatellite_list": test_dir / "microsatellite_list.txt",
        "normal_bam": test_dir / "normal.bam",
        "tumor_bam": test_dir / "tumor.bam",
        "msi_score_output": test_dir / "msi_score_output.txt",
        "read_count_distribution_output": test_dir / "read_count_distribution.tsv",
        "somatic_sites_output": test_dir / "somatic_sites.tsv",
        "germline_sites_output": test_dir / "germline_sites.tsv",
    }


def test_snakefile_msi(test_paths, tmp_path, capsys):
    """Test that the msi tool generates the correct Snakefile."""
    from tools.msisensor.mcp.run_msi import run_msi

    run_msi(
        microsatellite_list=str(test_paths["microsatellite_list"]),
        normal_bam=str(test_paths["normal_bam"]),
        tumor_bam=str(test_paths["tumor_bam"]),
        msi_score_output=str(test_paths["msi_score_output"]),
        read_count_distribution_output=str(
            test_paths["read_count_distribution_output"]
        ),
        somatic_sites_output=str(test_paths["somatic_sites_output"]),
        germline_sites_output=str(test_paths["germline_sites_output"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile elements
    assert "rule msi:" in content, "Missing rule definition for msi"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Check required inputs
    assert "microsatellite_list=" in content, (
        "Missing microsatellite_list input in Snakefile"
    )
    assert "normal_bam=" in content, "Missing normal_bam input in Snakefile"
    assert "tumor_bam=" in content, "Missing tumor_bam input in Snakefile"

    # Check required outputs
    assert "msi_score_output=" in content, "Missing msi_score_output in Snakefile"
    assert "read_count_distribution_output=" in content, (
        "Missing read_count_distribution_output in Snakefile"
    )
    assert "somatic_sites_output=" in content, (
        "Missing somatic_sites_output in Snakefile"
    )
    assert "germline_sites_output=" in content, (
        "Missing germline_sites_output in Snakefile"
    )


def test_run_msi(test_paths, tmp_path):
    """Test the execution of the msi tool with test files."""
    from tools.msisensor.mcp.run_msi import run_msi

    msi_score_output = tmp_path / "msi_score_output.txt"
    read_count_distribution_output = tmp_path / "read_count_distribution.tsv"
    somatic_sites_output = tmp_path / "somatic_sites.tsv"
    germline_sites_output = tmp_path / "germline_sites.tsv"

    result = run_msi(
        microsatellite_list=str(test_paths["microsatellite_list"]),
        normal_bam=str(test_paths["normal_bam"]),
        tumor_bam=str(test_paths["tumor_bam"]),
        msi_score_output=str(msi_score_output),
        read_count_distribution_output=str(read_count_distribution_output),
        somatic_sites_output=str(somatic_sites_output),
        germline_sites_output=str(germline_sites_output),
    )

    # Verify that the execution was successful
    assert result.returncode == 0, "msi tool execution failed"

    # Verify the expected output files are created
    assert msi_score_output.exists(), "MSI score output file not created"
    assert read_count_distribution_output.exists(), (
        "Read count distribution output file not created"
    )
    assert somatic_sites_output.exists(), "Somatic sites output file not created"
    assert germline_sites_output.exists(), "Germline sites output file not created"
