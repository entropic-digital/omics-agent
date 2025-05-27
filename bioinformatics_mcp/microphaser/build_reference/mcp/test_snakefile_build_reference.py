import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "peptide_reference": test_dir / "peptide_reference.fasta",
        "output_fasta": test_dir / "output.fasta",
        "output_binary": test_dir / "output.binary",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_build_reference(test_paths, tmp_path, capsys):
    """Test that build_reference generates the expected Snakefile."""
    from bioinformatics_mcp.microphaser.build_reference.run_build_reference import run_build_reference

    temp_output_fasta = tmp_path / "output.fasta"
    temp_output_binary = tmp_path / "output.binary"

    # Generate the Snakefile with print_only=True to capture the content
    run_build_reference(
        peptide_reference=str(test_paths["peptide_reference"]),
        output_fasta=str(temp_output_fasta),
        output_binary=str(temp_output_binary),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential Snakefile elements
    assert "rule build_reference:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    # Add assertions for required input parameters
    assert "peptide_reference" in content, "Missing peptide_reference parameter in input"
    # Add assertions for required output parameters
    assert "output_fasta" in content, "Missing output_fasta parameter in output"
    assert "output_binary" in content, "Missing output_binary parameter in output"
    # Verify the wrapper path
    assert "tools/microphaser/build_reference" in content, "Incorrect or missing wrapper path"


def test_run_build_reference(test_paths, tmp_path):
    """Test that build_reference can be run with the test files."""
    from bioinformatics_mcp.microphaser.build_reference.run_build_reference import run_build_reference

    temp_output_fasta = tmp_path / "output.fasta"
    temp_output_binary = tmp_path / "output.binary"

    # Run the build_reference tool
    result = run_build_reference(
        peptide_reference=str(test_paths["peptide_reference"]),
        output_fasta=str(temp_output_fasta),
        output_binary=str(temp_output_binary)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "build_reference run failed"

    # Verify outputs are created
    assert temp_output_fasta.exists(), "Output FASTA file not created"
    assert temp_output_binary.exists(), "Output binary file not created"