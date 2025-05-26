import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "fasta_assembly": test_dir / "test_assembly.fasta",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "candidate_coding_regions": test_dir / "candidate_coding_regions_output"
    }

def test_snakefile_predict(test_paths, tmp_path, capsys):
    """Test that predict generates the expected Snakefile."""
    from tools.transdecoder.predict.run_predict import run_predict
    temp_output = tmp_path / "output"

    # Generate the Snakefile with print_only=True to capture the content
    run_predict(
        fasta_assembly=str(test_paths["fasta_assembly"]),
        candidate_coding_regions=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule predict:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "fasta_assembly=" in content, "Missing fasta_assembly parameter"
    assert "candidate_coding_regions=" in content, "Missing candidate_coding_regions parameter"

def test_run_predict(test_paths, tmp_path):
    """Test that predict can be run with the test files."""
    from tools.transdecoder.predict.run_predict import run_predict
    temp_output = tmp_path / "output"

    result = run_predict(
        fasta_assembly=str(test_paths["fasta_assembly"]),
        candidate_coding_regions=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "Predict tool run failed"

    # Check if the expected output files are generated
    output_files = [
        temp_output / "output.pep",
        temp_output / "output.cds",
        temp_output / "output.gff3",
        temp_output / "output.bed"
    ]
    for file in output_files:
        assert file.exists(), f"Expected output file {file} not found"