import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_file": test_dir / "test_input.bed",
        "ref_file": test_dir / "test_reference.genome",
        "expected_output": test_dir / "expected_output.genomecov"
    }


def test_snakefile_genomecov(test_paths, tmp_path, capsys):
    """Test that genomecov generates the expected Snakefile."""
    from bioinformatics_mcp.bedtools.genomecov.run_genomecov import run_genomecov
    temp_output = tmp_path / "output.genomecov"

    run_genomecov(
        input_file=str(test_paths["input_file"]),
        ref=str(test_paths["ref_file"]),
        output_file=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule genomecov:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "input_file=" in content, "Missing input_file parameter in Snakefile"
    assert "ref=" in content, "Missing ref parameter in Snakefile"
    assert "output_file=" in content, "Missing output_file parameter in Snakefile"


def test_run_genomecov(test_paths, tmp_path):
    """Test that genomecov can be run with the test files."""
    from bioinformatics_mcp.bedtools.genomecov.run_genomecov import run_genomecov
    temp_output = tmp_path / "output.genomecov"

    result = run_genomecov(
        input_file=str(test_paths["input_file"]),
        ref=str(test_paths["ref_file"]),
        output_file=str(temp_output)
    )

    assert result.returncode == 0, "genomecov run failed"
    assert temp_output.exists(), "Output file was not created by genomecov"
    assert temp_output.stat().st_size > 0, "Output file is empty after genomecov run"