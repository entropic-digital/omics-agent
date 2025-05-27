import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_files"
    return {
        "cns_file": base_dir / "test.cns",
        "cnr_file": base_dir / "test.cnr",
        "expected_pdf": base_dir / "output.pdf",
    }

def test_snakefile_diagram(test_paths, tmp_path, capsys):
    """Test that the diagram tool generates the correct Snakefile."""
    from run_diagram import run_diagram
    temp_output = tmp_path / "output.pdf"

    # Generate the Snakefile using print_only=True
    run_diagram(
        cns_file=str(test_paths["cns_file"]),
        cnr_or_cnn_file=str(test_paths["cnr_file"]),
        output_pdf=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present in the Snakefile
    assert "rule diagram:" in content, "Missing 'rule diagram' definition in Snakefile"
    assert "input:" in content, "Missing 'input' section in Snakefile"
    assert "output:" in content, "Missing 'output' section in Snakefile"
    assert "wrapper:" in content, "Missing 'wrapper' section in Snakefile"
    assert "cns_file=" in content, "Missing 'cns_file' parameter in Snakefile input"
    assert "cnr_or_cnn_file=" in content, "Missing 'cnr_or_cnn_file' parameter in Snakefile input"
    assert f"output_pdf='{temp_output}'" in content, "Missing or incorrect 'output_pdf' parameter in Snakefile output"

def test_run_diagram(test_paths, tmp_path):
    """Test that the diagram tool runs successfully with test files."""
    from run_diagram import run_diagram
    temp_output = tmp_path / "output.pdf"

    # Run the diagram tool with test inputs
    result = run_diagram(
        cns_file=str(test_paths["cns_file"]),
        cnr_or_cnn_file=str(test_paths["cnr_file"]),
        output_pdf=str(temp_output),
    )

    # Verify the tool executes successfully
    assert result.returncode == 0, "Diagram tool failed to run"
    assert temp_output.exists(), "Output PDF file was not created"