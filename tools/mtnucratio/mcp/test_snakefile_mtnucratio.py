"""Module that tests if the mtnucratio Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "test.bam",
        "chrom": "chrM",
        "expected_json": test_dir / "expected_output.json",
        "expected_txt": test_dir / "expected_output.txt",
    }


def test_snakefile_mtnucratio(test_paths, tmp_path, capsys):
    """Test that mtnucratio generates the expected Snakefile."""
    from tools.mtnucratio.mcp.run_mtnucratio import run_mtnucratio

    # Generate the Snakefile with print_only=True to capture the content
    run_mtnucratio(
        bam_file=str(test_paths["bam_file"]),
        chrom=test_paths["chrom"],
        json=tmp_path / "output.json",
        txt=tmp_path / "output.txt",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential Snakemake rule parts
    assert "rule mtnucratio:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify the inputs as described in the meta.yaml
    assert "bam_file=" in content, "Missing bam_file input parameter"

    # Verify the outputs as described in the meta.yaml
    assert "'json':" in content, "Missing JSON output parameter"
    assert "'txt':" in content, "Missing TXT output parameter"

    # Verify the params as described in the meta.yaml
    assert "chrom=" in content, "Missing chrom parameter in params"


def test_run_mtnucratio(test_paths, tmp_path):
    """Test that mtnucratio can be run with the provided test files."""
    from tools.mtnucratio.mcp.run_mtnucratio import run_mtnucratio

    temp_json = tmp_path / "output.json"
    temp_txt = tmp_path / "output.txt"

    result = run_mtnucratio(
        bam_file=str(test_paths["bam_file"]),
        chrom=test_paths["chrom"],
        json=str(temp_json),
        txt=str(temp_txt),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "MTNucRatioCalculator run failed"

    # Verify that the output files are created
    assert temp_json.exists(), "Expected JSON output file was not generated"
    assert temp_txt.exists(), "Expected TXT output file was not generated"
