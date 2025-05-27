import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "preprocessed_observations": test_dir / "preprocessed_observations.ext",
        "scenario": test_dir / "scenario.ext",
        "expected_snakefile": test_dir / "Snakefile",
        "variant_calls": test_dir / "variant_calls.ext"
    }

def test_snakefile_call_variants(test_paths, tmp_path, capsys):
    """Test that call-variants generates the expected Snakefile."""
    from bioinformatics_mcp.varlociraptor.call_variants.mcp.run_call_variants import run_call_variants
    temp_output = tmp_path / "variant_calls.ext"

    run_call_variants(
        preprocessed_observations=str(test_paths["preprocessed_observations"]),
        scenario=str(test_paths["scenario"]),
        variant_calls=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule call_variants:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "preprocessed_observations=" in content, "Missing preprocessed_observations parameter"
    assert "scenario=" in content, "Missing scenario parameter"
    assert "variant_calls=" in content, "Missing variant_calls output parameter"

def test_run_call_variants(test_paths, tmp_path):
    """Test that call-variants can be run with the test files."""
    from bioinformatics_mcp.varlociraptor.call_variants.mcp.run_call_variants import run_call_variants
    temp_output = tmp_path / "variant_calls.ext"

    result = run_call_variants(
        preprocessed_observations=str(test_paths["preprocessed_observations"]),
        scenario=str(test_paths["scenario"]),
        variant_calls=str(temp_output)
    )

    assert result.returncode == 0, "call-variants run failed"
    assert temp_output.exists(), "Variant calls output file was not created"