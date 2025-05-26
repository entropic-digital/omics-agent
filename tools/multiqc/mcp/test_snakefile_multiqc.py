import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_dir": test_dir / "input_dir",
        "qc_report": test_dir / "qc_report.html",
        "multiqc_data": test_dir / "multiqc_data.zip",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_multiqc(test_paths, tmp_path, capsys):
    """Test that multiqc generates the expected Snakefile."""
    from tools.multiqc.mcp.run_multiqc import run_multiqc

    run_multiqc(
        input_dir=str(test_paths["input_dir"]),
        qc_report=str(test_paths["qc_report"]),
        multiqc_data=str(test_paths["multiqc_data"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule multiqc:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert f'input_dir="{test_paths["input_dir"]}"' in content, (
        "Missing input_dir parameter"
    )
    assert f'qc_report="{test_paths["qc_report"]}"' in content, (
        "Missing qc_report parameter"
    )
    assert f'multiqc_data="{test_paths["multiqc_data"]}"' in content, (
        "Missing multiqc_data parameter"
    )


def test_run_multiqc(test_paths, tmp_path):
    """Test that multiqc can be run with the test files."""
    from tools.multiqc.mcp.run_multiqc import run_multiqc

    temp_qc_report = tmp_path / "qc_report.html"
    temp_multiqc_data = tmp_path / "multiqc_data.zip"

    result = run_multiqc(
        input_dir=str(test_paths["input_dir"]),
        qc_report=str(temp_qc_report),
        multiqc_data=str(temp_multiqc_data),
    )

    assert result.returncode == 0, "multiqc run failed"
    assert temp_qc_report.exists(), "QC report was not generated"
    assert temp_multiqc_data.exists(), "MultiQC data folder/ZIP was not generated"
