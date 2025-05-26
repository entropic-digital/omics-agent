import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_files"
    return {
        "aln": base_dir / "test_input.bam",
        "output": base_dir / "test_output.bam",
        "expected_snakefile": base_dir / "expected_Snakefile",
    }


def test_snakefile_alignmentsieve(test_paths, tmp_path, capsys):
    """Test that alignmentsieve generates the expected Snakefile."""
    from tools.deeptools.alignmentsieve.run_alignmentsieve import run_alignmentsieve

    temp_output = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_alignmentsieve(
        aln=str(test_paths["aln"]),
        output=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assertions for essential Snakefile elements based on meta.yaml
    assert "rule alignmentsieve:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f'aln="{test_paths["aln"]}"' in content, "Missing alignment input parameter"
    assert f'output="{temp_output}"' in content, "Missing output parameter"


def test_run_alignmentsieve(test_paths, tmp_path):
    """Test that alignmentsieve can be run with the test files."""
    from tools.deeptools.alignmentsieve.run_alignmentsieve import run_alignmentsieve

    temp_output = tmp_path / "output.bam"

    # Run the alignmentsieve tool
    result = run_alignmentsieve(
        aln=str(test_paths["aln"]),
        output=str(temp_output),
    )

    # Verify that the process completes successfully
    assert result.returncode == 0, "alignmentsieve run failed"

    # Verify that the output file is created
    assert temp_output.exists(), "Output file not created"

    # Optionally, validate the output content (e.g., file format, size, etc.)
    assert temp_output.stat().st_size > 0, "Output file is empty"