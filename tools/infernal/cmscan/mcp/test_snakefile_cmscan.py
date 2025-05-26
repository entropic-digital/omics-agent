import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "sequence_file": test_dir / "test_sequences.fasta",
        "covariance_models": test_dir / "test_covariance.cm",
        "expected_snakefile": test_dir / "Snakefile",
        "rna_alignments": test_dir / "test_rna_alignments.sto",
        "tblout": test_dir / "test_tblout.tbl",
    }


def test_snakefile_cmscan(test_paths, tmp_path, capsys):
    """Test that cmscan generates the expected Snakefile."""
    from tools.infernal.cmscan.run_cmscan import run_cmscan
    temp_output = tmp_path / "temp_output.sto"

    # Generate the Snakefile with print_only=True to capture the content
    run_cmscan(
        sequence_file=str(test_paths["sequence_file"]),
        covariance_models=str(test_paths["covariance_models"]),
        rna_alignments=str(temp_output),
        tblout=str(test_paths["tblout"]),
        main_output="/dev/null",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule cmscan:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Assert required inputs
    assert "sequence_file=" in content, "Missing sequence_file in input section"
    assert "covariance_models=" in content, "Missing covariance_models in input section"

    # Assert required outputs
    assert "rna_alignments=" in content, "Missing rna_alignments in output section"
    assert "tblout=" in content, "Missing tblout in output section"

    # Assert additional params
    assert "main_output=" in content, "Missing main_output in parameters"


def test_run_cmscan(test_paths, tmp_path):
    """Test that cmscan can be executed with test files."""
    from tools.infernal.cmscan.run_cmscan import run_cmscan
    temp_output = tmp_path / "temp_output.sto"
    temp_tblout = tmp_path / "temp_tblout.tbl"

    result = run_cmscan(
        sequence_file=str(test_paths["sequence_file"]),
        covariance_models=str(test_paths["covariance_models"]),
        rna_alignments=str(temp_output),
        tblout=str(temp_tblout),
        main_output="/dev/null",
    )

    # Verify that the run is successful
    assert result.returncode == 0, "cmscan execution failed"

    # Verify the expected output files are created
    assert temp_output.exists(), "RNA alignments output file was not created"
    assert temp_tblout.exists(), "Tabular output (tblout) file was not created"