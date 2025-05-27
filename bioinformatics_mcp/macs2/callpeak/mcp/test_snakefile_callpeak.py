import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_file": test_dir / "test_input.bam",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "expected_output": test_dir / "expected_output.xls",
    }


def test_snakefile_callpeak(test_paths, tmp_path, capsys):
    """Test that callpeak generates the expected Snakefile."""
    from bioinformatics_mcp.macs2.callpeak.run_callpeak import run_callpeak

    temp_output = tmp_path / "output.xls"

    # Generate the Snakefile with print_only=True to capture the content
    run_callpeak(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        broad=True,
        format="BAM",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the Snakefile
    assert "rule callpeak:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"input_file='{test_paths['input_file']}'" in content, (
        "Missing input_file parameter"
    )
    assert f"output_file='{temp_output}'" in content, "Missing output_file parameter"
    assert "broad=True" in content, "Missing broad parameter"
    assert "format='BAM'" in content, "Missing format parameter"


def test_run_callpeak(test_paths, tmp_path):
    """Test that callpeak can be run with the test files."""
    from bioinformatics_mcp.macs2.callpeak.run_callpeak import run_callpeak

    temp_output = tmp_path / "output.xls"

    # Execute the tool with test data
    result = run_callpeak(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        broad=True,
        format="BAM",
    )

    # Verify the run was successful
    assert result.returncode == 0, "callpeak execution failed"

    # Verify the output file is generated
    assert temp_output.exists(), "Output file not generated"

    # Optionally, compare content of output with expected
    with (
        open(test_paths["expected_output"], "r") as expected,
        open(temp_output, "r") as output,
    ):
        assert expected.read() == output.read(), (
            "Generated output does not match expected output"
        )
