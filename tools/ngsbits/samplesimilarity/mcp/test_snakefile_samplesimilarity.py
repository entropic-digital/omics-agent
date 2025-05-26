
"""Module that tests if the samplesimilarity Snakefile is rendered and runnable"""

import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "sample_vcf": test_dir / "sample1.vcf",
        "sample_vcf2": test_dir / "sample2.vcf",
        "reference_fai": test_dir / "reference.fai",
        "regions_bed": test_dir / "regions.bed",
        "output_file": test_dir / "output.tsv",
        "snakefile_dir": tmp_path := test_dir / "Snakefile_dir"
    }

def test_snakefile_samplesimilarity(test_paths, tmp_path, capsys):
    """Test that samplesimilarity generates the expected Snakefile."""
    from tools.samplesimilarity.mcp.run_samplesimilarity import run_samplesimilarity
    temp_output = tmp_path / "output.tsv"

    run_samplesimilarity(
         samples=[xθή