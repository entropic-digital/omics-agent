"""Test file for the merge-pairs tool and its Snakefile"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "dadaF": test_dir / "dadaF.rds",
        "dadaR": test_dir / "dadaR.rds",
        "derepF": test_dir / "derepF.rds",
        "derepR": test_dir / "derepR.rds",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_merge_pairs(test_paths, tmp_path, capsys):
    """Test that merge-pairs generates the expected Snakefile."""
    from tools.dada2.merge_pairs.run_merge_pairs import run_merge_pairs

    temp_output = tmp_path / "merged_output.rds"

    # Generate the Snakefile with print_only=True to capture the content
    run_merge_pairs(
        dadaF=str(test_paths["dadaF"]),
        dadaR=str(test_paths["dadaR"]),
        derepF=str(test_paths["derepF"]),
        derepR=str(test_paths["derepR"]),
        output=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule merge_pairs:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "dadaF=" in content, "Missing dadaF parameter in Snakefile"
    assert "dadaR=" in content, "Missing dadaR parameter in Snakefile"
    assert "derepF=" in content, "Missing derepF parameter in Snakefile"
    assert "derepR=" in content, "Missing derepR parameter in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "output=" in content, "Missing output parameter in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"


def test_run_merge_pairs(test_paths, tmp_path):
    """Test that merge-pairs can be run with the test files."""
    from tools.dada2.merge_pairs.run_merge_pairs import run_merge_pairs

    temp_output = tmp_path / "merged_output.rds"

    # Run the tool with test files
    result = run_merge_pairs(
        dadaF=str(test_paths["dadaF"]),
        dadaR=str(test_paths["dadaR"]),
        derepF=str(test_paths["derepF"]),
        derepR=str(test_paths["derepR"]),
        output=str(temp_output),
    )

    # Verify that the tool execution is successful
    assert result.returncode == 0, "merge-pairs run failed"
    assert temp_output.exists(), "Output file was not created"
