import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "cns": test_dir / "test.cns",
        "expected_output": test_dir / "expected_output.bed",
    }

def test_snakefile_export(test_paths, tmp_path, capsys):
    """Test that export generates the expected Snakefile."""
    from tools.cnvkit.export.run_export import run_export
    temp_output = tmp_path / "output.bed"

    run_export(
        cns=str(test_paths["cns"]),
        output=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule export:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "cns=" in content, "Missing cns parameter in input section"
    assert "output=" in content, "Missing output parameter in output section"

def test_run_export(test_paths, tmp_path):
    """Test that export can be run with the test files."""
    from tools.cnvkit.export.run_export import run_export
    temp_output = tmp_path / "output.bed"

    result = run_export(
        cns=str(test_paths["cns"]),
        output=str(temp_output)
    )

    assert result.returncode == 0, "Export run failed with non-zero return code"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"