"""Module that tests if the plugins Snakefile is rendered and runnable"""

import pytest
from pathlib import Path
from subprocess import CompletedProcess


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test" / "tools" / "vep" / "plugins"
    return {
        "expected_input1": test_dir / "example_input1.ext",
        "expected_snakefile": test_dir / "expected_snakefile",
        "expected_output": test_dir / "expected_output.ext",
    }


def test_snakefile_plugins_verification(test_paths, tmp_path, capsys):
    """Test that the plugins Snakefile is generated correctly."""
    from bioinformatics_mcp.vep.plugins.run_plugins import run_vep_download_plugins

    temp_output = tmp_path / "output.ext"

    run_vep_download_plugins(
        name="vep_plugin_tool",
        description="Download VEP plugins.",
        authors="Johannes Köster",
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule all:" in content, "Missing rule all definition"
    assert "rule download_plugins" in content, "Missing rule for downloading plugins"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper declaration"
    assert "params:" in content, "Missing params section"
    assert 'name="vep_plugin_tool"' in content, "Missing 'name' parameter"
    assert 'description="Download VEP plugins."' in content, (
        "Missing 'description' parameter"
    )
    assert 'authors="Johannes Köster"' in content, "Missing 'authors' parameter"


def test_run_plugins_execution(test_paths, tmp_path):
    """Test the successful execution of download plugins."""
    from bioinformatics_mcp.vep.plugins.run_plugins import run_vep_download_plugins

    temp_output = tmp_path / "output.ext"

    result: CompletedProcess = run_vep_download_plugins(
        name="vep_plugin_tool",
        description="Download VEP plugins.",
        authors="Johannes Köster",
        output=str(temp_output),
    )

    # Verify that the run is successful
    assert result.returncode == 0, (
        f"Tool execution failed with return code {result.returncode}"
    )
    assert temp_output.exists(), "Expected output file was not created"
