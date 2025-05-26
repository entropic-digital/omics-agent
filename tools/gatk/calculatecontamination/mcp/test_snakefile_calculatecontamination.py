import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "tumor": test_dir / "tumor.pileup",
        "normal": test_dir / "normal.pileup",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_calculatecontamination(test_paths, tmp_path, capsys):
    """Test that calculatecontamination generates the expected Snakefile."""
    from tools.gatk.calculatecontamination.run_calculatecontamination import (
        run_calculatecontamination,
    )

    temp_output = tmp_path / "contamination_table.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_calculatecontamination(
        tumor=str(test_paths["tumor"]),
        normal=str(test_paths["normal"]),
        output=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule calculatecontamination:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Add assertions for input parameters
    assert "tumor=" in content, "Missing tumor input parameter"
    assert "normal=" in content, "Missing normal input parameter"
    # Add assertions for output parameter
    assert "output=" in content, "Missing output parameter"
    assert "file:tools/gatk/calculatecontamination" in content, (
        "Incorrect or missing wrapper path"
    )


def test_run_calculatecontamination(test_paths, tmp_path):
    """Test that calculatecontamination can be run with the test files."""
    from tools.gatk.calculatecontamination.run_calculatecontamination import (
        run_calculatecontamination,
    )

    temp_output = tmp_path / "contamination_table.txt"

    result = run_calculatecontamination(
        tumor=str(test_paths["tumor"]),
        normal=str(test_paths["normal"]),
        output=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "calculatecontamination run failed"

    # Verify the output file is created
    assert temp_output.exists(), "Output contamination table was not created"
