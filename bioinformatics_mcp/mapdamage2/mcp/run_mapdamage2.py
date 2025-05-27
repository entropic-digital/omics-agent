from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_mapdamage2(
    *,
    reference_genome: str,
    alignment_file: str,
    runtime_log: str,
    fragmisincorporation_plot: Optional[str] = None,
    length_plot: Optional[str] = None,
    misincorporation_txt: Optional[str] = None,
    five_prime_ctot_freq: Optional[str] = None,
    three_prime_gtoa_freq: Optional[str] = None,
    dnacomp_txt: Optional[str] = None,
    lgdistribution_txt: Optional[str] = None,
    stats_out_mcmc_hist: Optional[str] = None,
    stats_out_mcmc_iter: Optional[str] = None,
    stats_out_mcmc_trace: Optional[str] = None,
    stats_out_mcmc_iter_summ_stat: Optional[str] = None,
    stats_out_post_pred: Optional[str] = None,
    stats_out_mcmc_correct_prob: Optional[str] = None,
    dnacomp_genome: Optional[str] = None,
    rescaled_bam: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Runs the mapDamage2 computational framework to quantify DNA damage patterns.

    Args:
        reference_genome: Path to the reference genome file.
        alignment_file: Path to the alignment file (SAM/BAM/CRAM format).
        runtime_log: Path to save the runtime log file.
        fragmisincorporation_plot: Path to save the fragmentation and misincorporation plot.
        length_plot: Path to save the length distribution plot.
        misincorporation_txt: Path to save the misincorporation table.
        five_prime_ctot_freq: Path to save C->T mutation frequencies (5'-ends).
        three_prime_gtoa_freq: Path to save G->A mutation frequencies (3'-ends).
        dnacomp_txt: Path to save reference genome base composition per position.
        lgdistribution_txt: Path to save read-length distributions per strand.
        stats_out_mcmc_hist: Path to save MCMC histogram of damage parameters.
        stats_out_mcmc_iter: Path to save MCMC iteration values.
        stats_out_mcmc_trace: Path to save MCMC trace plot.
        stats_out_mcmc_iter_summ_stat: Path to save MCMC iteration summary statistics.
        stats_out_post_pred: Path to save posterior predictive damage parameters.
        stats_out_mcmc_correct_prob: Path to save position-specific damage probabilities.
        dnacomp_genome: Path to save global reference genome base composition.
        rescaled_bam: Path to output BAM file with rescaled base quality scores.
        extra: Additional command-line arguments for mapDamage2.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "reference_genome": reference_genome,
        "alignment_file": alignment_file,
    }
    outputs = {
        "runtime_log": runtime_log,
        "fragmisincorporation_plot": fragmisincorporation_plot,
        "length_plot": length_plot,
        "misincorporation_txt": misincorporation_txt,
        "five_prime_ctot_freq": five_prime_ctot_freq,
        "three_prime_gtoa_freq": three_prime_gtoa_freq,
        "dnacomp_txt": dnacomp_txt,
        "lgdistribution_txt": lgdistribution_txt,
        "stats_out_mcmc_hist": stats_out_mcmc_hist,
        "stats_out_mcmc_iter": stats_out_mcmc_iter,
        "stats_out_mcmc_trace": stats_out_mcmc_trace,
        "stats_out_mcmc_iter_summ_stat": stats_out_mcmc_iter_summ_stat,
        "stats_out_post_pred": stats_out_post_pred,
        "stats_out_mcmc_correct_prob": stats_out_mcmc_correct_prob,
        "dnacomp_genome": dnacomp_genome,
        "rescaled_bam": rescaled_bam,
    }
    params = {"extra": extra} if extra else {}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/mapdamage2",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def mapdamage2(
    *,
    reference_genome: str,
    alignment_file: str,
    runtime_log: str,
    fragmisincorporation_plot: Optional[str] = None,
    length_plot: Optional[str] = None,
    misincorporation_txt: Optional[str] = None,
    five_prime_ctot_freq: Optional[str] = None,
    three_prime_gtoa_freq: Optional[str] = None,
    dnacomp_txt: Optional[str] = None,
    lgdistribution_txt: Optional[str] = None,
    stats_out_mcmc_hist: Optional[str] = None,
    stats_out_mcmc_iter: Optional[str] = None,
    stats_out_mcmc_trace: Optional[str] = None,
    stats_out_mcmc_iter_summ_stat: Optional[str] = None,
    stats_out_post_pred: Optional[str] = None,
    stats_out_mcmc_correct_prob: Optional[str] = None,
    dnacomp_genome: Optional[str] = None,
    rescaled_bam: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Runs the mapDamage2 computational framework through a decorated MCP tool wrapper function.

    Args:
        reference_genome: Path to the reference genome file.
        alignment_file: Path to the alignment file (SAM/BAM/CRAM format).
        runtime_log: Path to save the runtime log file.
        fragmisincorporation_plot: Path to save the fragmentation and misincorporation plot.
        length_plot: Path to save the length distribution plot.
        misincorporation_txt: Path to save the misincorporation table.
        five_prime_ctot_freq: Path to save C->T mutation frequencies (5'-ends).
        three_prime_gtoa_freq: Path to save G->A mutation frequencies (3'-ends).
        dnacomp_txt: Path to save reference genome base composition per position.
        lgdistribution_txt: Path to save read-length distributions per strand.
        stats_out_mcmc_hist: Path to save MCMC histogram of damage parameters.
        stats_out_mcmc_iter: Path to save MCMC iteration values.
        stats_out_mcmc_trace: Path to save MCMC trace plot.
        stats_out_mcmc_iter_summ_stat: Path to save MCMC iteration summary statistics.
        stats_out_post_pred: Path to save posterior predictive damage parameters.
        stats_out_mcmc_correct_prob: Path to save position-specific damage probabilities.
        dnacomp_genome: Path to save global reference genome base composition.
        rescaled_bam: Path to output BAM file with rescaled base quality scores.
        extra: Additional command-line arguments for mapDamage2.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mapdamage2(
        reference_genome=reference_genome,
        alignment_file=alignment_file,
        runtime_log=runtime_log,
        fragmisincorporation_plot=fragmisincorporation_plot,
        length_plot=length_plot,
        misincorporation_txt=misincorporation_txt,
        five_prime_ctot_freq=five_prime_ctot_freq,
        three_prime_gtoa_freq=three_prime_gtoa_freq,
        dnacomp_txt=dnacomp_txt,
        lgdistribution_txt=lgdistribution_txt,
        stats_out_mcmc_hist=stats_out_mcmc_hist,
        stats_out_mcmc_iter=stats_out_mcmc_iter,
        stats_out_mcmc_trace=stats_out_mcmc_trace,
        stats_out_mcmc_iter_summ_stat=stats_out_mcmc_iter_summ_stat,
        stats_out_post_pred=stats_out_post_pred,
        stats_out_mcmc_correct_prob=stats_out_mcmc_correct_prob,
        dnacomp_genome=dnacomp_genome,
        rescaled_bam=rescaled_bam,
        extra=extra,
         
    )
