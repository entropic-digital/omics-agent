import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reference": test_dir / "reference.fa",
        "bam": test_dir / "sample.bam",
        "region": test_dir / "regions.bed",
        "normal": test_dir / "normal.bam",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_vardict(test_paths, tmp_path, capsys):
    """Test that vardict generates the expected Snakefile."""
    from bioinformatics_mcp.vardict.mcp.run_vardict import run_vardict
    temp_output = tmp_path / "output.vcf"

    # Generate the Snakefile with print_only=True to capture the content
    run_vardict(
        reference=str(test_paths["reference"]),
        bam=str(test_paths["bam"]),
        region=str(test_paths["region"]),
        normal=str(test_paths["normal"]),
        output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements exist in Snakefile
    assert "rule vardict:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "reference=" in content, "Missing reference parameter in Snakefile"
    assert "bam=" in content, "Missing bam parameter in Snakefile"
    assert "region=" in content, "Missing region parameter in Snakefile"
    assert "normal=" in content, "Missing normal parameter in Snakefile"
    assert "output=" in content, "Missing output parameter in Snakefile"


def test_run_vardict(test_paths, tmp_path):
    """Test that vardict can be run with the test files."""
    from bioinformatics_mcp.vardict.mcp.run_vardict import run_vardict
    temp_output = tmp_path / "output.vcf"

    result = run_vardict(
        reference=str(test_paths["reference"]),
        bam=str(test_paths["bam"]),
        region=str(test_paths["region"]),
        normal=str(test_paths["normal"]),
        output=str(temp_output)
    )

    # Verify tool runs successfully
    assert result.returncode == 0, "vardict run failed with non-zero return code"

    # Verify the output file is created
    assert temp_output.exists(), "Output VCF file not created by vardict"