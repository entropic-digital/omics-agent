from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_rasusa(
    *,
    input_reads: str,
    output_reads: str,
    bases: Optional[str] = None,
    coverage: Optional[str] = None,
    genome_size: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Randomly subsample sequencing reads to a specified coverage.

    Args:
        input_reads: Reads to subsample in FASTA/Q format.
        output_reads: File path to write subsampled reads to. For paired-end data,
                      there should be two output files in the same order as the input.
        bases (optional): Explicitly set the number of bases required (e.g., 4.3kb, 7Tb, 4.1MB).
                          If this is provided, 'coverage' and 'genome_size' are ignored.
        coverage (optional): Desired coverage to subsample the reads to. This is
                             required if 'bases' is not provided.
        genome_size (optional): Genome size to calculate coverage with respect to.
                                This is required if 'bases' is not provided. Alternatively,
                                a FASTA/Q index file can be provided.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/rasusa",
        inputs=dict(input_reads=input_reads),
        outputs=dict(output_reads=output_reads),
        params={
            "bases": bases,
            "coverage": coverage,
            "genome_size": genome_size,
            "extra": extra,
        },
         
    )


@collect_tool()
def rasusa(
    *,
    input_reads: str,
    output_reads: str,
    bases: Optional[str] = None,
    coverage: Optional[str] = None,
    genome_size: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Randomly subsample sequencing reads to a specified coverage.

    Args:
        input_reads: Reads to subsample in FASTA/Q format.
        output_reads: File path to write subsampled reads to. For paired-end data,
                      there should be two output files in the same order as the input.
        bases (optional): Explicitly set the number of bases required (e.g., 4.3kb, 7Tb, 4.1MB).
                          If this is provided, 'coverage' and 'genome_size' are ignored.
        coverage (optional): Desired coverage to subsample the reads to. This is
                             required if 'bases' is not provided.
        genome_size (optional): Genome size to calculate coverage with respect to.
                                This is required if 'bases' is not provided. Alternatively,
                                a FASTA/Q index file can be provided.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_rasusa(
        input_reads=input_reads,
        output_reads=output_reads,
        bases=bases,
        coverage=coverage,
        genome_size=genome_size,
        extra=extra,
         
    )
