import pytest
from pathlib import Path

@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test" / "bismark2summary"
    return {
        "bam": test_dir / "test.bam",
        "expected_html": test_dir / "expected_report.html",
        "expected_txt": test_dir / "expected_report.txt",
    }

def test_snakefile_bismark2summary(test_paths, tmp_path, capsys):
    """Test that bismark2summary generates the expected Snakefile."""
    from tools.bismark.run_bismark2summary import run_bismark2summary
    temp_html = tmp_path / "bismark_summary_report.html"
    temp_txt = tmp_path / "bismark_summary_report.txt"

    # Generate the Snakefile with print_only=True to capture the content
    run_bismark2summary(
        bam=str(test_paths["bam"]),
        html=str(temp_html),
        txt=str(temp_txt),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential rule elements are present
    assert "rule bismark2summary:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"
    
    # Verify that required inputs are specified
    assert f"'{test_paths['bam']}'" in content, "Missing BAM input file"
    
    # Verify that required outputs are specified
    assert f"'{temp_html}'" in content, "Missing output HTML report"
    assert f"'{temp_txt}'" in content, "Missing output TXT report"

    # Verify optional params exist
    assert "extra" in content, "Missing optional 'extra' parameter"
    assert "title" in content, "Missing optional 'title' parameter"

def test_run_bismark2summary(test_paths, tmp_path):
    """Test that bismark2summary can be executed with test inputs."""
    from tools.bismark.run_bismark2summary import run_bismark2summary
    temp_html = tmp_path / "bismark_summary_report.html"
    temp_txt = tmp_path / "bismark_summary_report.txt"

    result = run_bismark2summary(
        bam=str(test_paths["bam"]),
        html=str(temp_html),
        txt=str(temp_txt),
    )

    # Verify that the tool runs successfully
    assert result.returncode == 0, "bismark2summary execution failed"
    
    # Verify the expected output files are generated
    assert temp_html.exists(), "HTML report was not generated"
    assert temp_txt.exists(), "TXT report was not generated"