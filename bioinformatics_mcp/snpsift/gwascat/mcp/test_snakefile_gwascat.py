import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test file paths for gwascat."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test_files"
    return {
        "calls": test_dir / "test_calls.vcf",
        "gwas_catalog": test_dir / "test_gwas_catalog.tsv",
        "expected_annotated_calls": test_dir / "expected_annotated_calls.vcf",
    }


def test_snakefile_gwascat(test_paths, tmp_path, capsys):
    """Test that the gwascat Snakefile is generated as expected."""
    from bioinformatics_mcp.snpsift.gwascat.run_gwascat import run_gwascat

    temp_output = tmp_path / "temp_output.vcf"

    # Generate Snakefile with print_only=True to capture its content
    run_gwascat(
        calls=str(test_paths["calls"]),
        gwas_catalog=str(test_paths["gwas_catalog"]),
        annotated_calls=str(temp_output),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assert essential elements are present in the Snakefile
    assert "rule gwascat:" in content, "Missing rule definition in the Snakefile"
    assert "input:" in content, "Missing input section in the Snakefile"
    assert "output:" in content, "Missing output section in the Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in the Snakefile"

    # Ensure input parameters from meta.yaml are included
    assert "calls=" in content, "Missing 'calls' in the input parameters"
    assert "gwas_catalog=" in content, "Missing 'gwas_catalog' in the input parameters"

    # Ensure output parameters from meta.yaml are included
    assert "annotated_calls=" in content, (
        "Missing 'annotated_calls' in the output parameters"
    )


def test_run_gwascat(test_paths, tmp_path):
    """Test that the gwascat tool executes successfully with test files."""
    from bioinformatics_mcp.snpsift.gwascat.run_gwascat import run_gwascat

    temp_output = tmp_path / "annotated_calls.vcf"

    # Run the gwascat tool
    result = run_gwascat(
        calls=str(test_paths["calls"]),
        gwas_catalog=str(test_paths["gwas_catalog"]),
        annotated_calls=str(temp_output),
    )

    # Assert the tool executed successfully
    assert result.returncode == 0, "gwascat tool execution failed"

    # Assert the output file is generated
    assert temp_output.exists(), "Output annotated calls file was not created"
