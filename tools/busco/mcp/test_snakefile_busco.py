import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "input_fasta": test_dir / "test_input.fasta",
        "out_dir": test_dir / "test_output",
        "expected_snakefile": test_dir / "expected_Snakefile"
    }

def test_snakefile_busco(test_paths, tmp_path, capsys):
    """Test that the busco Snakefile is generated correctly with print_only=True."""
    from tools.busco.mcp.run_busco import run_busco

    temp_output_dir = tmp_path / "busco_output"

    run_busco(
        input_fasta=str(test_paths["input_fasta"]),
        out_dir=str(temp_output_dir),
        mode="genome",
        lineage="test_lineage",
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule busco:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "input_fasta=" in content, "Missing 'input_fasta' parameter in input section"
    assert "lineage=" in content, "Missing 'lineage' parameter in params section"
    assert "mode=" in content, "Missing 'mode' parameter in params section"
    assert "out_dir=" in content, "Missing 'out_dir' parameter in output section"

def test_run_busco(test_paths, tmp_path):
    """Test that the busco tool runs successfully with provided inputs."""
    from tools.busco.mcp.run_busco import run_busco

    temp_output_dir = tmp_path / "busco_output"

    result = run_busco(
        input_fasta=str(test_paths["input_fasta"]),
        out_dir=str(temp_output_dir),
        mode="genome",
        lineage="test_lineage"
    )

    assert result.returncode == 0, "busco run failed with non-zero return code"
    assert temp_output_dir.exists(), "Output directory was not created"
    assert any(temp_output_dir.iterdir()), "Output directory is empty"