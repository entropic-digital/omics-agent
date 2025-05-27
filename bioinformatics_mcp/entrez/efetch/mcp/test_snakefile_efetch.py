import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "db": test_dir / "db.txt",
        "id": test_dir / "id.txt",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_efetch(test_paths, tmp_path, capsys):
    """Test that the efetch tool generates the expected Snakefile."""
    from bioinformatics_mcp.entrez.efetch.run_efetch import run_efetch
    temp_output = tmp_path / "output.fasta"

    # Generate the Snakefile with print_only=True
    run_efetch(
        db=str(test_paths["db"]),
        id="NM_001200001",
        rettype="fasta",
        retmode="text",
        output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule efetch:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing 'input:' section in Snakefile"
    assert "output:" in content, "Missing 'output:' section in Snakefile"
    assert "params:" in content, "Missing 'params:' section in Snakefile"
    assert "wrapper:" in content, "Missing 'wrapper:' in Snakefile"
    
    # Verify inputs, outputs, and params are defined correctly
    assert f"'db': '{test_paths['db']}'" in content, "Missing or incorrect db input"
    assert "'id': 'NM_001200001'" in content, "Missing or incorrect id parameter"
    assert "'rettype': 'fasta'" in content, "Missing or incorrect rettype parameter"
    assert "'retmode': 'text'" in content, "Missing or incorrect retmode parameter"
    assert f"'{str(temp_output)}'" in content, "Missing or incorrect output definition"


def test_run_efetch(test_paths, tmp_path):
    """Test that the efetch tool executes properly."""
    from bioinformatics_mcp.entrez.efetch.run_efetch import run_efetch
    temp_output = tmp_path / "output.fasta"

    # Run the efetch tool
    result = run_efetch(
        db=str(test_paths["db"]),
        id="NM_001200001",
        rettype="fasta",
        retmode="text",
        output=str(temp_output)
    )

    # Verify the process completed successfully
    assert result.returncode == 0, "efetch execution failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"

    # Optionally, validate the output content (if example output is known)
    with open(temp_output, "r") as f:
        content = f.read()
        assert ">NM_001200001" in content, "Output file missing expected sequence header"