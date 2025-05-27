import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bgzip_file": test_dir / "test_input.bgz",
        "tabix_index_file": test_dir / "test_input.bgz.tbi",
        "expected_output": test_dir / "expected_output.txt",
    }


def test_snakefile_query_tabix(test_paths, tmp_path, capsys):
    """Test that the tabix query Snakefile is generated correctly."""
    from run_query import run_query

    temp_output = tmp_path / "output.txt"

    # Generate the Snakefile with print_only=True
    run_query(
        bgzip_file=str(test_paths["bgzip_file"]),
        tabix_index_file=str(test_paths["tabix_index_file"]),
        region="chr1:1-1000",
        output=str(temp_output),
        print_only=True
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile components
    assert "rule tabix_query:" in content, "Missing rule definition for tabix_query"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    
    # Check for required inputs
    assert "bgzip_file=" in content, "Missing bgzip_file parameter in input section"
    assert "tabix_index_file=" in content, "Missing tabix_index_file parameter in input section"
    
    # Check for required outputs
    assert "output=" in content, "Missing output parameter"

    # Check for required params
    assert "region=" in content, "Missing region parameter"
    
    # Verify wrapper usage
    assert 'wrapper="file:bioinformatics_mcp/tabix/query"' in content, "Incorrect or missing wrapper definition"


def test_run_query_tabix(test_paths, tmp_path):
    """Test that the tabix query executes successfully."""
    from run_query import run_query

    temp_output = tmp_path / "output.txt"

    # Run the query
    result = run_query(
        bgzip_file=str(test_paths["bgzip_file"]),
        tabix_index_file=str(test_paths["tabix_index_file"]),
        region="chr1:1-1000",
        output=str(temp_output)
    )

    # Verify that the command executes without errors
    assert result.returncode == 0, "Tabix query execution failed"

    # Verify the output file is created
    assert temp_output.exists(), "Output file was not created"

    # Optionally, compare output content to expected
    with open(temp_output, "r") as output:
        actual_content = output.read()
    with open(test_paths["expected_output"], "r") as expected:
        expected_content = expected.read()
    assert actual_content == expected_content, "Output content does not match expected content"