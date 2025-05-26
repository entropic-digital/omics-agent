"""Module that tests if the cache Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_species": test_dir / "input_species.txt",
        "input_build": test_dir / "input_build.txt",
        "input_release": test_dir / "input_release.txt",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "output_directory": test_dir / "output",
    }


def test_snakefile_cache(test_paths, tmp_path, capsys):
    """Test that cache generates the expected Snakefile."""
    from tools.vep.mcp.run_cache import run_cache

    # Generate the Snakefile with print_only=True to capture the content
    run_cache(
        species="homo_sapiens",
        build="GRCh38",
        release="108",
        indexed=True,
        output_directory=str(test_paths["output_directory"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule cache:" in content, "Missing rule definition"
    assert "params:" in content, "Missing params section"
    assert "species=" in content, "Missing species parameter"
    assert "build=" in content, "Missing build parameter"
    assert "release=" in content, "Missing release parameter"
    assert "indexed=" in content, "Missing indexed parameter"
    assert "output:" in content, "Missing output section"
    assert "output_directory=" in content, "Missing output_directory parameter"
    assert "wrapper:" in content, "Missing wrapper section"


def test_run_cache(test_paths, tmp_path):
    """Test that cache can be run with the test files."""
    from tools.vep.mcp.run_cache import run_cache

    temp_output = tmp_path / "output_directory"
    temp_output.mkdir(parents=True, exist_ok=True)

    result = run_cache(
        species="homo_sapiens",
        build="GRCh38",
        release="108",
        indexed=False,
        output_directory=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, "cache run failed"
    # Check for output directory existence
    assert temp_output.exists(), "Output directory was not created"
    # Additional file-level checks can be added here
