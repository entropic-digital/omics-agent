import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "input.bam",
        "filter_json": test_dir / "filter.json",
        "expected_output_bam": test_dir / "expected_output.bam",
    }


def test_snakefile_filter_json(test_paths, tmp_path, capsys):
    """Test that filter_json generates the expected Snakefile."""
    from tools.bamtools.filter_json.run_filter_json import run_filter_json
    temp_output_bam = tmp_path / "output.bam"

    # Generate the Snakefile with print_only=True to capture the content
    run_filter_json(
        bam_file=str(test_paths["input_bam"]),
        output_bam=str(temp_output_bam),
        json=str(test_paths["filter_json"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule and parameters are present
    assert "rule filter_json:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f"bam_file='{test_paths['input_bam']}'" in content, "Missing bam_file input"
    assert f"output_bam='{temp_output_bam}'" in content, "Missing output_bam"
    assert f"json='{test_paths['filter_json']}'" in content, "Missing json param"


def test_run_filter_json(test_paths, tmp_path):
    """Test that filter_json can process the input BAM file using the filter JSON."""
    from tools.bamtools.filter_json.run_filter_json import run_filter_json
    temp_output_bam = tmp_path / "output.bam"

    # Execute the tool
    result = run_filter_json(
        bam_file=str(test_paths["input_bam"]),
        output_bam=str(temp_output_bam),
        json=str(test_paths["filter_json"]),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "filter_json run failed"
    assert temp_output_bam.exists(), "Output BAM file was not created"

    # Add additional checks to verify the correctness of the output if needed
    # For example, you can compare the content of temp_output_bam with expected_output_bam
