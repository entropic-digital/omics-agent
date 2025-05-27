"""Module that tests if the blastn Snakefile is rendered and runnable"""

import pytest
from pathlib import Path
from bioinformatics_mcp.blastn.mcp.run_blastn import run_blastn


@pytest.fixture
def test_paths():
    """Set up test paths for inputs and outputs."""
    test_dir = Path(__file__).parent / "test_data"
    return {
        "query": test_dir / "test_query.fasta",
        "blastdb": test_dir / "test_db",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_blastn(test_paths, tmp_path, capsys):
    """Test that blastn Snakefile is generated correctly."""
    temp_output = tmp_path / "output.txt"

    # Generate Snakefile with print_only=True to capture its content
    run_blastn(
        query=str(test_paths["query"]),
        blastdb=str(test_paths["blastdb"]),
        output=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in the generated Snakefile
    assert "rule blastn:" in content, "Missing 'rule blastn' definition in Snakefile."
    assert "input:" in content, "Missing 'input' section in Snakefile."
    assert "output:" in content, "Missing 'output' section in Snakefile."
    assert "wrapper:" in content, "Missing 'wrapper' section in Snakefile."
    assert "query=" in content, "Missing 'query' input in Snakefile."
    assert "blastdb=" in content, "Missing 'blastdb' input in Snakefile."
    assert "output=" in content, "Missing 'output' parameter in Snakefile."


def test_run_blastn(test_paths, tmp_path):
    """Test that blastn executes successfully with test files."""
    temp_output = tmp_path / "output.txt"

    # Run the blastn tool
    result = run_blastn(
        query=str(test_paths["query"]),
        blastdb=str(test_paths["blastdb"]),
        output=str(temp_output),
    )

    # Verify that the process completed successfully
    assert result.returncode == 0, "blastn run failed — return code is not 0."
    assert temp_output.exists(), "Output file was not created by blastn."
