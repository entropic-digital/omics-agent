import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_data"
    return {
        "segments": base_dir / "test_segments.cns",
        "vcf": base_dir / "test_variants.vcf",
        "output_segments": base_dir / "test_output.cns",
    }

def test_snakefile_call(test_paths, tmp_path, capsys):
    """Test that call generates the expected Snakefile."""
    from bioinformatics_mcp.cnvkit.call.run_call import run_call
    
    temp_output = tmp_path / "output.cns"
    
    # Generate the Snakefile with print_only=True to capture the content
    run_call(
        segments=str(test_paths["segments"]),
        vcf=str(test_paths["vcf"]),
        output_segments=str(temp_output),
        print_only=True
    )
    
    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential parameters are present
    assert "rule call:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "segments=" in content, "Missing segments input parameter"
    assert "vcf=" in content, "Missing vcf input parameter"
    assert "segments=" in content, "Missing segments output parameter"

def test_run_call(test_paths, tmp_path):
    """Test that call tool can be executed with the given test files."""
    from bioinformatics_mcp.cnvkit.call.run_call import run_call

    temp_output = tmp_path / "output.cns"
    
    result = run_call(
        segments=str(test_paths["segments"]),
        vcf=str(test_paths["vcf"]),
        output_segments=str(temp_output)
    )
    
    # Verify the tool execution is successful
    assert result.returncode == 0, "Tool execution failed"
    assert temp_output.exists(), "Output file was not created"