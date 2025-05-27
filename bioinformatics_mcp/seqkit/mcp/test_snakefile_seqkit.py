import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_files": test_dir / "input.fasta",
        "output_files": test_dir / "output.txt",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_seqkit(test_paths, tmp_path, capsys):
    """Test that seqkit generates the expected Snakefile."""
    from bioinformatics_mcp.seqkit.mcp.run_seqkit import run_seqkit
    temp_output = tmp_path / "output.txt"

    run_seqkit(
        input_files=str(test_paths["input_files"]),
        output_files=str(temp_output),
        command="fx2tab",
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule seqkit:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "input_files=" in content, "Missing `input_files` parameter in Snakefile"
    assert "output_files=" in content, "Missing `output_files` parameter in Snakefile"
    assert "command=" in content, "Missing `command` parameter in Snakefile"


def test_run_seqkit(test_paths, tmp_path):
    """Test that seqkit can be executed with the test files."""
    from bioinformatics_mcp.seqkit.mcp.run_seqkit import run_seqkit
    temp_output = tmp_path / "output.txt"

    result = run_seqkit(
        input_files=str(test_paths["input_files"]),
        output_files=str(temp_output),
        command="fx2tab"
    )

    assert result.returncode == 0, "seqkit run failed"
    assert temp_output.exists(), "Expected output file not created"