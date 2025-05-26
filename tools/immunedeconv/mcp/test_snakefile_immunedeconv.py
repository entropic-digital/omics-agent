import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up paths for test inputs and outputs."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "expr": test_dir / "test_expression_matrix.csv",
        "signature": test_dir / "test_custom_signatures.tsv",
        "cibersort_bin": test_dir / "CIBERSORT.R",
        "cibersort_mat": test_dir / "CIBERSORT_signature_matrix.txt",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_immunedeconv(test_paths, tmp_path, capsys):
    """Test that the immunedeconv tool generates the expected Snakefile."""
    from tools.immunedeconv.mcp.run_immunedeconv import run_immunedeconv
    temp_output = tmp_path / "deconvolution_result.csv"

    # Generate the Snakefile with print_only=True
    run_immunedeconv(
        expr=str(test_paths["expr"]),
        signature=str(test_paths["signature"]),
        cibersort_bin=str(test_paths["cibersort_bin"]),
        cibersort_mat=str(test_paths["cibersort_mat"]),
        output=str(temp_output),
        method="CIBERSORT",
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential elements of the Snakefile
    assert "rule immunedeconv:" in content, "Missing 'rule' definition for immunedeconv"
    assert "input:" in content, "Missing 'input' section in rule"
    assert "output:" in content, "Missing 'output' section in rule"
    assert "params:" in content, "Missing 'params' section in rule"
    assert "wrapper:" in content, "Missing 'wrapper' directive"
    # Verify required inputs are present
    assert "expr=" in content, "Missing 'expr' input in rule"
    assert "signature=" in content, "Missing 'signature' input in rule"
    assert "cibersort_bin=" in content, "Missing 'cibersort_bin' input in rule"
    assert "cibersort_mat=" in content, "Missing 'cibersort_mat' input in rule"
    # Verify required output is present
    assert "output=" in content, "Missing 'output' parameter in rule"
    # Verify required params
    assert "method=" in content, "Missing 'method' parameter in rule"


def test_run_immunedeconv(test_paths, tmp_path):
    """Test the execution of the immunedeconv tool with test inputs."""
    from tools.immunedeconv.mcp.run_immunedeconv import run_immunedeconv
    temp_output = tmp_path / "deconvolution_result.csv"

    result = run_immunedeconv(
        expr=str(test_paths["expr"]),
        signature=str(test_paths["signature"]),
        cibersort_bin=str(test_paths["cibersort_bin"]),
        cibersort_mat=str(test_paths["cibersort_mat"]),
        output=str(temp_output),
        method="CIBERSORT",
    )

    # Assert the successful execution of the tool
    assert result.returncode == 0, "immunedeconv execution failed"
    assert temp_output.exists(), "Output file was not created"
    # Additional assertions can ensure correct output formatting or contents if needed