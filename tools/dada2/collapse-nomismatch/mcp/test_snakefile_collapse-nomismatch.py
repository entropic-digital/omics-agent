import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_rds": test_dir / "input_chimera_free.rds",
        "expected_snakefile": test_dir / "Snakefile",
        "output_rds": test_dir / "output_collapsed.rds"
    }


def test_snakefile_collapse_nomismatch(test_paths, tmp_path, capsys):
    """Test that collapse-nomismatch generates the expected Snakefile."""
    from tools.dada2.collapse_nomismatch.run_collapse_nomismatch import run_collapse_nomismatch

    temp_output = tmp_path / "output.rds"

    # Generate the Snakefile with print_only=True to capture the content
    run_collapse_nomismatch(
        input_rds=str(test_paths["input_rds"]),
        output_rds=str(temp_output),
        optional_params={"key": "value"},
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential elements are present in the Snakefile
    assert "rule collapse_nomismatch:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "input_rds=" in content, "Missing input_rds parameter in Snakefile"
    assert "output_rds=" in content, "Missing output_rds parameter in Snakefile"


def test_run_collapse_nomismatch(test_paths, tmp_path):
    """Test that collapse-nomismatch can be executed with test inputs."""
    from tools.dada2.collapse_nomismatch.run_collapse_nomismatch import run_collapse_nomismatch

    temp_output = tmp_path / "output_collapsed.rds"

    # Run the tool with test inputs
    result = run_collapse_nomismatch(
        input_rds=str(test_paths["input_rds"]),
        output_rds=str(temp_output),
        optional_params={"key": "value"}
    )

    # Verify that the process completed successfully
    assert result.returncode == 0, "collapse-nomismatch run failed"
    assert temp_output.exists(), "Output file was not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"