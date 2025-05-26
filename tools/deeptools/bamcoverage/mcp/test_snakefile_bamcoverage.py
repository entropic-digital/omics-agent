import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths for the bamcoverage tool."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam": test_dir / "test.bam",
        "blacklist": test_dir / "blacklist.bed",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_bamcoverage(test_paths, tmp_path, capsys):
    """Test that the bamcoverage Snakefile is correctly generated."""
    from tools.deeptools.bamcoverage.run_bamcoverage import run_bamcoverage
    temp_output = tmp_path / "output.bigwig"

    # Generate Snakefile content
    run_bamcoverage(
        bam=str(test_paths["bam"]),
        blacklist=str(test_paths["blacklist"]),
        output=str(temp_output),
        genome="GRCh38",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assert that essential rule elements are present
    assert "rule bamcoverage:" in content, "Missing rule definition `bamcoverage`"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam=" in content, "Missing `bam` input parameter"
    assert "blacklist=" in content, "Missing `blacklist` input parameter"
    assert "output=" in content, "Missing output parameter"
    assert f"wrapper: 'file:tools/deeptools/bamcoverage'" in content, "Incorrect wrapper path"
    assert "genome" in content, "Missing `genome` parameter"
    assert "effective_genome_size" not in content, "`effective_genome_size` should not be included when genome is used"


def test_run_bamcoverage(test_paths, tmp_path):
    """Test the execution of bamcoverage using test files."""
    from tools.deeptools.bamcoverage.run_bamcoverage import run_bamcoverage
    temp_output = tmp_path / "output.bigwig"

    # Run the tool with the test setup
    result = run_bamcoverage(
        bam=str(test_paths["bam"]),
        blacklist=str(test_paths["blacklist"]),
        output=str(temp_output),
        genome="GRCh38",
    )

    # Assert successful execution
    assert result.returncode == 0, "bamcoverage tool execution failed"

    # Verify output file existence
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"