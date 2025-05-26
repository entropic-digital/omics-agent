import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam": test_dir / "test.bam",
        "genome": test_dir / "test.fa",
        "annotation": test_dir / "test.gtf",
        "fusions": test_dir / "output_fusions.txt",
        "known_fusions": test_dir / "known_fusions.txt",
        "blacklist": test_dir / "blacklist.txt",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_arriba(test_paths, tmp_path, capsys):
    """Test that arriba generates the expected Snakefile."""
    from tools.arriba.mcp.run_arriba import run_arriba
    temp_output = tmp_path / "output_fusions.txt"

    run_arriba(
        bam=str(test_paths["bam"]),
        genome=str(test_paths["genome"]),
        annotation=str(test_paths["annotation"]),
        fusions=str(temp_output),
        known_fusions=str(test_paths["known_fusions"]),
        blacklist=str(test_paths["blacklist"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule arriba:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    assert "bam=" in content, "Missing bam parameter in Snakefile input"
    assert "genome=" in content, "Missing genome parameter in Snakefile input"
    assert "annotation=" in content, "Missing annotation parameter in Snakefile input"
    assert "fusions" in content, "Missing fusions parameter in Snakefile output"
    assert "known_fusions" in content, "Missing known_fusions parameter in Snakefile params"
    assert "blacklist" in content, "Missing blacklist parameter in Snakefile params"


def test_run_arriba(test_paths, tmp_path):
    """Test that arriba can be run with the test files."""
    from tools.arriba.mcp.run_arriba import run_arriba
    temp_output = tmp_path / "output_fusions.txt"

    result = run_arriba(
        bam=str(test_paths["bam"]),
        genome=str(test_paths["genome"]),
        annotation=str(test_paths["annotation"]),
        fusions=str(temp_output),
        known_fusions=str(test_paths["known_fusions"]),
        blacklist=str(test_paths["blacklist"])
    )

    assert result.returncode == 0, "Arriba run failed"
    assert temp_output.exists(), "Expected output file was not created"