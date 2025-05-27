import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "mcool_file": test_dir / "test.mcool",
        "view_file": test_dir / "test_view.bed",
        "output_tsv": test_dir / "test_output.tsv",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_expected_cis(test_paths, tmp_path, capsys):
    """Test that expected_cis generates the expected Snakefile."""
    from bioinformatics_mcp.cooltools.expected_cis.run_expected_cis import run_expected_cis
    temp_output = tmp_path / "output.tsv"

    # Generate the Snakefile with print_only=True to capture the content
    run_expected_cis(
        mcool_file=str(test_paths["mcool_file"]),
        output_tsv=str(temp_output),
        view=str(test_paths["view_file"]),
        resolution=10000,
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule expected_cis:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Add assertions for all required input parameters
    assert "mcool_file=" in content, "Missing mcool_file parameter in input section"
    assert "view=" in content, "Missing view parameter in input section"
    # Add assertions for all required output parameters
    assert "output_tsv=" in content, "Missing output_tsv parameter in output section"
    # Add assertions for required params
    assert "resolution=10000" in content, "Missing resolution parameter in params section"


def test_run_expected_cis(test_paths, tmp_path):
    """Test that expected_cis can be run with the test files."""
    from bioinformatics_mcp.cooltools.expected_cis.run_expected_cis import run_expected_cis
    temp_output = tmp_path / "output.tsv"

    result = run_expected_cis(
        mcool_file=str(test_paths["mcool_file"]),
        output_tsv=str(temp_output),
        view=str(test_paths["view_file"]),
        resolution=10000,
    )

    # Verify that the run is successful
    assert result.returncode == 0, "expected_cis run failed"
    # Verify the output file is created
    assert temp_output.exists(), "Output TSV file was not created"
    # Additional verification of output content can be added if format/content expectations are known