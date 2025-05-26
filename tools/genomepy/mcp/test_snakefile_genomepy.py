import pytest
from pathlib import Path
from tools.genomepy.mcp.run_genomepy import run_genomepy

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_files"
    return {
        "input_dir": test_dir,
        "expected_snakefile": test_dir / "expected_Snakefile",
        "test_assembly": "test_assembly",
    }

def test_snakefile_genomepy(test_paths, tmp_path, capsys):
    """Test that genomepy generates a valid Snakefile."""
    output_dir = tmp_path / test_paths["test_assembly"]

    # Generate the Snakefile with print_only=True to capture the content
    run_genomepy(
        provider="UCSC",
        output_assembly=str(output_dir),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in the generated Snakefile
    assert "rule genomepy:" in content, "Missing rule definition."
    assert "params:" in content, "Missing params section."
    assert "provider=" in content, "Missing provider parameter."
    assert "output:" in content, "Missing output section."
    assert f"{test_paths['test_assembly']}/{test_paths['test_assembly']}.fa" in content, "Missing assembly Fasta output."
    assert f"{test_paths['test_assembly']}/{test_paths['test_assembly']}.fa.fai" in content, "Missing FAI index output."
    assert f"{test_paths['test_assembly']}/{test_paths['test_assembly']}.gaps.bed" in content, "Missing gaps BED output."
    assert f"{test_paths['test_assembly']}/{test_paths['test_assembly']}.fa.sizes" in content, "Missing sizes output."
    assert "wrapper:" in content and "file:tools/genomepy" in content, "Missing wrapper specification."

def test_run_genomepy(test_paths, tmp_path):
    """Test that genomepy can be run with the specified assembly."""
    output_dir = tmp_path / test_paths["test_assembly"]

    # Run the tool with the test assembly
    result = run_genomepy(
        provider="UCSC",
        output_assembly=str(output_dir),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "genomepy run failed."

    # Verify that all expected output files are generated
    expected_outputs = [
        f"{output_dir}/{test_paths['test_assembly']}.fa",
        f"{output_dir}/{test_paths['test_assembly']}.fa.fai",
        f"{output_dir}/{test_paths['test_assembly']}.gaps.bed",
        f"{output_dir}/{test_paths['test_assembly']}.fa.sizes",
    ]
    for output_file in expected_outputs:
        assert Path(output_file).exists(), f"Expected output file missing: {output_file}"