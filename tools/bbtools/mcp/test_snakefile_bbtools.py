import pytest
from pathlib import Path
import subprocess


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent / "test_files"
    return {
        "input1": base_dir / "input1.fastq",
        "input2": base_dir / "input2.fastq",
        "expected_snakefile": base_dir / "expected_Snakefile",
        "output": base_dir / "output.fastq",
    }


def test_snakefile_bbtools(test_paths, tmp_path, capsys):
    """Test that bbtools generates the expected Snakefile."""
    from tools.bbtools.mcp.run_bbtools import run_bbtools

    temp_output = tmp_path / "output.fastq"

    # Generate the Snakefile with print_only=True to capture the content
    run_bbtools(
        command="bbmap.sh",
        input=[str(test_paths["input1"]), str(test_paths["input2"])],
        out=[str(temp_output)],
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule bbtools:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify all required input parameters
    assert f"in1='{test_paths['input1']}'" in content, "Missing in1 parameter"
    assert f"in2='{test_paths['input2']}'" in content, "Missing in2 parameter"

    # Verify all required output parameters
    assert f"out1='{temp_output}'" in content, "Missing output parameter"

    # Ensure no errors in the Snakefile
    assert len(content.strip()) > 0, "Generated Snakefile is empty"


def test_run_bbtools(test_paths, tmp_path):
    """Test that bbtools can be run with the test files."""
    from tools.bbtools.mcp.run_bbtools import run_bbtools

    temp_output = tmp_path / "output.fastq"

    # Run the bbtools wrapper
    result = run_bbtools(
        command="bbmap.sh",
        input=[str(test_paths["input1"]), str(test_paths["input2"])],
        out=[str(temp_output)]
    )

    # Verify that the process completed successfully
    assert result.returncode == 0, "bbtools run failed"
    assert temp_output.exists(), "Expected output file was not generated"

    # Additional checks for expected output content can be added here if needed