import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_fastq1": test_dir / "test_fastq1.fq",
        "input_fastq2": test_dir / "test_fastq2.fq",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "configfile": test_dir / "config.yaml",
        "output_dir": test_dir / "output",
    }


def test_snakefile_optitype(test_paths, tmp_path, capsys):
    """Test that optitype generates the expected Snakefile."""
    from bioinformatics_mcp.optitype.mcp.run_optitype import run_optitype

    # Generate the Snakefile with print_only=True to capture the content
    run_optitype(
        fastq1=str(test_paths["input_fastq1"]),
        fastq2=str(test_paths["input_fastq2"]),
        configfile=str(test_paths["configfile"]),
        outdir=str(tmp_path),
        prefix="test_prefix",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile elements
    assert "rule optitype:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper definition in Snakefile"
    assert f'"{str(test_paths["input_fastq1"])}"' in content, (
        "Missing input_fastq1 in Snakefile inputs"
    )
    assert f'"{str(test_paths["input_fastq2"])}"' in content, (
        "Missing input_fastq2 in Snakefile inputs"
    )
    assert f'outdir="{str(tmp_path)}"' in content, (
        "Missing output directory in Snakefile outputs"
    )
    assert 'prefix="test_prefix"' in content, (
        "Missing prefix parameter in Snakefile outputs"
    )


def test_run_optitype(test_paths, tmp_path):
    """Test that optitype can be run with the test files."""
    from bioinformatics_mcp.optitype.mcp.run_optitype import run_optitype

    output_dir = tmp_path / "output"

    # Run the tool with test input files
    result = run_optitype(
        fastq1=str(test_paths["input_fastq1"]),
        fastq2=str(test_paths["input_fastq2"]),
        configfile=str(test_paths["configfile"]),
        outdir=str(output_dir),
        prefix="test_prefix",
    )

    # Verify that the tool execution is successful
    assert result.returncode == 0, "Optitype run failed"
    assert output_dir.exists(), "Output directory was not created"
    assert any(output_dir.iterdir()), "Output directory is empty, expected results"
