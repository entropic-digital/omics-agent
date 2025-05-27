import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_bam": test_dir / "input.bam",
        "expected_output_bam": test_dir / "expected_output.bam",
        "expected_snakefile": test_dir / "expected_Snakefile",
        "umi_tag": "UB",
        "reject_bam": test_dir / "rejected.bam",
        "output_stats": test_dir / "output.stats",
    }


def test_snakefile_callmolecularconsensusreads(test_paths, tmp_path, capsys):
    """Test that callmolecularconsensusreads generates the expected Snakefile."""
    from bioinformatics_mcp.callmolecularconsensusreads.mcp.run_callmolecularconsensusreads import run_callmolecularconsensusreads

    temp_output_bam = tmp_path / "output.bam"

    # Generate Snakefile with print_only=True
    run_callmolecularconsensusreads(
        input_bam=str(test_paths["input_bam"]),
        output_bam=str(temp_output_bam),
        umi_tag=test_paths["umi_tag"],
        reject_bam=str(test_paths["reject_bam"]),
        output_stats=str(test_paths["output_stats"]),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential rule structure and parameters
    assert "rule callmolecularconsensusreads:" in content, "Rule 'callmolecularconsensusreads' is missing"
    assert "input:" in content, "Input section is missing"
    assert "output:" in content, "Output section is missing"
    assert "params:" in content, "Params section is missing"
    assert "wrapper:" in content, "Wrapper section is missing"
    assert f"'{str(test_paths['input_bam'])}'" in content, "Input BAM path is missing"
    assert f"output_bam='{str(temp_output_bam)}'" in content, "Output BAM path is missing"
    assert f"umi_tag='{test_paths['umi_tag']}'" in content, "UMI tag parameter is missing"
    assert f"reject_bam='{str(test_paths['reject_bam'])}'" in content, "Reject BAM path is missing"
    assert f"output_stats='{str(test_paths['output_stats'])}'" in content, "Output stats path is missing"


def test_run_callmolecularconsensusreads(test_paths, tmp_path):
    """Test that callmolecularconsensusreads executes correctly with test files."""
    from bioinformatics_mcp.callmolecularconsensusreads.mcp.run_callmolecularconsensusreads import run_callmolecularconsensusreads

    temp_output_bam = tmp_path / "output.bam"

    # Execute the tool with the test inputs
    result = run_callmolecularconsensusreads(
        input_bam=str(test_paths["input_bam"]),
        output_bam=str(temp_output_bam),
        umi_tag=test_paths["umi_tag"],
        reject_bam=str(test_paths["reject_bam"]),
        output_stats=str(test_paths["output_stats"]),
    )

    # Verify execution is successful
    assert result.returncode == 0, "Tool execution failed"
    assert temp_output_bam.exists(), "Output BAM file was not created"
    assert test_paths["reject_bam"].exists(), "Reject BAM file was not created"
    assert test_paths["output_stats"].exists(), "Output stats file was not created"