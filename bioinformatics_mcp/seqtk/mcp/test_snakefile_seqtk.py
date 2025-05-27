import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fastx": test_dir / "test_input.fastq",
        "output": test_dir / "test_output.fastq",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_seqtk(test_paths, tmp_path, capsys):
    """Test that seqtk Snakefile is generated correctly."""
    from bioinformatics_mcp.seqtk.mcp.run_seqtk import run_seqtk

    temp_output = tmp_path / "temp_output.fastq"

    # Generate the Snakefile with print_only=True to capture the content
    run_seqtk(
        fastx=str(test_paths["fastx"]),
        output=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present in the Snakefile
    assert "rule seqtk:" in content, "Missing rule definition for seqtk"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify all input parameters from meta.yaml
    assert "fastx=" in content, "Missing fastx input parameter in Snakefile"

    # Verify all output parameters from meta.yaml
    assert "output=" in content, "Missing output parameter in Snakefile"


def test_run_seqtk(test_paths, tmp_path):
    """Test that seqtk completes execution successfully."""
    from bioinformatics_mcp.seqtk.mcp.run_seqtk import run_seqtk

    temp_output = tmp_path / "temp_output.fastq"

    # Run seqtk with test inputs
    result = run_seqtk(
        fastx=str(test_paths["fastx"]),
        output=str(temp_output),
    )

    # Verify the tool execution was successful
    assert result.returncode == 0, "seqtk execution failed"
    assert temp_output.exists(), "Output file was not created"
