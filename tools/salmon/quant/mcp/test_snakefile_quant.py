import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "index": test_dir / "index.fa",
        "r1": test_dir / "reads_1.fastq",
        "r2": test_dir / "reads_2.fastq",
        "gtf": test_dir / "annotation.gtf",
        "output_quant": test_dir / "quant.sf",
        "output_bam": test_dir / "pseudo.bam",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_quant(test_paths, tmp_path, capsys):
    """Test that quant generates the expected Snakefile."""
    from tools.salmon.quant.run_quant import run_quant
    temp_output = tmp_path / "output"

    run_quant(
        index=str(test_paths["index"]),
        r1=str(test_paths["r1"]),
        r2=str(test_paths["r2"]),
        output=str(temp_output / "quant.sf"),
        bam=str(temp_output / "pseudo.bam"),
        libType="A",
        gtf=str(test_paths["gtf"]),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule quant:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "index=" in content, "Missing index input parameter"
    assert "r1=" in content, "Missing r1 input parameter"
    assert "r2=" in content, "Missing r2 input parameter"
    assert "bam=" in content, "Missing bam output parameter"
    assert "quant.sf" in content, "Missing quant output parameter"
    assert "libType=" in content, "Missing libType parameter"


def test_run_quant(test_paths, tmp_path):
    """Test that quant can be run with the test files."""
    from tools.salmon.quant.run_quant import run_quant
    temp_output = tmp_path / "output"
    temp_quant = temp_output / "quant.sf"
    temp_bam = temp_output / "pseudo.bam"

    result = run_quant(
        index=str(test_paths["index"]),
        r1=str(test_paths["r1"]),
        r2=str(test_paths["r2"]),
        output=str(temp_quant),
        bam=str(temp_bam),
        libType="A",
        gtf=str(test_paths["gtf"])
    )

    assert result.returncode == 0, "quant run failed"
    assert temp_quant.exists(), "Quantification output file not created"
    assert temp_bam.exists(), "Pseudo BAM output file not created"