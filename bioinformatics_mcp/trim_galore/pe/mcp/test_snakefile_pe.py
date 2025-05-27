import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_fastq1": test_dir / "test_input1.fastq",
        "input_fastq2": test_dir / "test_input2.fastq",
        "output_trimmed1": test_dir / "test_output_trimmed1.fastq",
        "output_trimmed2": test_dir / "test_output_trimmed2.fastq",
        "output_report1": test_dir / "test_report1.txt",
        "output_report2": test_dir / "test_report2.txt",
    }


def test_snakefile_pe(test_paths, tmp_path, capsys):
    """Test that the Snakefile for trim_galore-pe is generated correctly."""
    from bioinformatics_mcp.trim_galore.mcp.run_pe import run_pe

    run_pe(
        input_fastq1=str(test_paths["input_fastq1"]),
        input_fastq2=str(test_paths["input_fastq2"]),
        output_trimmed1=str(test_paths["output_trimmed1"]),
        output_trimmed2=str(test_paths["output_trimmed2"]),
        output_report1=str(test_paths["output_report1"]),
        output_report2=str(test_paths["output_report2"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule trim_galore_pe:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "'fastq1':" in content, "Missing fastq1 input in Snakefile"
    assert "'fastq2':" in content, "Missing fastq2 input in Snakefile"
    assert "'trimmed1':" in content, "Missing trimmed1 output in Snakefile"
    assert "'trimmed2':" in content, "Missing trimmed2 output in Snakefile"
    assert "'report1':" in content, "Missing report1 output in Snakefile"
    assert "'report2':" in content, "Missing report2 output in Snakefile"


def test_run_pe(test_paths, tmp_path):
    """Test that trim_galore-pe runs successfully with test files."""
    from bioinformatics_mcp.trim_galore.mcp.run_pe import run_pe

    result = run_pe(
        input_fastq1=str(test_paths["input_fastq1"]),
        input_fastq2=str(test_paths["input_fastq2"]),
        output_trimmed1=str(test_paths["output_trimmed1"]),
        output_trimmed2=str(test_paths["output_trimmed2"]),
        output_report1=str(test_paths["output_report1"]),
        output_report2=str(test_paths["output_report2"]),
    )

    assert result.returncode == 0, "trim_galore-pe run failed"
    assert test_paths["output_trimmed1"].exists(), "Trimmed output1 file is missing"
    assert test_paths["output_trimmed2"].exists(), "Trimmed output2 file is missing"
    assert test_paths["output_report1"].exists(), "Report file1 is missing"
    assert test_paths["output_report2"].exists(), "Report file2 is missing"