import pytest
from pathlib import Path
from tools.assembly_stats.mcp.   _stats import    _stats

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test_data"
    return {
        "assembly": test_dir / "test_assembly.fasta",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "output": test_dir / "output_stats.txt"
    }

def test_snakefile_assembly_stats(test_paths, tmp_path, capsys):
    """Test that assembly-stats generates the expected Snakefile."""
    temp_output = tmp_path / "output_stats.txt"

    # Generate the Snakefile with print_only=True to capture the content
       _stats(
        assembly=str(test_paths["assembly"]),
        assembly_stats=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential parameters and sections are present in the Snakefile
    assert "rule assembly_stats:" in content, "Missing rule definition for assembly_stats"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper declaration in Snakefile"
    assert f"assembly='{test_paths['assembly']}'" in content, "Missing assembly input parameter"
    assert f"assembly_stats='{temp_output}'" in content, "Missing assembly_stats output parameter"

def test_   _stats(test_paths, tmp_path):
    """Test that assembly-stats can be run with the test files."""
    temp_output = tmp_path / "output_stats.txt"

    # Execute the assembly-stats tool
    result =    _stats(
        assembly=str(test_paths["assembly"]),
        assembly_stats=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "assembly-stats tool execution failed"

    # Verify the output file is created
    assert temp_output.exists(), "Output file was not created by assembly-stats"
    assert temp_output.stat().st_size > 0, "Output file is empty"