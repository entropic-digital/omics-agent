"""Module that tests if the hmmbuild Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_files"
    return {
        "sequence_alignment_file": base_dir / "alignment.fa",
        "expected_hmm_output": base_dir / "expected_output.hmm",
    }


def test_snakefile_hmmbuild(test_paths, tmp_path, capsys):
    """Test that hmmbuild generates the expected Snakefile."""
    from bioinformatics_mcp.hmmbuild.mcp.run_hmmbuild import run_hmmbuild

    temp_output = tmp_path / "output.hmm"

    # Generate the Snakefile with print_only=True to capture the content
    run_hmmbuild(
        sequence_alignment_file=str(test_paths["sequence_alignment_file"]),
        profile_hmm=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the Snakefile
    assert "rule hmmbuild:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify all required inputs and outputs are specified
    assert "sequence_alignment_file=" in content, (
        "Missing sequence_alignment_file input"
    )
    assert "profile_hmm=" in content, "Missing profile_hmm output"


def test_run_hmmbuild(test_paths, tmp_path):
    """Test that hmmbuild can be run with the test files."""
    from bioinformatics_mcp.hmmbuild.mcp.run_hmmbuild import run_hmmbuild

    temp_output = tmp_path / "output.hmm"

    # Run the tool with actual test files
    result = run_hmmbuild(
        sequence_alignment_file=str(test_paths["sequence_alignment_file"]),
        profile_hmm=str(temp_output),
    )

    # Verify that the run was successful
    assert result.returncode == 0, "hmmbuild process failed"
    assert temp_output.exists(), "Output HMM file was not created"

    # Optionally, compare the output file with an expected output, if available
    with (
        open(temp_output, "r") as generated,
        open(test_paths["expected_hmm_output"], "r") as expected,
    ):
        assert generated.read() == expected.read(), (
            "Generated HMM file content does not match expected output"
        )
