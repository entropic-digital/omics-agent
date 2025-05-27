import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "example.bam",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "expected_output": test_dir / "expected.flagstat",
    }


def test_snakefile_flagstat(test_paths, tmp_path, capsys):
    """Test that the flagstat Snakefile is generated correctly."""
    from bioinformatics_mcp.samtools.flagstat.run_flagstat import run_flagstat

    temp_output = tmp_path / "output.flagstat"

    # Generate the Snakefile with print_only=True
    run_flagstat(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify required rule elements in the Snakefile
    assert "rule flagstat:" in content, "Missing rule definition for flagstat."
    assert "input:" in content, "Missing input section in the Snakefile."
    assert "output:" in content, "Missing output section in the Snakefile."
    assert "wrapper:" in content, "Missing wrapper declaration in the Snakefile."
    assert f"input_file='{test_paths['input_file']}'" in content, (
        "Input file path is incorrect or missing."
    )
    assert f"output_file='{temp_output}'" in content, (
        "Output file path is incorrect or missing."
    )


def test_run_flagstat(test_paths, tmp_path):
    """Test that the flagstat tool can be executed successfully."""
    from bioinformatics_mcp.samtools.flagstat.run_flagstat import run_flagstat

    temp_output = tmp_path / "output.flagstat"

    # Run the tool
    result = run_flagstat(
        input_file=str(test_paths["input_file"]), output_file=str(temp_output)
    )

    # Verify the process executed correctly
    assert result.returncode == 0, "flagstat run failed with non-zero return code."

    # Verify the output file is created
    assert temp_output.exists(), "Output flagstat file was not created."

    # Optionally, compare the output content to the expected file
    with (
        temp_output.open() as generated,
        test_paths["expected_output"].open() as expected,
    ):
        assert generated.read() == expected.read(), (
            "Generated flagstat output does not match the expected output."
        )
