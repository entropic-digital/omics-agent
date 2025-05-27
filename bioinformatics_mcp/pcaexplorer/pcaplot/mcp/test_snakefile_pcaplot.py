import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "input_path": test_dir / "input.rds",
        "expected_output": test_dir / "output.svg",
        "snakefile_output": test_dir / "Snakefile",
    }


def test_snakefile_pcaplot(test_paths, tmp_path, capsys):
    """Test that pcaplot generates the expected Snakefile."""
    from bioinformatics_mcp.pcaexplorer.pcaplot import run_pcaplot
    temp_output = tmp_path / "output.svg"

    run_pcaplot(
        input_path=str(test_paths["input_path"]),
        output_path=str(temp_output),
        print_only=True
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule pcaplot:" in content, "Missing pcaplot rule definition"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert f"input={repr(str(test_paths['input_path']))}" in content, "Missing or incorrect input in Snakefile"
    assert f"output={repr(str(temp_output))}" in content, "Missing or incorrect output in Snakefile"


def test_run_pcaplot(test_paths, tmp_path):
    """Test that pcaplot can be run with the test files."""
    from bioinformatics_mcp.pcaexplorer.pcaplot import run_pcaplot
    temp_output = tmp_path / "output.svg"

    result = run_pcaplot(
        input_path=str(test_paths["input_path"]),
        output_path=str(temp_output)
    )

    assert result.returncode == 0, "pcaplot execution failed"
    assert temp_output.exists(), "Expected output file was not created"