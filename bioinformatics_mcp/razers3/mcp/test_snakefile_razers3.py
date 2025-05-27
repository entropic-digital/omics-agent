import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reads": test_dir / "reads.fastq",
        "reference": test_dir / "reference.fasta",
        "expected_output": test_dir / "expected_output.sam",
    }


def test_snakefile_razers3(test_paths, tmp_path, capsys):
    """Test that razers3 generates the expected Snakefile."""
    from bioinformatics_mcp.razers3.mcp.run_razers3 import run_razers3
    temp_output = tmp_path / "output.sam"

    # Generate the Snakefile with print_only=True to capture the content
    run_razers3(
        reads=str(test_paths["reads"]),
        reference=str(test_paths["reference"]),
        output=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile structure and parameters
    assert "rule razers3:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify input parameters
    assert "reads=" in content, "Missing 'reads' parameter in Snakefile"
    assert "reference=" in content, "Missing 'reference' parameter in Snakefile"

    # Verify output parameters
    assert "output=" in content, "Missing 'output' parameter in Snakefile"

    # Verify wrapper reference
    assert "tools/razers3" in content, "Wrapper path is missing or incorrect"


def test_run_razers3(test_paths, tmp_path):
    """Test that the razers3 tool can be run with test files."""
    from bioinformatics_mcp.razers3.mcp.run_razers3 import run_razers3
    temp_output = tmp_path / "output.sam"

    result = run_razers3(
        reads=str(test_paths["reads"]),
        reference=str(test_paths["reference"]),
        output=str(temp_output),
    )

    # Verify that the tool ran successfully
    assert result.returncode == 0, "razers3 execution failed"
    assert temp_output.exists(), "Expected output file was not created"

    # Optionally, compare output with expected results if applicable
    # This assumes expected_output exists and contains the expected result
    expected_output = test_paths["expected_output"]
    assert temp_output.read_text() == expected_output.read_text(), "Output does not match expected result"