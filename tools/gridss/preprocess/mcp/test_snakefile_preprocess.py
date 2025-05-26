import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "input.bam",
        "reference_genome": test_dir / "ref_genome.fa",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_preprocess(test_paths, tmp_path, capsys):
    """Test that preprocess generates the expected Snakefile."""
    from tools.gridss.preprocess.run_preprocess import run_preprocess

    temp_output = tmp_path / "output_directory"

    # Generate the Snakefile with print_only=True to capture the content
    run_preprocess(
        input_bam=str(test_paths["input_bam"]),
        output_directory=str(temp_output),
        reference_genome=str(test_paths["reference_genome"]),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements and parameters are present
    assert "rule preprocess:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify required inputs in Snakefile
    assert "input_bam=" in content, "Missing input_bam parameter in Snakefile"
    assert "reference_genome=" in content, "Missing reference_genome parameter in Snakefile"

    # Verify required outputs in Snakefile
    assert "output_directory=" in content, "Missing output_directory parameter in Snakefile"

    # Verify reference to the wrapper
    assert "file:tools/gridss/preprocess" in content, "Wrapper path is missing or incorrect in Snakefile"


def test_run_preprocess(test_paths, tmp_path):
    """Test that preprocess can be run with the test files."""
    from tools.gridss.preprocess.run_preprocess import run_preprocess

    temp_output = tmp_path / "output_directory"

    # Run the preprocess tool
    result = run_preprocess(
        input_bam=str(test_paths["input_bam"]),
        output_directory=str(temp_output),
        reference_genome=str(test_paths["reference_genome"])
    )

    # Verify that the tool runs successfully
    assert result.returncode == 0, "preprocess run failed"
    assert temp_output.exists(), "Output directory was not created"