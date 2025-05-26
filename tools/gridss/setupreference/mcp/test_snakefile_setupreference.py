import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reference": test_dir / "test_reference.fa",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_setupreference(test_paths, tmp_path, capsys):
    """Test that setupreference generates the expected Snakefile."""
    from tools.gridss.setupreference.run_setupreference import run_setupreference

    # Generate the Snakefile with print_only=True to capture the content
    run_setupreference(
        reference=str(test_paths["reference"]),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule setupreference:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Add assertions for specific inputs/outputs as described in the meta.yaml
    assert f"input: reference='{test_paths['reference']}'" in content, "Missing reference input"
    assert "output:" in content, "Missing output specification"
    assert "params:" in content or "optional_param=" not in content or {}, "Missing optional params logic"


def test_run_setupreference(test_paths, tmp_path):
    """Test that setupreference can be run with the test reference file."""
    from tools.gridss.setupreference.run_setupreference import run_setupreference

    temp_output = tmp_path / "output.txt"

    # Execute the tool with test reference file
    result = run_setupreference(
        reference=str(test_paths["reference"]),
        optional_param="test_param",
        output=str(temp_output)
    )

    # Verify that the process ran successfully
    assert result.returncode == 0, "setupreference run failed"
    assert temp_output.exists(), "Expected output file was not generated"
    assert temp_output.stat().st_size > 0, "Output file is empty"