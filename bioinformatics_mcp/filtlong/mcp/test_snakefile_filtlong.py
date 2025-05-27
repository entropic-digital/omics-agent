import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reads": test_dir / "test_reads.fastq",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "output": test_dir / "output.fastq",
    }


def test_snakefile_filtlong(test_paths, tmp_path, capsys):
    """Test that filtlong generates the expected Snakefile."""
    from bioinformatics_mcp.filtlong.mcp.run_filtlong import run_filtlong

    temp_output = tmp_path / "temp_output.fastq"

    # Generate the Snakefile with print_only=True to capture the content
    run_filtlong(
        reads=str(test_paths["reads"]),
        output=str(temp_output),
        length_weight=0.5,
        quality_weight=0.7,
        min_length=1000,
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements are present in the Snakefile
    assert "rule filtlong:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Add assertions for all required input parameters
    assert "reads=" in content, "Missing reads parameter"
    # Add assertions for all required output parameters
    assert "output=" in content, "Missing output parameter"
    # Add assertions for params
    assert "length_weight=0.5" in content, "Missing length_weight parameter"
    assert "quality_weight=0.7" in content, "Missing quality_weight parameter"
    assert "min_length=1000" in content, "Missing min_length parameter"


def test_run_filtlong(test_paths, tmp_path):
    """Test that filtlong can be run with the test files."""
    from bioinformatics_mcp.filtlong.mcp.run_filtlong import run_filtlong

    temp_output = tmp_path / "output.fastq"

    result = run_filtlong(
        reads=str(test_paths["reads"]),
        output=str(temp_output),
        length_weight=0.5,
        quality_weight=0.7,
        min_length=1000,
    )

    # Verify the process completed successfully
    assert result.returncode == 0, "filtlong execution failed"
    # Verify that the output file is generated
    assert temp_output.exists(), "Output file was not created"
