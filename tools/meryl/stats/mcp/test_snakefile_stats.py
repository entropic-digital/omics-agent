import pytest
from pathlib import Path
import subprocess


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "meryl_database": test_dir / "meryl_db_example"
    }


def test_snakefile_stats(test_paths, tmp_path, capsys):
    """Test that meryl stats generates the expected Snakefile."""
    from tools.meryl.stats.run_stats import run_stats
    temp_output = tmp_path / "output.stats"

    # Generate the Snakefile with print_only=True to capture the content
    run_stats(
        meryl_databases=str(test_paths["meryl_database"]),
        output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assertions for required Snakefile elements
    assert "rule stats:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper directive in Snakefile"
    assert "meryl_databases=" in content, "Missing meryl_databases input parameter"
    assert "command=" in content, "Missing command parameter"
    assert "output=" in content, "Missing output parameter in Snakefile"


def test_run_stats(test_paths, tmp_path):
    """Test that meryl stats runs successfully with test inputs."""
    from tools.meryl.stats.run_stats import run_stats
    temp_output = tmp_path / "output.stats"

    result = run_stats(
        meryl_databases=str(test_paths["meryl_database"]),
        output=str(temp_output),
        output_type="statistics"
    )

    # Assertions to verify successful execution
    assert result.returncode == 0, "meryl stats command failed to execute"
    assert temp_output.exists(), "Expected output file was not generated"
