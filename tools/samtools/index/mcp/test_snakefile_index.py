"""Module that tests if the samtools index Snakefile is rendered and runnable"""

import pytest
from pathlib import Path
from tools.samtools.index.run_index import run_index


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam_file": test_dir / "test.bam",
        "bam_file_index": test_dir / "test.bam.bai",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_index(test_paths, tmp_path, capsys):
    """Test that samtools index generates the expected Snakefile."""
    temp_output = tmp_path / "test.bam.bai"

    # Generate the Snakefile with print_only=True to capture content
    run_index(
        bam_file=str(test_paths["bam_file"]),
        bam_file_index=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the Snakefile
    assert "rule index:" in content, "Rule definition is missing"
    assert "input:" in content, "Input section is missing"
    assert "output:" in content, "Output section is missing"
    assert "wrapper:" in content, "Wrapper section is missing"

    # Verify the inputs and outputs from meta.yaml
    assert f"'{str(test_paths['bam_file'])}'" in content, "Input BAM file is missing"
    assert f"'{str(temp_output)}'" in content, "Output BAM index file is missing"


def test_run_index(test_paths, tmp_path):
    """Test running samtools index with test files."""
    temp_output = tmp_path / "test.bam.bai"

    # Run the samtools index tool
    result = run_index(
        bam_file=str(test_paths["bam_file"]),
        bam_file_index=str(temp_output),
    )

    # Verify the run is successful
    assert result.returncode == 0, "samtools index run failed"

    # Verify that output BAM index file was created
    assert temp_output.exists(), "Output BAM index file was not created"
