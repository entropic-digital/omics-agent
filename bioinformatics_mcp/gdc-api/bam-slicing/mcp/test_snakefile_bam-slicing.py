import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_uuid": test_dir / "sample_bam_uuid.txt",
        "gdc_token": test_dir / "gdc_access_token.txt",
        "output": test_dir / "output.bam",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_bam_slicing(test_paths, tmp_path, capsys):
    """Test that bam-slicing generates the expected Snakefile."""
    from bioinformatics_mcp.gdc_api.bam_slicing.run_bam_slicing import run_bam_slicing

    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_bam_slicing(
        bam_uuid=str(test_paths["bam_uuid"]),
        gdc_token=str(test_paths["gdc_token"]),
        output=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential parts of the Snakefile are present
    assert "rule bam-slicing:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam_uuid=" in content, "Missing bam_uuid parameter"
    assert "gdc_token=" in content, "Missing gdc_token parameter"
    assert "output=" in content, "Missing output parameter"


def test_run_bam_slicing(test_paths, tmp_path):
    """Test that bam-slicing can be run with the test files."""
    from bioinformatics_mcp.gdc_api.bam_slicing.run_bam_slicing import run_bam_slicing

    temp_output = tmp_path / "output.bam"

    result = run_bam_slicing(
        bam_uuid=str(test_paths["bam_uuid"]),
        gdc_token=str(test_paths["gdc_token"]),
        output=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "bam-slicing run failed"
    # Ensure output file is created
    assert temp_output.exists(), "Output BAM file was not created"
