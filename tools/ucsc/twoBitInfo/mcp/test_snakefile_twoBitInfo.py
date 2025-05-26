import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_2bit": test_dir / "test_genome.2bit",
        "output_chrom_sizes": test_dir / "expected_output.chrom.sizes",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_twoBitInfo(test_paths, capsys):
    """Test that twoBitInfo generates the expected Snakefile."""
    from tools.ucsc.twoBitInfo.run_twoBitInfo import run_twoBitInfo

    # Generate the Snakefile with print_only=True to capture the content
    run_twoBitInfo(
        input_2bit=str(test_paths["input_2bit"]),
        output_chrom_sizes="dummy_output.chrom.sizes",
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule twoBitInfo:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify inputs and outputs match meta.yaml expectations
    assert "input_2bit=" in content, "Missing input_2bit parameter in Snakefile"
    assert "output_chrom_sizes=" in content, "Missing output_chrom_sizes parameter in Snakefile"


def test_run_twoBitInfo(test_paths, tmp_path):
    """Test that twoBitInfo can be run with the test files."""
    from tools.ucsc.twoBitInfo.run_twoBitInfo import run_twoBitInfo
    temp_output = tmp_path / "output.chrom.sizes"

    result = run_twoBitInfo(
        input_2bit=str(test_paths["input_2bit"]),
        output_chrom_sizes=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "twoBitInfo run failed"

    # Verify output file exists and matches expectations
    assert temp_output.exists(), "Output file was not created"
    with open(temp_output) as f:
        output_content = f.read()
    with open(test_paths["output_chrom_sizes"]) as f:
        expected_content = f.read()
    assert output_content == expected_content, "Output content does not match expected content"