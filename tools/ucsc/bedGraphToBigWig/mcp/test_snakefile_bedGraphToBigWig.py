import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bedGraph": test_dir / "example.bedGraph",
        "chromsizes": test_dir / "example.chrom.sizes",
        "expected_bw": test_dir / "example.bw",
        "snakefile_output": test_dir / "generated_snakefile.smk"
    }


def test_snakefile_bedGraphToBigWig(test_paths, tmp_path, capsys):
    """Test that bedGraphToBigWig generates the expected Snakefile."""
    from tools.ucsc.bedGraphToBigWig.run_bedGraphToBigWig import run_bedGraphToBigWig
    temp_output = tmp_path / "output.bw"

    # Generate the Snakefile with print_only=True to capture the content
    run_bedGraphToBigWig(
        bedGraph=str(test_paths["bedGraph"]),
        chromsizes=str(test_paths["chromsizes"]),
        output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule bedGraphToBigWig:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "bedGraph=" in content, "Missing 'bedGraph' input parameter"
    assert "chromsizes=" in content, "Missing 'chromsizes' input parameter"
    assert "output=" in content, "Missing 'output' parameter"


def test_run_bedGraphToBigWig(test_paths, tmp_path):
    """Test that bedGraphToBigWig can be run with the test files."""
    from tools.ucsc.bedGraphToBigWig.run_bedGraphToBigWig import run_bedGraphToBigWig
    temp_output = tmp_path / "output.bw"

    # Run the tool with test files
    result = run_bedGraphToBigWig(
        bedGraph=str(test_paths["bedGraph"]),
        chromsizes=str(test_paths["chromsizes"]),
        output=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "bedGraphToBigWig run failed"
    assert temp_output.exists(), "Output file was not created successfully"

    # Optional: Verify the output file format if a validation method exists
    # For example, check if it conforms to BigWig format or contains expected data
