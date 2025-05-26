import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "read1": test_dir / "test_read1.fastq",
        "read2": test_dir / "test_read2.fastq",
        "reference": test_dir / "test_reference.fasta",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_mem_samblaster(test_paths, tmp_path, capsys):
    """Test that mem-samblaster generates the expected Snakefile."""
    from tools.bwa_mem2.mem_samblaster.mcp.run_mem_samblaster import run_mem_samblaster

    temp_output_bam = tmp_path / "test_output.bam"

    run_mem_samblaster(
        read1=str(test_paths["read1"]),
        read2=str(test_paths["read2"]),
        reference=str(test_paths["reference"]),
        output_bam=str(temp_output_bam),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule mem_samblaster:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    
    assert f'read1="{test_paths["read1"]}"' in content, "Missing read1 input in Snakefile"
    assert f'read2="{test_paths["read2"]}"' in content, "Missing read2 input in Snakefile"
    assert f'reference="{test_paths["reference"]}"' in content, "Missing reference input in Snakefile"
    assert f'output_bam="{temp_output_bam}"' in content, "Missing output_bam parameter in Snakefile"


def test_run_mem_samblaster(test_paths, tmp_path):
    """Test that mem-samblaster can be executed with test files."""
    from tools.bwa_mem2.mem_samblaster.mcp.run_mem_samblaster import run_mem_samblaster

    temp_output_bam = tmp_path / "test_output.bam"

    result = run_mem_samblaster(
        read1=str(test_paths["read1"]),
        read2=str(test_paths["read2"]),
        reference=str(test_paths["reference"]),
        output_bam=str(temp_output_bam),
    )

    assert result.returncode == 0, "mem-samblaster run failed with non-zero return code"
    assert temp_output_bam.exists(), "Output BAM file not generated after mem-samblaster run"