import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths for snapshot tool."""
    base_dir = Path(__file__).parent
    test_dir = base_dir / "test_data"
    return {
        "pretext_contact_map": test_dir / "test_contact_map.pretext",
        "expected_full_image": test_dir / "expected_full_image.png",
        "expected_snakefile": test_dir / "expected_Snakefile.txt",
    }


def test_snakefile_snapshot(test_paths, tmp_path, capsys):
    """Test that snapshot generates the expected Snakefile."""
    from tools.pretext.snapshot.run_snapshot import run_snapshot

    temp_output = tmp_path / "output.png"

    run_snapshot(
        pretext_contact_map=str(test_paths["pretext_contact_map"]),
        full_image=str(temp_output),
        print_only=True,
    )

    captured = capsys.readouterr()
    content = captured.out

    assert "rule snapshot:" in content, "Missing rule definition in Snakefile"
    assert "input:" in content, "Missing input section in Snakefile"
    assert "output:" in content, "Missing output section in Snakefile"
    assert "params:" in content, "Missing params section in Snakefile"
    assert "wrapper:" in content, "Missing wrapper section in Snakefile"
    assert "pretext_contact_map=" in content, "Missing pretext_contact_map in input section"
    assert "full_image=" in content, "Missing full_image in params section"


def test_run_snapshot(test_paths, tmp_path):
    """Test that snapshot can run successfully with the test files."""
    from tools.pretext.snapshot.run_snapshot import run_snapshot

    temp_output = tmp_path / "full_image.png"

    result = run_snapshot(
        pretext_contact_map=str(test_paths["pretext_contact_map"]),
        full_image=str(temp_output),
    )

    assert result.returncode == 0, "Snapshot tool execution failed"
    assert temp_output.exists(), "Expected output file was not generated"