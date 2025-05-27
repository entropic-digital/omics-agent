import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "bam_file": test_dir / "test.bam",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_verifybamid2(test_paths, tmp_path, capsys):
    """Test that verifybamid2 generates the expected Snakefile."""
    from bioinformatics_mcp.verifybamid2.run_verifybamid2 import run_verifybamid2

    temp_output = tmp_path / "output.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_verifybamid2(
        bam_file=str(test_paths["bam_file"]),
        extra=None,
        output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify that required elements are present in the Snakefile
    assert "rule verifybamid2:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "bam_file=" in content, "Missing bam_file input parameter"
    assert "output=" in content, "Missing output parameter"
    assert "file:tools/verifybamid/verifybamid2" in content, "Incorrect or missing wrapper path"

def test_run_verifybamid2(test_paths, tmp_path):
    """Test that verifybamid2 can be run with the test files."""
    from bioinformatics_mcp.verifybamid2.run_verifybamid2 import run_verifybamid2

    temp_output = tmp_path / "verifybamid2_output.txt"

    result = run_verifybamid2(
        bam_file=str(test_paths["bam_file"]),
        extra=None,
        output=str(temp_output)
    )

    # Verify that the process completes successfully
    assert result.returncode == 0, "verifybamid2 run failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"