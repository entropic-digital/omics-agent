import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bed": test_dir / "input.bed",
        "accessible": test_dir / "accessible.bed",
        "expected_output": test_dir / "expected_output.bed",
        "expected_snakefile": test_dir / "Snakefile"
    }

def test_snakefile_antitarget(test_paths, tmp_path, capsys):
    """Test that the antitarget generates the expected Snakefile."""
    from tools.cnvkit.antitarget.run_antitarget import run_antitarget
    temp_output = tmp_path / "output.bed"

    run_antitarget(
        bed=str(test_paths["bed"]),
        accessible=str(test_paths["accessible"]),
        output_bed=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule antitarget:" in content, "Missing rule definition."
    assert "input:" in content, "Missing input section."
    assert "output:" in content, "Missing output section."
    assert "wrapper:" in content, "Missing wrapper section."
    assert 'bed="' in content, "Missing 'bed' input parameter."
    assert 'accessible="' in content, "Missing 'accessible' input parameter."
    assert 'output_bed="' in content, "Missing 'output_bed' output parameter."

def test_run_antitarget(test_paths, tmp_path):
    """Test that the antitarget tool executes successfully with test files."""
    from tools.cnvkit.antitarget.run_antitarget import run_antitarget
    temp_output = tmp_path / "output.bed"

    result = run_antitarget(
        bed=str(test_paths["bed"]),
        accessible=str(test_paths["accessible"]),
        output_bed=str(temp_output)
    )

    assert result.returncode == 0, "antitarget run failed."
    assert temp_output.exists(), "Output BED file not created."