import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_graphs": test_dir / "input_graphs.txt",
        "expected_snakefile": test_dir / "expected_snakefile.txt",
        "output_merged": test_dir / "output_merged.gfa",
    }


def test_snakefile_merge(test_paths, tmp_path, capsys):
    """Test that the merge tool generates the expected Snakefile."""
    from tools.vg.merge.run_merge import run_merge

    temp_output = tmp_path / "merged_output.gfa"

    run_merge(
        input_graphs=str(test_paths["input_graphs"]),
        output_merged=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    snakefile_content = captured.out

    # Verify essential rule elements from meta.yaml
    assert "rule merge:" in snakefile_content, "Missing rule definition in Snakefile"
    assert "input:" in snakefile_content, "Missing input section in Snakefile"
    assert "output:" in snakefile_content, "Missing output section in Snakefile"
    assert "wrapper:" in snakefile_content, "Missing wrapper definition in Snakefile"
    assert "input_graphs=" in snakefile_content, (
        "Missing input_graphs parameter in Snakefile"
    )
    assert "output_merged=" in snakefile_content, (
        "Missing output_merged parameter in Snakefile"
    )

    # Optionally check against an expected Snakefile for completeness
    if test_paths["expected_snakefile"].exists():
        with open(test_paths["expected_snakefile"], "r") as expected_file:
            expected_snakefile_content = expected_file.read()
        assert snakefile_content.strip() == expected_snakefile_content.strip(), (
            "Generated Snakefile does not match the expected content"
        )


def test_run_merge(test_paths, tmp_path):
    """Test that the merge tool runs successfully with provided inputs."""
    from tools.vg.merge.run_merge import run_merge

    temp_output = tmp_path / "merged_output.gfa"

    result = run_merge(
        input_graphs=str(test_paths["input_graphs"]), output_merged=str(temp_output)
    )

    # Verify that the run was successful
    assert result.returncode == 0, "Merge tool execution failed"
    assert temp_output.exists(), "Output file was not generated"
