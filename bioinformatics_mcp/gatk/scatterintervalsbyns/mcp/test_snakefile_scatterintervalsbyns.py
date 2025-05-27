import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reference_genome": test_dir / "test_reference.fasta",
        "expected_interval_list": test_dir / "expected_intervals.list",
    }


def test_snakefile_scatterintervalsbyns(test_paths, tmp_path, capsys):
    """Test that scatterintervalsbyns generates the expected Snakefile."""
    from bioinformatics_mcp.gatk.scatterintervalsbyns.run_scatterintervalsbyns import run_scatterintervalsbyns
    temp_output = tmp_path / "output_intervals.list"

    # Generate the Snakefile with print_only=True
    run_scatterintervalsbyns(
        reference_genome=str(test_paths["reference_genome"]),
        interval_list=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements in the Snakefile
    assert "rule scatterintervalsbyns:" in content, "Rule definition is missing from the Snakefile"
    assert "input:" in content, "Input section is missing from the rule"
    assert "output:" in content, "Output section is missing from the rule"
    assert "params:" in content, "Params section is missing from the rule"
    assert "wrapper:" in content, "Wrapper section is missing from the rule"

    # Verify inputs
    assert "reference_genome=" in content, "reference_genome input is missing from the rule"

    # Verify outputs
    assert "interval_list=" in content, "interval_list output is missing from the rule"

    # Verify wrapper path
    assert "wrapper=\"file:tools/gatk/scatterintervalsbyns\"" in content, "Wrapper path is incorrect or missing"


def test_run_scatterintervalsbyns(test_paths, tmp_path):
    """Test that scatterintervalsbyns runs successfully with test files."""
    from bioinformatics_mcp.gatk.scatterintervalsbyns.run_scatterintervalsbyns import run_scatterintervalsbyns
    temp_output = tmp_path / "output_intervals.list"

    result = run_scatterintervalsbyns(
        reference_genome=str(test_paths["reference_genome"]),
        interval_list=str(temp_output),
    )

    # Verify that the process completed successfully
    assert result.returncode == 0, f"scatterintervalsbyns failed with return code {result.returncode}"

    # Verify the output file is created
    assert temp_output.exists(), "Output interval list file was not generated"
    assert temp_output.stat().st_size > 0, "Output interval list file is empty"