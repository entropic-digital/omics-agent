import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_model": test_dir / "input_model.model",
        "input_reference_genome": test_dir / "input_reference.fa",
        "output_reads": test_dir / "output_reads.fq",
        "output_unaligned_reads": test_dir / "output_unaligned_reads.fq",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_simulator(test_paths, tmp_path, capsys):
    """Test that the simulator generates the expected Snakefile."""
    from tools.nanosim.simulator.run_simulator import run_simulator

    temp_output_reads = tmp_path / "output_reads.fq"

    # Generate the Snakefile with print_only=True
    run_simulator(
        input_model=str(test_paths["input_model"]),
        output_reads=str(temp_output_reads),
        input_reference_genome=str(test_paths["input_reference_genome"]),
        output_unaligned_reads=str(test_paths["output_unaligned_reads"]),
        params_extra="--custom-param",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential params are present
    assert "rule simulator:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"

    # Verify all required inputs
    assert "model=" in content, "Missing model input parameter"
    assert "reference_genome=" in content, "Missing reference genome input parameter"

    # Verify all required outputs
    assert "reads=" in content, "Missing reads output parameter"
    assert "unaligned_reads=" in content, "Missing unaligned_reads output parameter"

    # Verify extra params
    assert "extra=" in content, "Missing extra parameter in Snakefile"

    # Check that the Snakefile wrapper path is correct
    assert "file:tools/nanosim/simulator" in content, (
        "Incorrect wrapper path in Snakefile"
    )


def test_run_simulator(test_paths, tmp_path):
    """Test that the simulator can be run with the test files."""
    from tools.nanosim.simulator.run_simulator import run_simulator

    temp_output_reads = tmp_path / "output_reads.fq"
    temp_output_unaligned_reads = tmp_path / "output_unaligned_reads.fq"

    # Run the simulator
    result = run_simulator(
        input_model=str(test_paths["input_model"]),
        output_reads=str(temp_output_reads),
        input_reference_genome=str(test_paths["input_reference_genome"]),
        output_unaligned_reads=str(temp_output_unaligned_reads),
        params_extra="--custom-param",
    )

    # Verify the run was successful
    assert result.returncode == 0, "Simulator run failed"

    # Check if the output files are generated
    assert temp_output_reads.exists(), "Output reads file was not created"
    assert temp_output_unaligned_reads.exists(), (
        "Output unaligned reads file was not created"
    )
