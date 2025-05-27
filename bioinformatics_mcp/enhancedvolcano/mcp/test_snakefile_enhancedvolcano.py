import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_path": test_dir / "test_input.csv",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "output_path": test_dir / "test_output.svg"
    }

def test_snakefile_enhancedvolcano(test_paths, tmp_path, capsys):
    """Test that enhancedvolcano generates the expected Snakefile."""
    from bioinformatics_mcp.enhancedvolcano.mcp.run_enhancedvolcano import run_enhancedvolcano
    temp_output = tmp_path / "output.svg"

    run_enhancedvolcano(
        input_path=str(test_paths["input_path"]),
        output_path=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule enhancedvolcano:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper definition"
    assert f"'{test_paths['input_path']}'" in content, "Input path missing or incorrect"
    assert f"'{temp_output}'" in content, "Output path missing or incorrect"
    assert "height=" in content, "Missing height parameter"
    assert "width=" in content, "Missing width parameter"

def test_run_enhancedvolcano(test_paths, tmp_path):
    """Test that enhancedvolcano can be run with test files."""
    from bioinformatics_mcp.enhancedvolcano.mcp.run_enhancedvolcano import run_enhancedvolcano
    temp_output = tmp_path / "output.svg"

    result = run_enhancedvolcano(
        input_path=str(test_paths["input_path"]),
        output_path=str(temp_output)
    )

    assert result.returncode == 0, "enhancedvolcano run failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"