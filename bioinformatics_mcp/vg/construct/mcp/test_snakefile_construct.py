import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "reference": test_dir / "reference.fa",
        "variant_calls": test_dir / "variants.vcf",
        "output_graph": test_dir / "output_graph.vg",
        "expected_snakefile": test_dir / "Snakefile"
    }


def test_snakefile_construct(test_paths, tmp_path, capsys):
    """Test that construct generates the expected Snakefile."""
    from bioinformatics_mcp.vg.construct.run_construct import run_construct
    temp_output = tmp_path / "output_graph.vg"

    # Generate the Snakefile with print_only=True
    run_construct(
        reference=str(test_paths["reference"]),
        variant_calls=str(test_paths["variant_calls"]),
        output_graph=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule elements in the Snakefile
    assert "rule construct:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"
    assert "reference=" in content, "Missing reference input parameter"
    assert "variant_calls=" in content, "Missing variant_calls input parameter"
    assert "output_graph=" in content, "Missing output_graph parameter"


def test_run_construct(test_paths, tmp_path):
    """Test that construct can be run with the test files."""
    from bioinformatics_mcp.vg.construct.run_construct import run_construct
    temp_output = tmp_path / "output_graph.vg"

    result = run_construct(
        reference=str(test_paths["reference"]),
        variant_calls=str(test_paths["variant_calls"]),
        output_graph=str(temp_output)
    )

    # Verify that the run is successful
    assert result.returncode == 0, "construct run failed"
    assert temp_output.exists(), "Output graph was not generated"