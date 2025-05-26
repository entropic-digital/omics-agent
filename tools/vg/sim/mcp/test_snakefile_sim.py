import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "xg_index": test_dir / "test.xg",
        "output_reads": test_dir / "output.gam",
        "gam_input": test_dir / "test.gam",
        "gbwt_index": test_dir / "test.gbwt",
    }


def test_snakefile_sim(test_paths, tmp_path, capsys):
    """Test that sim generates the expected Snakefile."""
    from tools.vg.sim.mcp.run_sim import run_sim
    temp_output = tmp_path / "output.gam"

    # Generate the Snakefile with print_only=True
    run_sim(
        xg_index=str(test_paths["xg_index"]),
        output_reads=str(temp_output),
        gam_input=str(test_paths["gam_input"]),
        gbwt_index=str(test_paths["gbwt_index"]),
        num_reads=10,
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential elements of the Snakefile
    assert "rule sim:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    
    # Verify the inputs are correctly defined
    assert f"xg_index='{test_paths['xg_index']}'" in content, "Missing xg_index input"
    assert f"gam_input='{test_paths['gam_input']}'" in content, "Missing gam_input input"
    assert f"gbwt_index='{test_paths['gbwt_index']}'" in content, "Missing gbwt_index input"
    
    # Verify the outputs are correctly defined
    assert f"output_reads='{temp_output}'" in content, "Missing output_reads output"
    
    # Verify params are correctly passed
    assert "num_reads=10" in content, "Missing num_reads parameter"


def test_run_sim(test_paths, tmp_path):
    """Test that sim can be run with the test files."""
    from tools.vg.sim.mcp.run_sim import run_sim
    temp_output = tmp_path / "output.gam"

    # Run the tool with test inputs
    result = run_sim(
        xg_index=str(test_paths["xg_index"]),
        output_reads=str(temp_output),
        gam_input=str(test_paths["gam_input"]),
        gbwt_index=str(test_paths["gbwt_index"]),
        num_reads=10,
    )

    # Verify that the run is successful
    assert result.returncode == 0, "sim run failed"
    
    # Verify that the output file is generated and has content
    assert temp_output.exists(), "Output file not created"
    assert temp_output.stat().st_size > 0, "Output file is empty"