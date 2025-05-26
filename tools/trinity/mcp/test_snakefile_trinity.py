import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fastq1": test_dir / "reads_1.fastq",
        "fastq2": test_dir / "reads_2.fastq",
        "expected_fas": test_dir / "expected_output.fasta",
        "expected_map": test_dir / "expected_map.txt",
        "expected_dir": test_dir / "expected_intermediate_dir",
    }


def test_snakefile_trinity(test_paths, tmp_path, capsys):
    """Test that the trinity Snakefile is generated correctly."""
    from tools.trinity.run_trinity import run_trinity

    # Generate the Snakefile with print_only=True to capture its content
    run_trinity(
        fastq_files=[str(test_paths["fastq1"]), str(test_paths["fastq2"])],
        fas="output.fasta",
        map="output_map.txt",
        dir="output_dir",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify all essential rule elements
    assert "rule trinity:" in content, "Missing rule definition for trinity."
    assert "input:" in content, "Missing input section in Snakefile."
    assert "output:" in content, "Missing output section in Snakefile."
    assert "wrapper:" in content, "Missing wrapper section in Snakefile."

    # Verify input parameters in Snakefile
    assert "fastq_files" in content, "Missing fastq_files input definition in Snakefile."

    # Verify output parameters in Snakefile
    assert "fas=" in content, "Missing fas output parameter in Snakefile."
    assert "map=" in content, "Missing map output parameter in Snakefile."
    assert "dir=" in content, "Missing dir output parameter in Snakefile."


def test_run_trinity(test_paths, tmp_path):
    """Test that the trinity tool can be executed successfully."""
    from tools.trinity.run_trinity import run_trinity

    temp_output_fas = tmp_path / "output.fasta"
    temp_output_map = tmp_path / "output_map.txt"
    temp_output_dir = tmp_path / "output_dir"

    # Run the Trinity tool
    result = run_trinity(
        fastq_files=[str(test_paths["fastq1"]), str(test_paths["fastq2"])],
        fas=str(temp_output_fas),
        map=str(temp_output_map),
        dir=str(temp_output_dir),
    )

    # Verify the process completes successfully
    assert result.returncode == 0, "Trinity run failed."

    # Verify output files are created
    assert temp_output_fas.exists(), "Output fasta file was not created."
    assert temp_output_map.exists(), "Output map file was not created."
    assert temp_output_dir.exists(), "Output intermediate directory was not created."