import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths for the tool."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "hdf5": test_dir / "test_input.hdf5",
        "pon": test_dir / "test_pon.tsv",
        "gc_interval": test_dir / "test_gc_interval.tsv",
        "std_copy_ratio": test_dir / "std_copy_ratio.tsv",
        "denoised_copy_ratio": test_dir / "denoised_copy_ratio.tsv",
    }


def test_snakefile_denoisereadcounts(test_paths, tmp_path, capsys):
    """Test that the denoisereadcounts generates the expected Snakefile."""
    from tools.gatk.denoisereadcounts.mcp.run_denoisereadcounts import run_denoisereadcounts

    temp_std_output = tmp_path / "temp_std_copy_ratio.tsv"
    temp_denoised_output = tmp_path / "temp_denoised_copy_ratio.tsv"

    # Generate the Snakefile with print_only=True to capture the content
    run_denoisereadcounts(
        hdf5=str(test_paths["hdf5"]),
        std_copy_ratio=str(temp_std_output),
        denoised_copy_ratio=str(temp_denoised_output),
        pon=str(test_paths["pon"]),
        gc_interval=str(test_paths["gc_interval"]),
        java_opts="-Xms4g -Xmx4g",
        extra="--extra-arg",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements
    assert "rule denoisereadcounts:" in content, "Snakefile is missing the rule definition."
    assert "input:" in content, "Snakefile is missing the input section."
    assert "output:" in content, "Snakefile is missing the output section."
    assert "params:" in content, "Snakefile is missing the params section."
    assert "wrapper:" in content, "Snakefile is missing the wrapper section."

    # Assert required inputs in the generated Snakefile
    assert "hdf5=" in content, "Missing 'hdf5' input parameter in Snakefile."
    assert "pon=" in content, "Missing 'pon' input parameter in Snakefile."
    assert "gc_interval=" in content, "Missing 'gc_interval' input parameter in Snakefile."

    # Assert required outputs in the generated Snakefile
    assert "std_copy_ratio=" in content, "Missing 'std_copy_ratio' output parameter in Snakefile."
    assert "denoised_copy_ratio=" in content, "Missing 'denoised_copy_ratio' output parameter in Snakefile."

    # Assert optional parameters in the generated Snakefile
    assert "java_opts" in content, "Missing 'java_opts' parameter in Snakefile."
    assert "extra" in content, "Missing 'extra' parameter in Snakefile."


def test_run_denoisereadcounts(test_paths, tmp_path):
    """Test that the denoisereadcounts tool runs with the provided test files."""
    from tools.gatk.denoisereadcounts.mcp.run_denoisereadcounts import run_denoisereadcounts

    temp_std_output = tmp_path / "temp_std_copy_ratio.tsv"
    temp_denoised_output = tmp_path / "temp_denoised_copy_ratio.tsv"

    # Run the tool with test inputs and capture results
    result = run_denoisereadcounts(
        hdf5=str(test_paths["hdf5"]),
        std_copy_ratio=str(temp_std_output),
        denoised_copy_ratio=str(temp_denoised_output),
        pon=str(test_paths["pon"]),
        gc_interval=str(test_paths["gc_interval"]),
        java_opts="-Xms4g -Xmx4g",
        extra="--extra-arg",
    )

    # Assert that the tool ran successfully
    assert result.returncode == 0, "denoisereadcounts execution failed."

    # Assert that the output files are created
    assert temp_std_output.exists(), "Standard copy ratio output file not created."
    assert temp_denoised_output.exists(), "Denoised copy ratio output file not created."
