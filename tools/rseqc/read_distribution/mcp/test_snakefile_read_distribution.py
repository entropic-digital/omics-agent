import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test" / "read_distribution"
    return {
        "aln": test_dir / "test.bam",
        "refgene": test_dir / "test.refgene.bed",
        "expected_output": test_dir / "expected_output.txt"
    }


def test_snakefile_read_distribution(test_paths, tmp_path, capsys):
    """Test that read_distribution generates the expected Snakefile."""
    from tools.rseqc.read_distribution.run_read_distribution import run_read_distribution
    temp_output = tmp_path / "output.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_read_distribution(
        aln=str(test_paths["aln"]),
        refgene=str(test_paths["refgene"]),
        output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential elements are present in the generated Snakefile
    assert "rule read_distribution:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "aln=" in content, "Missing 'aln' input parameter in Snakefile"
    assert "refgene=" in content, "Missing 'refgene' input parameter in Snakefile"
    assert "output=" in content, "Missing 'output' parameter in Snakefile"


def test_run_read_distribution(test_paths, tmp_path):
    """Test that read_distribution can be run with the test files."""
    from tools.rseqc.read_distribution.run_read_distribution import run_read_distribution
    temp_output = tmp_path / "output.txt"

    result = run_read_distribution(
        aln=str(test_paths["aln"]),
        refgene=str(test_paths["refgene"]),
        output=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "read_distribution run failed"
    assert temp_output.exists(), "Output file was not created during the run"
    assert temp_output.stat().st_size > 0, "Output file is empty"