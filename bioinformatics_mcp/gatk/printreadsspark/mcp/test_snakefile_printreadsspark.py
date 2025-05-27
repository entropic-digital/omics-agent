import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "bam_file": test_dir / "input.bam",
        "reference_file": test_dir / "reference.fasta",
        "reference_dict": test_dir / "reference.dict",
        "filtered_bam_file": test_dir / "output.filtered.bam",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_printreadsspark(test_paths, tmp_path, capsys):
    """Test that printreadsspark generates the expected Snakefile."""
    from bioinformatics_mcp.gatk.printreadsspark.run_printreadsspark import run_printreadsspark

    run_printreadsspark(
        bam_file=str(test_paths["bam_file"]),
        reference_file=str(test_paths["reference_file"]),
        reference_dict=str(test_paths["reference_dict"]),
        filtered_bam_file=str(test_paths["filtered_bam_file"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule printreadsspark:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    assert "bam_file=" in content, "Missing bam_file parameter"
    assert "reference_file=" in content, "Missing reference_file parameter"
    assert "reference_dict=" in content, "Missing reference_dict parameter"
    assert "filtered_bam_file=" in content, "Missing filtered_bam_file parameter"


def test_run_printreadsspark(test_paths, tmp_path):
    """Test that printreadsspark can be run with the test files."""
    from bioinformatics_mcp.gatk.printreadsspark.run_printreadsspark import run_printreadsspark

    temp_output = tmp_path / "output.filtered.bam"

    result = run_printreadsspark(
        bam_file=str(test_paths["bam_file"]),
        reference_file=str(test_paths["reference_file"]),
        reference_dict=str(test_paths["reference_dict"]),
        filtered_bam_file=str(temp_output)
    )

    assert result.returncode == 0, "printreadsspark run failed"
    assert temp_output.exists(), "Output filtered BAM file was not created"