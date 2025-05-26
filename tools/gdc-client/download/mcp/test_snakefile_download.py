"""Module that tests if the download Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "manifest_file": test_dir / "test_manifest.txt",
        "token_file": test_dir / "test_token.txt",
        "expected_snakefile": test_dir / "Snakefile",
        "download_dir": test_dir / "download",
        "log_file": test_dir / "download.log",
    }


def test_snakefile_download(test_paths, tmp_path, capsys):
    """Test that download generates the expected Snakefile."""
    from run_download import run_download

    # Generate the Snakefile with print_only=True to capture the content
    run_download(
        manifest_file=str(test_paths["manifest_file"]),
        token_file=str(test_paths["token_file"]),
        download_dir=str(tmp_path / "download"),
        log_file=str(tmp_path / "log_file.log"),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify essential Snakefile elements
    assert "rule download:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "manifest_file=" in content, "Missing manifest_file input parameter"
    assert "token_file=" in content, "Missing token_file input parameter"
    assert "client_bin=" in content, "Missing client_bin param"
    assert "download_dir=" in content, "Missing download_dir param"
    assert "log_file=" in content, "Missing log_file param"


def test_run_download(test_paths, tmp_path):
    """Test that download can be run with the provided test files."""
    from run_download import run_download

    # Run the tool's download process
    result = run_download(
        manifest_file=str(test_paths["manifest_file"]),
        token_file=str(test_paths["token_file"]),
        download_dir=str(tmp_path / "download"),
        log_file=str(tmp_path / "log_file.log"),
    )

    # Verify the process runs successfully
    assert result.returncode == 0, "Download run failed with non-zero return code"

    # Verify output directory and log file are created
    download_dir = tmp_path / "download"
    log_file = tmp_path / "log_file.log"
    assert download_dir.exists() and download_dir.is_dir(), (
        "Download directory not created"
    )
    assert log_file.exists() and log_file.is_file(), "Log file not created"
