import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test_data"
    return {
        "input_file": test_dir / "test_input.bam",
        "reference": test_dir / "test_reference.fa",
        "expected_output": test_dir / "test_output.bam",
        "expected_index": test_dir / "test_output.bam.bai",
        "expected_metrics": test_dir / "metrics.txt",
    }


def test_snakefile_bamsormadup(test_paths, tmp_path, capsys):
    """Test that bamsormadup generates the expected Snakefile."""
    from bioinformatics_mcp.biobambam2.bamsormadup.mcp.run_bamsormadup import run_bamsormadup

    temp_output = tmp_path / "output.bam"
    temp_index = tmp_path / "output.bai"
    temp_metrics = tmp_path / "metrics.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_bamsormadup(
        input_file=str(test_paths["input_file"]),
        reference=str(test_paths["reference"]),
        output_file=str(temp_output),
        index=str(temp_index),
        metrics=str(temp_metrics),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in the Snakefile
    assert "rule bamsormadup:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper in Snakefile"
    assert "input_file=" in content, "Missing input_file parameter in Snakefile input"
    assert "reference=" in content, "Missing reference parameter in Snakefile input"
    assert "output_file=" in content, "Missing output_file parameter in Snakefile output"
    assert "index=" in content, "Missing index parameter in Snakefile output"
    assert "metrics=" in content, "Missing metrics parameter in Snakefile output"
    assert (
        "tools/biobambam2/bamsormadup" in content
    ), "Missing or incorrect wrapper path"


def test_run_bamsormadup(test_paths, tmp_path):
    """Test that bamsormadup can be run with the test files."""
    from bioinformatics_mcp.biobambam2.bamsormadup.mcp.run_bamsormadup import run_bamsormadup

    temp_output = tmp_path / "output.bam"
    temp_index = tmp_path / "output.bai"
    temp_metrics = tmp_path / "metrics.txt"

    # Execute the bamsormadup tool
    result = run_bamsormadup(
        input_file=str(test_paths["input_file"]),
        reference=str(test_paths["reference"]),
        output_file=str(temp_output),
        index=str(temp_index),
        metrics=str(temp_metrics),
    )

    # Verify successful execution
    assert result.returncode == 0, "bamsormadup tool execution failed"

    # Verify outputs are created
    assert temp_output.exists(), "Output BAM file not created"
    assert temp_index.exists(), "Output BAM index file not created"
    assert temp_metrics.exists(), "Metrics file not created"