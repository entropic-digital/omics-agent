from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_indelqual(
    *,
    bam_file: str,
    reference_genome: Optional[str] = None,
    output_bam: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Insert indel qualities into a BAM file (required for indel predictions).

    Args:
        bam_file: Input BAM file that will have variants called.
        reference_genome (optional): Reference genome of the BAM file. Required if --dindel is specified in extra.
        output_bam: Output BAM file with indel qualities added.
        extra (optional): Additional parameters, e.g., `--uniform INT[,INT]` (uniform quality) or `--dindel` (dindel's indel qualities).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {"bam_file": bam_file}
    if reference_genome:
        inputs["reference_genome"] = reference_genome

    params = {"extra": extra} if extra else {}

    return run_snake_wrapper(
        wrapper="file:tools/lofreq/indelqual",
        inputs=inputs,
        params=params,
        outputs={"output_bam": output_bam},
         
    )


@collect_tool()
def indelqual(
    *,
    bam_file: str,
    reference_genome: Optional[str] = None,
    output_bam: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Insert indel qualities into a BAM file (required for indel predictions).

    Args:
        bam_file: Input BAM file that will have variants called.
        reference_genome (optional): Reference genome of the BAM file. Required if --dindel is specified in extra.
        output_bam: Output BAM file with indel qualities added.
        extra (optional): Additional parameters, e.g., `--uniform INT[,INT]` (uniform quality) or `--dindel` (dindel's indel qualities).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_indelqual(
        bam_file=bam_file,
        reference_genome=reference_genome,
        output_bam=output_bam,
        extra=extra,
         
    )
