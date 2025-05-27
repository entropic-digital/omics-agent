import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "gvcf_files": [test_dir / "sample1.g.vcf", test_dir / "sample2.g.vcf"],
        "combined_gvcf": test_dir / "combined_output.g.vcf",
    }


def test_snakefile_combinegvcfs(test_paths, tmp_path, capsys):
    """Test that combinegvcfs generates the expected Snakefile."""
    from bioinformatics_mcp.gatk.combinegvcfs.mcp.run_combinegvcfs import run_combinegvcfs

    run_combinegvcfs(
        gvcf_files=[str(f) for f in test_paths["gvcf_files"]],
        combined_gvcf=str(test_paths["combined_gvcf"]),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule combinegvcfs:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    for file in test_paths["gvcf_files"]:
        assert str(file) in content, f"Missing input GVCF file: {file}"
    assert str(test_paths["combined_gvcf"]) in content, "Missing combined GVCF output"


def test_run_combinegvcfs(test_paths, tmp_path):
    """Test that combinegvcfs can be run with the test files."""
    from bioinformatics_mcp.gatk.combinegvcfs.mcp.run_combinegvcfs import run_combinegvcfs

    temp_output = tmp_path / "combined_output.g.vcf"

    result = run_combinegvcfs(
        gvcf_files=[str(f) for f in test_paths["gvcf_files"]],
        combined_gvcf=str(temp_output),
    )

    assert result.returncode == 0, "combinegvcfs run failed"
    assert temp_output.exists(), "Output combined GVCF was not created"
