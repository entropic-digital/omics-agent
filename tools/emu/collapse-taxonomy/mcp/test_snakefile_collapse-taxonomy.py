import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_file": test_dir / "input.tsv",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "expected_output": test_dir / "expected_output.tsv",
    }


def test_snakefile_collapse_taxonomy(test_paths, tmp_path, capsys):
    """Test that collapse-taxonomy generates the expected Snakefile."""
    from tools.emu.collapse_taxonomy.run_collapse_taxonomy import run_collapse_taxonomy
    temp_output = tmp_path / "output.tsv"

    run_collapse_taxonomy(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        rank="genus",
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule collapse_taxonomy:" in content, "Missing 'collapse_taxonomy' rule definition"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "input_file=" in content, "Missing input_file in Snakefile"
    assert "output_file=" in content, "Missing output_file in Snakefile"
    assert "rank=" in content, "Missing rank param in Snakefile"


def test_run_collapse_taxonomy(test_paths, tmp_path):
    """Test that collapse-taxonomy can be executed correctly."""
    from tools.emu.collapse_taxonomy.run_collapse_taxonomy import run_collapse_taxonomy
    temp_output = tmp_path / "output.tsv"

    result = run_collapse_taxonomy(
        input_file=str(test_paths["input_file"]),
        output_file=str(temp_output),
        rank="genus"
    )

    assert result.returncode == 0, "collapse-taxonomy execution failed"

    output_content = temp_output.read_text()
    expected_content = test_paths["expected_output"].read_text()

    assert output_content == expected_content, "Output file does not match expected content"