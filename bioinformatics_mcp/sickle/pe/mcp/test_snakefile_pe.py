import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_1": test_dir / "input_1.fastq",
        "input_2": test_dir / "input_2.fastq",
        "output_1": test_dir / "output_1.fastq",
        "output_2": test_dir / "output_2.fastq",
        "output_single": test_dir / "output_single.fastq",
        "qual_type": "illumina"
    }


def test_snakefile_pe(test_paths, tmp_path, capsys):
    """Test that pe generates the expected Snakefile."""
    from bioinformatics_mcp.sickle_pe.run_pe import run_pe

    # Invoke run_pe with print_only=True
    run_pe(
        input_1=test_paths["input_1"],
        input_2=test_paths["input_2"],
        output_1=str(tmp_path / "output_1.fastq"),
        output_2=str(tmp_path / "output_2.fastq"),
        output_single=str(tmp_path / "output_single.fastq"),
        qual_type=test_paths["qual_type"],
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Check for essential rule elements in the Snakefile
    assert "rule pe:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Validate input parameters
    assert "input_1=" in content, "Missing input_1 parameter"
    assert "input_2=" in content, "Missing input_2 parameter"

    # Validate output parameters
    assert "output_1=" in content, "Missing output_1 parameter"
    assert "output_2=" in content, "Missing output_2 parameter"
    assert "output_single=" in content, "Missing output_single parameter"

    # Validate params
    assert "qual_type=" in content, "Missing qual_type in params"


def test_run_pe(test_paths, tmp_path):
    """Test that pe can be run with the test files."""
    from bioinformatics_mcp.sickle_pe.run_pe import run_pe

    output_1 = tmp_path / "output_1.fastq"
    output_2 = tmp_path / "output_2.fastq"
    output_single = tmp_path / "output_single.fastq"

    # Run the tool with test inputs
    result = run_pe(
        input_1=str(test_paths["input_1"]),
        input_2=str(test_paths["input_2"]),
        output_1=str(output_1),
        output_2=str(output_2),
        output_single=str(output_single),
        qual_type=test_paths["qual_type"]
    )

    # Verify that the run was successful
    assert result.returncode == 0, "Tool execution failed"
    assert output_1.exists(), "Missing output_1.fastq after execution"
    assert output_2.exists(), "Missing output_2.fastq after execution"
    assert output_single.exists(), "Missing output_single.fastq after execution"