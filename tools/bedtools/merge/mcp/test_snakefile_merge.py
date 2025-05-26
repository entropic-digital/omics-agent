"""Module that tests if the merge Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "input1": test_dir / "input1.bed",
        "input2": test_dir / "input2.bed",
        "expected_output": test_dir / "expected_output.bed",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_merge(test_paths, tmp_path, capsys):
    """Test that merge generates the expected Snakefile."""
    from tools.bedtools.merge.run_merge import run_merge

    temp_output = tmp_path / "output.bed"

    # Generate the Snakefile with print_only=True to capture the content
    run_merge(
        input=[str(test_paths["input1"]), str(test_paths["input2"])],
        output=str(temp_output),
        extra=None,
        threads=1,
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule merge:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"input={str(test_paths['input1'])}" in content, (
        "Missing correct input file path"
    )
    assert f"input={str(test_paths['input2'])}" in content, (
        "Missing correct input file path"
    )
    assert f"output={str(temp_output)}" in content, "Missing correct output file path"


def test_run_merge(test_paths, tmp_path):
    """Test that merge can be run with the test files."""
    from tools.bedtools.merge.run_merge import run_merge

    temp_output = tmp_path / "output.bed"

    result = run_merge(
        input=[str(test_paths["input1"]), str(test_paths["input2"])],
        output=str(temp_output),
        extra=None,
        threads=1,
    )

    # Verify the process was successful
    assert result.returncode == 0, "Run failed, non-zero return code"
    assert temp_output.exists(), "Output file was not created"

    # Verify that output matches the expected result
    with (
        open(temp_output) as output_file,
        open(test_paths["expected_output"]) as expected_file,
    ):
        assert output_file.read() == expected_file.read(), (
            "Output file content does not match expected content"
        )
