import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_reads": test_dir / "input_reads.fastq",
        "output_reads": test_dir / "output_reads.fastq",
        "expected_snakefile": test_dir / "expected_snakefile"
    }


def test_snakefile_se(test_paths, tmp_path, capsys):
    """Test that se generates the expected Snakefile."""
    from bioinformatics_mcp.sickle.se.run_se import run_se
    temp_output = tmp_path / "output.fastq"

    # Generate the Snakefile with print_only=True to capture the content
    run_se(
        input_reads=str(test_paths["input_reads"]),
        output_reads=str(temp_output),
        quality_threshold=20,
        length_threshold=50,
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements in the generated Snakefile
    assert "rule se:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Assert input and output parameters
    assert f"'{test_paths['input_reads']}'" in content, "Input file path is missing"
    assert f"'{temp_output}'" in content, "Output file path is missing"

    # Assert params values
    assert "quality_threshold=20" in content, "Quality threshold param is missing or incorrect"
    assert "length_threshold=50" in content, "Length threshold param is missing or incorrect"


def test_run_se(test_paths, tmp_path):
    """Test that se tool runs successfully with test input files."""
    from bioinformatics_mcp.sickle.se.run_se import run_se
    temp_output = tmp_path / "output_trimmed.fastq"

    result = run_se(
        input_reads=str(test_paths["input_reads"]),
        output_reads=str(temp_output),
        quality_threshold=20,
        length_threshold=50
    )

    # Verify the Snakemake run is successful
    assert result.returncode == 0, "se execution failed"
    assert temp_output.exists(), "Output file was not created"

    # Optionally, validate file integrity or size
    output_size = temp_output.stat().st_size
    assert output_size > 0, "Output file is empty"