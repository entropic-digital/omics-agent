import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "calls": test_dir / "test_calls.vcf",
        "dbnsfp_file": test_dir / "test_dbnsfp.txt",
        "annotated_calls": test_dir / "expected_annotated_calls.vcf",
    }


def test_snakefile_dbnsfp(test_paths, tmp_path, capsys):
    """Test that dbnsfp generates the expected Snakefile."""
    from bioinformatics_mcp.snpsift.dbnsfp.run_dbnsfp import run_dbnsfp
    temp_output = tmp_path / "annotated.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_dbnsfp(
        calls=str(test_paths["calls"]),
        dbnsfp_file=str(test_paths["dbnsfp_file"]),
        annotated_calls=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    snakefile_content = captured.out

    # Verify essential rule elements in the Snakefile
    assert "rule dbnsfp:" in snakefile_content, "Rule 'dbnsfp' is missing in Snakefile"
    assert "input:" in snakefile_content, "Input section is missing in Snakefile"
    assert "calls=" in snakefile_content, "Input 'calls' is missing in Snakefile"
    assert "dbnsfp_file=" in snakefile_content, "Input 'dbnsfp_file' is missing in Snakefile"
    assert "output:" in snakefile_content, "Output section is missing in Snakefile"
    assert "annotated_calls=" in snakefile_content, "Output 'annotated_calls' is missing in Snakefile"
    assert "wrapper:" in snakefile_content, "Wrapper definition is missing in Snakefile"
    assert "tools/snpsift/dbnsfp" in snakefile_content, "Wrapper path is missing or incorrect in Snakefile"


def test_run_dbnsfp(test_paths, tmp_path):
    """Test that dbnsfp can annotate calls with the test files."""
    from bioinformatics_mcp.snpsift.dbnsfp.run_dbnsfp import run_dbnsfp
    temp_output = tmp_path / "annotated.vcf"

    # Run the dbnsfp tool
    result = run_dbnsfp(
        calls=str(test_paths["calls"]),
        dbnsfp_file=str(test_paths["dbnsfp_file"]),
        annotated_calls=str(temp_output),
    )

    # Check the run result
    assert result.returncode == 0, "dbnsfp tool execution failed"
    assert temp_output.exists(), "Annotated output file was not created"
    assert temp_output.stat().st_size > 0, "Annotated output file is empty"

    # Compare output with expected annotated calls file if available
    if test_paths["annotated_calls"].exists():
        with open(temp_output, "r") as output, open(test_paths["annotated_calls"], "r") as expected:
            output_content = output.read()
            expected_content = expected.read()
            assert output_content == expected_content, "Tool output does not match expected annotated calls"