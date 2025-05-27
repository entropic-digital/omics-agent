import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fasta_file": test_dir / "test.fasta",
        "expected_output_dir": test_dir / "expected_output",
    }


def test_snakefile_index_star_index(test_paths, tmp_path, capsys):
    """Test that STAR Index generates the expected Snakefile."""
    from bioinformatics_mcp.star.index.run_index import run_index

    # Temporary output directory
    temp_output_dir = tmp_path / "output_dir"
    temp_output_dir.mkdir()

    # Generate the Snakefile with print_only=True to capture the content
    run_index(
        fasta_file=str(test_paths["fasta_file"]),
        output_dir=str(temp_output_dir),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule parameters are present
    assert "rule index:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify specific elements for the STAR Index tool
    assert "fasta_file=" in content, "Missing fasta_file parameter in Snakefile"
    assert "output_dir=" in content, "Missing output_dir parameter in Snakefile"
    assert "tools/star/index" in content, "Missing STAR index wrapper path in Snakefile"


def test_run_index_star_index(test_paths, tmp_path):
    """Test that STAR Index can be run with the test files."""
    from bioinformatics_mcp.star.index.run_index import run_index

    # Temporary output directory
    temp_output_dir = tmp_path / "output_dir"
    temp_output_dir.mkdir()

    # Execute the run_index function
    result = run_index(
        fasta_file=str(test_paths["fasta_file"]),
        output_dir=str(temp_output_dir)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "STAR Index tool run failed"

    # Check if the output directory was created
    assert temp_output_dir.exists(), "Output directory not created by STAR Index tool"

    # Check if the output contains expected files
    output_files = list(temp_output_dir.iterdir())
    assert len(output_files) > 0, "No files generated in the output directory"
    assert any(f.suffix in [".sa", ".genome"] for f in output_files), "Expected STAR index output files are missing"