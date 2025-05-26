import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "bam_file": test_dir / "test.bam",
        "deduplicated_bam_file": test_dir / "deduplicated.bam",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_markdup(test_paths, tmp_path, capsys):
    """Test that markdup generates the expected Snakefile."""
    from tools.sambamba.markdup.run_markdup import run_markdup

    temp_output = tmp_path / "output.bam"

    run_markdup(
        bam_file=str(test_paths["bam_file"]),
        deduplicated_bam_file=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule markdup:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "bam_file=" in content, "Missing bam_file input parameter in Snakefile"
    assert "deduplicated_bam_file=" in content, "Missing deduplicated_bam_file output parameter in Snakefile"
    assert "tools/sambamba/markdup" in content, "Missing correct wrapper path in Snakefile"


def test_run_markdup(test_paths, tmp_path):
    """Test that the markdup tool can be executed with test files."""
    from tools.sambamba.markdup.run_markdup import run_markdup

    temp_output = tmp_path / "deduplicated.bam"

    result = run_markdup(
        bam_file=str(test_paths["bam_file"]),
        deduplicated_bam_file=str(temp_output)
    )

    assert result.returncode == 0, "markdup execution failed"
    assert temp_output.exists(), "Output deduplicated BAM file was not created"