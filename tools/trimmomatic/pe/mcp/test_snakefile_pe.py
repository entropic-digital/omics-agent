import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input1": test_dir / "input1.fastq",
        "input2": test_dir / "input2.fastq",
        "output1": test_dir / "output1.fastq",
        "output2": test_dir / "output2.fastq",
        "output_unpaired1": test_dir / "output_unpaired1.fastq",
        "output_unpaired2": test_dir / "output_unpaired2.fastq",
        "expected_snakefile": test_dir / "expected_snakefile.txt",
    }


def test_snakefile_pe(test_paths, tmp_path, capsys):
    """Test Snakefile generation for paired-end reads trimming."""
    from tools.trimmomatic.pe.run_pe import run_pe

    temp_output1 = tmp_path / "output1.fastq"
    temp_output2 = tmp_path / "output2.fastq"
    temp_output_unpaired1 = tmp_path / "output_unpaired1.fastq"
    temp_output_unpaired2 = tmp_path / "output_unpaired2.fastq"

    run_pe(
        input1=str(test_paths["input1"]),
        input2=str(test_paths["input2"]),
        output1=str(temp_output1),
        output2=str(temp_output2),
        output_unpaired1=str(temp_output_unpaired1),
        output_unpaired2=str(temp_output_unpaired2),
        threads=4,
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule pe:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "input1=" in content, "Missing input1 parameter in Snakefile"
    assert "input2=" in content, "Missing input2 parameter in Snakefile"
    assert "output1=" in content, "Missing output1 parameter in Snakefile"
    assert "output2=" in content, "Missing output2 parameter in Snakefile"
    assert "output_unpaired1=" in content, (
        "Missing output_unpaired1 parameter in Snakefile"
    )
    assert "output_unpaired2=" in content, (
        "Missing output_unpaired2 parameter in Snakefile"
    )
    assert "threads=" in content, "Missing threads parameter in Snakefile"
    assert "phred=" in content, "Missing phred parameter in Snakefile"


def test_run_pe(test_paths, tmp_path):
    """Test tool execution for paired-end reads trimming."""
    from tools.trimmomatic.pe.run_pe import run_pe

    temp_output1 = tmp_path / "output1.fastq"
    temp_output2 = tmp_path / "output2.fastq"
    temp_output_unpaired1 = tmp_path / "output_unpaired1.fastq"
    temp_output_unpaired2 = tmp_path / "output_unpaired2.fastq"

    result = run_pe(
        input1=str(test_paths["input1"]),
        input2=str(test_paths["input2"]),
        output1=str(temp_output1),
        output2=str(temp_output2),
        output_unpaired1=str(temp_output_unpaired1),
        output_unpaired2=str(temp_output_unpaired2),
        threads=4,
    )

    assert result.returncode == 0, "Tool execution failed with non-zero exit code"

    assert temp_output1.exists(), "Output file for the first read pair was not created"
    assert temp_output2.exists(), "Output file for the second read pair was not created"
    assert temp_output_unpaired1.exists(), (
        "Unpaired output file for the first read was not created"
    )
    assert temp_output_unpaired2.exists(), (
        "Unpaired output file for the second read was not created"
    )
