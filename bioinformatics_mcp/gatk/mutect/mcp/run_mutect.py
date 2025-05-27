from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_mutect(
    *,
    map: str,
    fasta: str,
    vcf: str,
    intervals: Optional[str] = None,
    pon: Optional[str] = None,
    germline: Optional[str] = None,
    bam: Optional[str] = None,
    f1r2: Optional[str] = None,
    extra: Optional[str] = None,
    use_parallelgc: bool = False,
    use_omp: bool = False,
    java_opts: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call somatic SNVs and indels via local assembly of haplotypes using GATK Mutect2.

    Args:
        map: Path to mapped reads (SAM/BAM/CRAM).
        fasta: Path to the reference FASTA file.
        vcf: Path to the output variant file.
        intervals (optional): Path to a BED interval file.
        pon (optional): Path to the Panel of Normals (BETA).
        germline (optional): Path to known germline variants.
        bam (optional): Path to the output BAM file.
        f1r2 (optional): Path to the F1R2 count file.
        extra (optional): Additional parameters for GATK Mutect2.
        use_parallelgc: Whether to automatically add `-XX:ParallelGCThreads={snakemake.threads}`.
        use_omp: Whether to automatically set the `OMP_NUM_THREADS` environment variable.
        java_opts (optional): Additional arguments for the Java compiler.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "extra": extra,
        "use_parallelgc": use_parallelgc,
        "use_omp": use_omp,
        "java_opts": java_opts,
    }
    outputs = {
        "vcf": vcf,
        "bam": bam,
        "f1r2": f1r2,
    }

    inputs = {
        "map": map,
        "fasta": fasta,
        "intervals": intervals,
        "pon": pon,
        "germline": germline,
    }

    # Filter out None values to avoid passing unnecessary arguments
    params = {k: v for k, v in params.items() if v is not None}
    inputs = {k: v for k, v in inputs.items() if v is not None}
    outputs = {k: v for k, v in outputs.items() if v is not None}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/mutect",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def mutect(
    *,
    map: str,
    fasta: str,
    vcf: str,
    intervals: Optional[str] = None,
    pon: Optional[str] = None,
    germline: Optional[str] = None,
    bam: Optional[str] = None,
    f1r2: Optional[str] = None,
    extra: Optional[str] = None,
    use_parallelgc: bool = False,
    use_omp: bool = False,
    java_opts: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call somatic SNVs and indels via local assembly of haplotypes using GATK Mutect2.

    Args:
        map: Path to mapped reads (SAM/BAM/CRAM).
        fasta: Path to the reference FASTA file.
        vcf: Path to the output variant file.
        intervals (optional): Path to a BED interval file.
        pon (optional): Path to the Panel of Normals (BETA).
        germline (optional): Path to known germline variants.
        bam (optional): Path to the output BAM file.
        f1r2 (optional): Path to the F1R2 count file.
        extra (optional): Additional parameters for GATK Mutect2.
        use_parallelgc: Whether to automatically add `-XX:ParallelGCThreads={snakemake.threads}`.
        use_omp: Whether to automatically set the `OMP_NUM_THREADS` environment variable.
        java_opts (optional): Additional arguments for the Java compiler.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mutect(
        map=map,
        fasta=fasta,
        vcf=vcf,
        intervals=intervals,
        pon=pon,
        germline=germline,
        bam=bam,
        f1r2=f1r2,
        extra=extra,
        use_parallelgc=use_parallelgc,
        use_omp=use_omp,
        java_opts=java_opts,
         
    )
