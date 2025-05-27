import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_sam": test_dir / "example.sam",
        "output_fastq1": test_dir / "output_1.fastq",
        "output_fastq2": test_dir / "output_2.fastq",
    }


def test_snakefile_samtofastq(test_paths, tmp_path, capsys):
    """Test that samtofastq generates the expected Snakefile."""
    from bioinformatics_mcp.picard.samtofastq.run_samtofastq import run_samtofastq

    output_fastq1 = tmp_path / "test_output_1.fastq"

    # Generate the Snakefile with print_only=True to capture its content
    run_samtofastq(
        input_file=str(test_paths["input_sam"]),
        output_fastq1=str(output_fastq1),
        output_fastq2=str(test_paths["output_fastq2"]),
        print_only=True,
    )

    # Capture printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile rule elements
    assert "rule samtofastq:" in content, "Missing `samtofastq` rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper directive"
    assert "input_file=" in content, "Missing input_file parameter"
    assert "output_fastq1=" in content, "Missing output_fastq1 parameter"
    assert "output_fastq2=" in content, "Missing output_fastq2 parameter"
    assert "file:tools/picard/samtofastq" in content, "Missing wrapper path"


def test_run_samtofastq(test_paths, tmp_path):
    """Test that samtofastq can be executed with test inputs."""
    from bioinformatics_mcp.picard.samtofastq.run_samtofastq import run_samtofastq

    output_fastq1 = tmp_path / "test_output_1.fastq"
    output_fastq2 = tmp_path / "test_output_2.fastq"

    # Execute the samtofastq tool
    result = run_samtofastq(
        input_file=str(test_paths["input_sam"]),
        output_fastq1=str(output_fastq1),
        output_fastq2=str(output_fastq2),
    )

    # Assert successful execution
    assert result.returncode == 0, "samtofastq execution failed"
    assert output_fastq1.exists(), "Output FASTQ1 file was not created"
    assert output_fastq2.exists(), "Output FASTQ2 file was not created"