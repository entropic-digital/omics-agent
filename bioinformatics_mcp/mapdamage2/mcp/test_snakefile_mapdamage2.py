"""Module that tests if the mapdamage2 Snakefile is rendered and runnable"""

import pytest
from pathlib import Path


@pytest.fixture
def test_paths():
    """Set up test paths."""
    base_dir = Path(__file__).parent.parent
    test_dir = base_dir / "test_data"
    return {
        "reference_genome": test_dir / "test_reference.fasta",
        "alignment_file": test_dir / "test_alignment.bam",
        "runtime_log": test_dir / "test_runtime_log.txt",
        "fragmisincorporation_plot": test_dir / "Fragmisincorporation_plot.pdf",
        "length_plot": test_dir / "Length_plot.pdf",
        "misincorporation_txt": test_dir / "misincorporation.txt",
        "five_prime_ctot_freq": test_dir / "5pCtoT_freq.txt",
        "three_prime_gtoa_freq": test_dir / "3pGtoA_freq.txt",
        "dnacomp_txt": test_dir / "dnacomp.txt",
        "lgdistribution_txt": test_dir / "lgdistribution.txt",
        "stats_out_mcmc_hist": test_dir / "Stats_out_MCMC_hist.pdf",
        "stats_out_mcmc_iter": test_dir / "Stats_out_MCMC_iter.csv",
        "stats_out_mcmc_trace": test_dir / "Stats_out_MCMC_trace.pdf",
        "stats_out_mcmc_iter_summ_stat": test_dir / "Stats_out_MCMC_iter_summ_stat.csv",
        "stats_out_post_pred": test_dir / "Stats_out_post_pred.pdf",
        "stats_out_mcmc_correct_prob": test_dir / "Stats_out_MCMC_correct_prob.csv",
        "dnacomp_genome": test_dir / "dnacomp_genome.txt",
        "rescaled_bam": test_dir / "rescaled_test.bam",
        "output_dir": test_dir / "output",
    }


def test_snakefile_mapdamage2(test_paths, tmp_path, capsys):
    """Test that mapdamage2 generates the expected Snakefile."""
    from bioinformatics_mcp.mapdamage2.mcp.run_mapdamage2 import run_mapdamage2

    # Generate the Snakefile with print_only=True to capture the content
    run_mapdamage2(
        reference_genome=str(test_paths["reference_genome"]),
        alignment_file=str(test_paths["alignment_file"]),
        runtime_log=str(tmp_path / "runtime_log.txt"),
        fragmisincorporation_plot=str(tmp_path / "Fragmisincorporation_plot.pdf"),
        length_plot=str(tmp_path / "Length_plot.pdf"),
        misincorporation_txt=str(tmp_path / "misincorporation.txt"),
        five_prime_ctot_freq=str(tmp_path / "5pCtoT_freq.txt"),
        three_prime_gtoa_freq=str(tmp_path / "3pGtoA_freq.txt"),
        dnacomp_txt=str(tmp_path / "dnacomp.txt"),
        lgdistribution_txt=str(tmp_path / "lgdistribution.txt"),
        stats_out_mcmc_hist=str(tmp_path / "Stats_out_MCMC_hist.pdf"),
        stats_out_mcmc_iter=str(tmp_path / "Stats_out_MCMC_iter.csv"),
        stats_out_mcmc_trace=str(tmp_path / "Stats_out_MCMC_trace.pdf"),
        stats_out_mcmc_iter_summ_stat=str(
            tmp_path / "Stats_out_MCMC_iter_summ_stat.csv"
        ),
        stats_out_post_pred=str(tmp_path / "Stats_out_post_pred.pdf"),
        stats_out_mcmc_correct_prob=str(tmp_path / "Stats_out_MCMC_correct_prob.csv"),
        dnacomp_genome=str(tmp_path / "dnacomp_genome.txt"),
        rescaled_bam=str(tmp_path / "rescaled_test.bam"),
        print_only=True,
    )

    # Capture the printed Snakefile content
    captured = capsys.readouterr()
    content = captured.out

    # Verify the essential params are present
    assert "rule mapdamage2:" in content, "Missing rule definition"
    assert "input:" in content, "Missing input section"
    assert "output:" in content, "Missing output section"
    assert "params:" in content, "Missing params section"
    assert "wrapper:" in content, "Missing wrapper section"

    # Assertions for inputs
    assert "alignment_file=" in content, "Missing alignment_file input"
    assert "reference_genome=" in content, "Missing reference_genome input"

    # Assertions for outputs
    assert "runtime_log=" in content, "Missing runtime_log output"
    assert "fragmisincorporation_plot=" in content, (
        "Missing fragmisincorporation_plot output"
    )
    assert "length_plot=" in content, "Missing length_plot output"
    assert "misincorporation_txt=" in content, "Missing misincorporation_txt output"
    assert "five_prime_ctot_freq=" in content, "Missing 5pCtoT_freq.txt output"
    assert "three_prime_gtoa_freq=" in content, "Missing 3pGtoA_freq.txt output"
    assert "dnacomp_txt=" in content, "Missing dnacomp.txt output"
    assert "lgdistribution_txt=" in content, "Missing lgdistribution.txt output"
    assert "stats_out_mcmc_hist=" in content, "Missing Stats_out_MCMC_hist output"
    assert "stats_out_mcmc_iter=" in content, "Missing Stats_out_MCMC_iter output"
    assert "stats_out_mcmc_trace=" in content, "Missing Stats_out_MCMC_trace output"
    assert "stats_out_mcmc_iter_summ_stat=" in content, (
        "Missing Stats_out_MCMC_iter_summ_stat output"
    )
    assert "stats_out_post_pred=" in content, "Missing Stats_out_post_pred output"
    assert "stats_out_mcmc_correct_prob=" in content, (
        "Missing Stats_out_MCMC_correct_prob output"
    )
    assert "dnacomp_genome=" in content, "Missing dnacomp_genome output"
    assert "rescaled_bam=" in content, "Missing rescaled_bam output"


