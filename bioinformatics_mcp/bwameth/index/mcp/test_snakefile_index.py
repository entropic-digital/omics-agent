import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reference_fasta": test_dir / "test_reference.fasta",
        "output_index_files": [
            test_dir / "test_reference.fasta.bwt",
            test_dir / "test_reference.fasta.pac",
            test_dir / "test_reference.fasta.ann",
            test_dir / "test_reference.fasta.amb",
            test_dir / "test_reference.fasta.sa",
        ],
    }


def test_snakefile_index(test_paths, tmp_path, capsys):
    """Test that bwa-meth index generates the expected Snakefile."""
    from bioinformatics_mcp.bwameth.index.run_index import run_index

    # Generate the Snakefile with print_only=True to capture the content
    run_index(
        reference_fasta=str(test_paths["reference_fasta"]),
        output_index_files=[str(file) for file in test_paths["output_index_files"]],
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential Snakefile elements
    assert "rule index:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "reference_fasta=" in content, "Missing reference_fasta input"
    assert "output_index_files=" in content, "Missing output_index_files output"
    assert "tools/bwameth/index" in content, "Missing wrapper path"


def test_run_index(test_paths, tmp_path):
    """Test that bwa-meth index can be run with the test files."""
    from bioinformatics_mcp.bwameth.index.run_index import run_index

    temp_output_files = [
        tmp_path / "output_file" / file.name for file in test_paths["output_index_files"]
    ]

    result = run_index(
        reference_fasta=str(test_paths["reference_fasta"]),
        output_index_files=[str(file) for file in temp_output_files],
    )

    # Verify that the run is successful
    assert result.returncode == 0, "bwa-meth index run failed"

    # Check that output files were created
    for output_file in temp_output_files:
        assert output_file.exists(), f"Output file {output_file} was not created"