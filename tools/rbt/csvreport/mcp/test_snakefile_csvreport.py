import pytest
from pathlib import Path
import subprocess


@pytest.fixture
def test_paths():
    """Set up test paths for csvreport tests."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "csv_file": test_dir / "test_qc_report.csv",
        "expected_snakefile": test_dir / "expected_snakefile.txt",
        "output_folder": test_dir / "output"
    }


def test_snakefile_csvreport(test_paths, tmp_path, capsys):
    """Test that csvreport generates the expected Snakefile."""
    from tools.rbt.csvreport.run_csvreport import run_csvreport

    # Generate the Snakefile with print_only=True to capture printed output
    run_csvreport(
        csv_file=str(test_paths["csv_file"]),
        output_folder=str(tmp_path),
        print_only=True
    )

    # Capture and process the output
    captured = capsys.readouterr()
    snakefile_content = captured.out

    # Verify the essential Snakefile structure and components
    assert "rule csvreport:" in snakefile_content, "Missing 'csvreport' rule definition"
    assert "input:" in snakefile_content, "Missing 'input' section"
    assert "output:" in snakefile_content, "Missing 'output' section"
    assert "wrapper:" in snakefile_content, "Missing 'wrapper' definition"
    assert "csv_file=" in snakefile_content, "Missing 'csv_file' input parameter"
    assert "output_folder=" in snakefile_content, "Missing 'output_folder' output parameter"


def test_run_csvreport(test_paths, tmp_path):
    """Test that csvreport can be executed with test input files."""
    from tools.rbt.csvreport.run_csvreport import run_csvreport

    output_folder = tmp_path / "output"

    # Run the csvreport tool
    result = run_csvreport(
        csv_file=str(test_paths["csv_file"]),
        output_folder=str(output_folder)
    )

    # Verify that the process completed successfully
    assert result.returncode == 0, "csvreport execution failed"
    assert output_folder.is_dir(), "Output folder was not created"
    # Verify expected output files
    html_report = output_folder / "report.html"
    xlsx_file = output_folder / "report.xlsx"
    assert html_report.exists(), "HTML report was not generated"
    assert xlsx_file.exists(), "Excel report was not generated"