def test_run_mapdamage2(test_paths, tmp_path):
    """Test that mapdamage2 can be run with the test files."""
    from bioinformatics_mcp.mapdamage2.mcp.run_mapdamage2 import run_mapdamage2

    # Run mapdamage2
    result = run_mapdamage2(
        reference_genome=str(test_paths["reference_genome"]),
        alignment_file=str(test_paths["alignment_file"]),
        runtime_log=str(tmp_path / "runtime_log.txt"),
        fragmisincorporation_plot=str(tmp_path / "Fragmisincorporation_plot.pdf"),
        length_plot=str(tmp_path / "Length_plot.pdf"),
        misincorporation_txt=str(tmp_path / "misincorporation.txt"),
        five_prime_ctot_freq=str(tmp_path / "5pCtoT_freq.txt"),
        three_prime_gtoa_freq=str(tmp_path / "3pGtoA_freq.txt"),
        dnacomp_txt=str(tmp_path / "dnacomp.txt"),
        lgdistribution_txt=str(tmp_path / "lgdistribution.txt"),
        stats_out_mcmc_hist=str(tmp_path / "Stats_out_MCMC_hist.pdf"),
        stats_out_mcmc_iter=str(tmp_path / "Stats_out_MCMC_iter.csv"),
        stats_out_mcmc_trace=str(tmp_path / "Stats_out_MCMC_trace.pdf"),
        stats_out_mcmc_iter_summ_stat=str(
            tmp_path / "Stats_out_MCMC_iter_summ_stat.csv"
        ),
        stats_out_post_pred=str(tmp_path / "Stats_out_post_pred.pdf"),
        stats_out_mcmc_correct_prob=str(tmp_path / "Stats_out_MCMC_correct_prob.csv"),
        dnacomp_genome=str(tmp_path / "dnacomp_genome.txt"),
        rescaled_bam=str(tmp_path / "rescaled_test.bam"),
    )

    # Verify successful run
    assert result.returncode == 0, "mapdamage2 run failed"

    # Verify essential output files exist
    assert (tmp_path / "runtime_log.txt").exists(), "runtime_log.txt not generated"
    assert (tmp_path / "Fragmisincorporation_plot.pdf").exists(), (
        "Fragmisincorporation_plot.pdf not generated"
    )
    assert (tmp_path / "Length_plot.pdf").exists(), "Length_plot.pdf not generated"
    assert (tmp_path / "misincorporation.txt").exists(), (
        "misincorporation.txt not generated"
    )
    assert (tmp_path / "5pCtoT_freq.txt").exists(), "5pCtoT_freq.txt not generated"
    assert (tmp_path / "3pGtoA_freq.txt").exists(), "3pGtoA_freq.txt not generated"
    assert (tmp_path / "dnacomp.txt").exists(), "dnacomp.txt not generated"
    assert (tmp_path / "lgdistribution.txt").exists(), (
        "lgdistribution.txt not generated"
    )
    assert (tmp_path / "Stats_out_MCMC_hist.pdf").exists(), (
        "Stats_out_MCMC_hist.pdf not generated"
    )
    assert (tmp_path / "Stats_out_MCMC_iter.csv").exists(), (
        "Stats_out_MCMC_iter.csv not generated"
    )
    assert (tmp_path / "Stats_out_MCMC_trace.pdf").exists(), (
        "Stats_out_MCMC_trace.pdf not generated"
    )
    assert (tmp_path / "Stats_out_MCMC_iter_summ_stat.csv").exists(), (
        "Stats_out_MCMC_iter_summ_stat.csv not generated"
    )
    assert (tmp_path / "Stats_out_post_pred.pdf").exists(), (
        "Stats_out_post_pred.pdf not generated"
    )
    assert (tmp_path / "Stats_out_MCMC_correct_prob.csv").exists(), (
        "Stats_out_MCMC_correct_prob.csv not generated"
    )
    assert (tmp_path / "dnacomp_genome.txt").exists(), (
        "dnacomp_genome.txt not generated"
    )
    assert (tmp_path / "rescaled_test.bam").exists(), "Rescaled BAM file not generated"
