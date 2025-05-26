import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test"
    return {
        "bam": test_dir / "test_input.bam",
        "txt": test_dir / "test_output.txt",
        "pdf": test_dir / "test_output.pdf",
        "expected_snakefile": test_dir / "Snakefile",
    }


def test_snakefile_collectinsertsizemetrics(test_paths, tmp_path, capsys):
    """Test that collectinsertsizemetrics generates the expected Snakefile."""
    from tools.picard.collectinsertsizemetrics.mcp.run_collectinsertsizemetrics import run_collectinsertsizemetrics

    # Generate the Snakefile with print_only=True to capture the content
    run_collectinsertsizemetrics(
        bam=str(test_paths["bam"]),
        txt=str(test_paths["txt"]),
        pdf=str(test_paths["pdf"]),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential Snakefile elements are present
    assert "rule collectinsertsizemetrics:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Verify inputs
    assert f"bam={str(test_paths['bam'])}" in content, "Missing BAM input definition"

    # Verify outputs
    assert f"txt={str(test_paths['txt'])}" in content, "Missing TXT output definition"
    assert f"pdf={str(test_paths['pdf'])}" in content, "Missing PDF output definition"


def test_run_collectinsertsizemetrics(test_paths, tmp_path):
    """Test that collectinsertsizemetrics can be run with the test files."""
    from tools.picard.collectinsertsizemetrics.mcp.run_collectinsertsizemetrics import run_collectinsertsizemetrics

    txt_output = tmp_path / "output.txt"
    pdf_output = tmp_path / "output.pdf"

    # Run the tool with the test BAM input
    result = run_collectinsertsizemetrics(
        bam=str(test_paths["bam"]),
        txt=str(txt_output),
        pdf=str(pdf_output),
    )

    # Verify that the process terminated successfully
    assert result.returncode == 0, "collectinsertsizemetrics run failed"

    # Verify that outputs are generated
    assert txt_output.exists(), "TXT output file was not generated"
    assert pdf_output.exists(), "PDF output file was not generated"