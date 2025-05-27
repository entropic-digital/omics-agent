import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_fa": test_dir / "test_genome.fa",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "output_2bit": test_dir / "output.2bit"
    }


def test_snakefile_faToTwoBit(test_paths, tmp_path, capsys):
    """Test that faToTwoBit generates the expected Snakefile."""
    from bioinformatics_mcp.ucsc.faToTwoBit.run_faToTwoBit import run_faToTwoBit
    temp_output = tmp_path / "output.2bit"

    # Generate the Snakefile with print_only=True
    run_faToTwoBit(
        input_paths=[str(test_paths["input_fa"])],
        output_path=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements in the Snakefile
    assert "rule faToTwoBit:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert str(test_paths["input_fa"]) in content, "Missing input file in Snakefile"
    assert str(temp_output) in content, "Missing output file in Snakefile"
    assert "file:tools/ucsc/faToTwoBit" in content, "Missing wrapper path in Snakefile"


def test_run_faToTwoBit(test_paths, tmp_path):
    """Test that faToTwoBit can be run with the test files."""
    from bioinformatics_mcp.ucsc.faToTwoBit.run_faToTwoBit import run_faToTwoBit
    temp_output = tmp_path / "output.2bit"

    result = run_faToTwoBit(
        input_paths=[str(test_paths["input_fa"])],
        output_path=str(temp_output)
    )

    # Verify execution success
    assert result.returncode == 0, "faToTwoBit run failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"