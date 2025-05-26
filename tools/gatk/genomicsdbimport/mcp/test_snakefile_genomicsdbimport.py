import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "gvcf1": test_dir / "sample1.g.vcf",
        "gvcf2": test_dir / "sample2.g.vcf",
        "workspace": tmp_path / "test_workspace",
        "intervals": test_dir / "intervals.list",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_genomicsdbimport(test_paths, tmp_path, capsys):
    """Test that genomicsdbimport generates the expected Snakefile."""
    from tools.gatk.genomicsdbimport.mcp.run_genomicsdbimport import run_genomicsdbimport

    # Generate the Snakefile with print_only=True to capture the content
    run_genomicsdbimport(
        gvcf_files=[str(test_paths["gvcf1"]), str(test_paths["gvcf2"])],
        workspace=str(test_paths["workspace"]),
        intervals=str(test_paths["intervals"]),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule genomicsdbimport:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify input and output parameters
    assert "gvcf_files=" in content, "Missing gvcf_files parameter"
    assert "workspace=" in content, "Missing workspace parameter"
    assert "intervals=" in content, "Missing intervals parameter"


def test_run_genomicsdbimport(test_paths, tmp_path):
    """Test that genomicsdbimport can be run with the test files."""
    from tools.gatk.genomicsdbimport.mcp.run_genomicsdbimport import run_genomicsdbimport

    # Prepare workspace folder
    workspace = tmp_path / "genomicsdb_workspace"

    result = run_genomicsdbimport(
        gvcf_files=[str(test_paths["gvcf1"]), str(test_paths["gvcf2"])],
        workspace=str(workspace),
        intervals=str(test_paths["intervals"])
    )

    # Verify that the run is successful
    assert result.returncode == 0, "genomicsdbimport run failed"

    # Verify workspace is created
    assert workspace.exists(), "Workspace folder was not created"