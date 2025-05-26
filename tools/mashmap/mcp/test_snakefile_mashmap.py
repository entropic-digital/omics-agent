import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "ref": test_dir / "test_ref.fasta",
        "query": test_dir / "test_query.fasta",
        "expected_snakefile": test_dir / "expected_Snakefile",
    }


def test_snakefile_mashmap(test_paths, tmp_path, capsys):
    """Test that mashmap generates the expected Snakefile."""
    from tools.mashmap.mcp.run_mashmap import run_mashmap
    temp_output = tmp_path / "output.paf"

    run_mashmap(
        ref=str(test_paths["ref"]),
        query=str(test_paths["query"]),
        output=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule mashmap:" in content, "Snakefile is missing the 'mashmap' rule definition"
    assert "input:" in content, "Snakefile is missing the input block"
    assert "output:" in content, "Snakefile is missing the output block"
    assert "wrapper:" in content, "Snakefile is missing the wrapper section"
    assert f"ref='{test_paths['ref']}'" in content, "Snakefile is missing the ref file path input"
    assert f"query='{test_paths['query']}'" in content, "Snakefile is missing the query file path input"
    assert f"output='{temp_output}'" in content, "Snakefile is missing the output file path"
    assert "tools/mashmap" in content, "Wrapper path for mashmap tool is missing in Snakefile"


def test_run_mashmap(test_paths, tmp_path):
    """Test that mashmap can be run with the test files."""
    from tools.mashmap.mcp.run_mashmap import run_mashmap
    temp_output = tmp_path / "output.paf"

    result = run_mashmap(
        ref=str(test_paths["ref"]),
        query=str(test_paths["query"]),
        output=str(temp_output),
    )

    assert result.returncode == 0, "MashMap execution failed"
    assert temp_output.exists(), "MashMap output file was not created"
    assert temp_output.stat().st_size > 0, "MashMap output file is empty"