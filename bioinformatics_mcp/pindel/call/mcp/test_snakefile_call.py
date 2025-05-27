import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reference": test_dir / "reference.fasta",
        "bam_files": [test_dir / "sample1.bam", test_dir / "sample2.bam"],
        "bam_config": test_dir / "bam_config.txt",
        "include_bed": test_dir / "include_regions.bed",
        "exclude_bed": test_dir / "exclude_regions.bed",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_call(test_paths, tmp_path, capsys):
    """Test that pindel call generates the expected Snakefile."""
    from bioinformatics_mcp.pindel.call.run_call import run_call

    # Test with print_only=True to generate Snakefile content
    run_call(
        reference=str(test_paths["reference"]),
        bam_files=[str(file) for file in test_paths["bam_files"]],
        bam_config=str(test_paths["bam_config"]),
        include_bed=str(test_paths["include_bed"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Assertions for the presence of required rule elements
    assert "rule call:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "reference=" in content, "Missing reference input"
    assert "bam_files=" in content, "Missing bam_files input"
    assert "bam_config=" in content, "Missing bam_config input"
    assert "include_bed=" in content, "Missing include_bed input"
    assert "output=" in content, "Missing output parameter"


def test_run_call(test_paths, tmp_path):
    """Test that pindel call can be executed with test files."""
    from bioinformatics_mcp.pindel.call.run_call import run_call

    temp_output = tmp_path / "output_dir"
    temp_output.mkdir()

    # Run the tool with test inputs
    result = run_call(
        reference=str(test_paths["reference"]),
        bam_files=[str(file) for file in test_paths["bam_files"]],
        bam_config=str(test_paths["bam_config"]),
        include_bed=str(test_paths["include_bed"]),
        **{"output_dir": str(temp_output)},
    )

    # Verify successful execution
    assert result.returncode == 0, "Pindel call run failed"
    assert (temp_output / "result_SV.txt").exists(), (
        "Expected output file not generated"
    )
