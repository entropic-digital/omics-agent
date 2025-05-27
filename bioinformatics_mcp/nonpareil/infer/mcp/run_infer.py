from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_infer(
    *,
    reads: str,
    redund_sum: str,
    redund_val: str,
    mate_distr: str,
    log: str,
    alg: str,
    infer_X: bool,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Nonpareil infer tool.

    Nonpareil uses the redundancy of the reads in metagenomic datasets to estimate
    the average coverage and predict the amount of sequences that will be required
    to achieve “nearly complete coverage”.

    Args:
        reads: Input reads in FASTA/Q format (can be gzipped or bzipped).
        redund_sum: Output TSV file for redundancy summary (six columns).
        redund_val: Output TSV file for redundancy values (three columns).
        mate_distr: Output mate distribution file.
        log: Output log file for Nonpareil processing.
        alg: Nonpareil algorithm, either `kmer` or `alignment` (mandatory).
        infer_X: Whether to automatically infer value of `-X` (slower for counting reads).
        extra (optional): Additional program arguments (not `-X` if infer_X is True).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/nonpareil/infer",
        inputs={"reads": reads},
        outputs={
            "redund_sum": redund_sum,
            "redund_val": redund_val,
            "mate_distr": mate_distr,
            "log": log,
        },
        params={
            "alg": alg,
            "infer_X": str(infer_X).lower(),
            "extra": extra,
        },
         
    )


@collect_tool()
def infer(
    *,
    reads: str,
    redund_sum: str,
    redund_val: str,
    mate_distr: str,
    log: str,
    alg: str,
    infer_X: bool,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the Nonpareil infer tool.

    Nonpareil uses the redundancy of the reads in metagenomic datasets to estimate
    the average coverage and predict the amount of sequences that will be required
    to achieve “nearly complete coverage”.

    Args:
        reads: Input reads in FASTA/Q format (can be gzipped or bzipped).
        redund_sum: Output TSV file for redundancy summary (six columns).
        redund_val: Output TSV file for redundancy values (three columns).
        mate_distr: Output mate distribution file.
        log: Output log file for Nonpareil processing.
        alg: Nonpareil algorithm, either `kmer` or `alignment` (mandatory).
        infer_X: Whether to automatically infer value of `-X` (slower for counting reads).
        extra (optional): Additional program arguments (not `-X` if infer_X is True).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_infer(
        reads=reads,
        redund_sum=redund_sum,
        redund_val=redund_val,
        mate_distr=mate_distr,
        log=log,
        alg=alg,
        infer_X=infer_X,
        extra=extra,
         
    )
