import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_tsv_files": [
            test_dir / "sample1_rel-abundance.tsv",
            test_dir / "sample2_rel-abundance.tsv"
        ],
        "expected_abundances": test_dir / "expected_abundances.tsv",
        "expected_taxonomy": test_dir / "expected_taxonomy.tsv",
        "snakefile": test_dir / "expected_Snakefile"
    }


def test_snakefile_combine_outputs(test_paths, tmp_path, capsys):
    """Test that combine-outputs generates the expected Snakefile."""
    from bioinformatics_mcp.emu.combine_outputs.run_combine_outputs import run_combine_outputs

    temp_abundances = tmp_path / "abundances.tsv"
    temp_taxonomy = tmp_path / "taxonomy.tsv"

    run_combine_outputs(
        input_tsv_files=[str(file) for file in test_paths["input_tsv_files"]],
        abundances=str(temp_abundances),
        taxonomy=str(temp_taxonomy),
        rank="genus",
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements are present
    assert "rule combine_outputs:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify required input parameters
    assert "tsv=" in content, "Missing TSV input parameter"
    # Verify required output parameters
    assert "abundances=" in content, "Missing abundances output parameter"
    assert "taxonomy=" in content, "Missing taxonomy output parameter"
    # Verify params related to rank
    assert "rank=" in content, "Missing rank param"

    # Check wrapper path
    assert "file:tools/emu/combine-outputs" in content, "Missing or incorrect wrapper path"


def test_run_combine_outputs(test_paths, tmp_path):
    """Test that combine-outputs can be run with the test files."""
    from bioinformatics_mcp.emu.combine_outputs.run_combine_outputs import run_combine_outputs

    temp_abundances = tmp_path / "abundances.tsv"
    temp_taxonomy = tmp_path / "taxonomy.tsv"

    result = run_combine_outputs(
        input_tsv_files=[str(file) for file in test_paths["input_tsv_files"]],
        abundances=str(temp_abundances),
        taxonomy=str(temp_taxonomy),
        rank="genus"
    )

    # Verify successful run
    assert result.returncode == 0, "combine-outputs run failed"

    # Validate output files exist
    assert temp_abundances.exists(), "Expected abundances output file not generated"
    assert temp_taxonomy.exists(), "Expected taxonomy output file not generated"

    # Optionally, compare output contents to expected files
    with open(temp_abundances) as generated, open(test_paths["expected_abundances"]) as expected:
        assert generated.read() == expected.read(), "Abundances output mismatch"

    with open(temp_taxonomy) as generated, open(test_paths["expected_taxonomy"]) as expected:
        assert generated.read() == expected.read(), "Taxonomy output mismatch"