from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_vardict(
    *,
    reference: str,
    bam: str,
    region: str,
    normal: Optional[str] = None,
    output: str,
    extra: Optional[str] = None,
    bed_columns: str = "-c 1 -S 2 -E 3 -g 4",
    ah_th: float = 0.01,
     
) -> subprocess.CompletedProcess:
    """
    Run Vardict to call genomic variants.

    Args:
        reference: Path to the reference genome file.
        bam: Path to the BAM file for analysis.
        region: Path to the regions of interest file.
        normal (optional): Path to the normal BAM file for tumor/normal mode.
        output: Path to the output VCF file.
        extra (optional): Additional parameters for Vardict.
        bed_columns (optional): BED file column format, defaults to '-c 1 -S 2 -E 3 -g 4'.
        ah_th (optional): Allele frequency threshold, defaults to 0.01.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "reference": reference,
        "bam": bam,
        "region": region,
    }
    if normal:
        inputs["normal"] = normal

    params = {
        "bed_columns": bed_columns,
        "ah_th": ah_th,
    }
    if extra:
        params["extra"] = extra

    outputs = {
        "output": output,
    }

    return run_snake_wrapper(
        wrapper="file:tools/vardict",
        inputs=inputs,
        params=params,
        outputs=outputs,
         
    )


@collect_tool()
def vardict(
    *,
    reference: str,
    bam: str,
    region: str,
    normal: Optional[str] = None,
    output: str,
    extra: Optional[str] = None,
    bed_columns: str = "-c 1 -S 2 -E 3 -g 4",
    ah_th: float = 0.01,
     
) -> subprocess.CompletedProcess:
    """
    Run Vardict to call genomic variants.

    Args:
        reference: Path to the reference genome file.
        bam: Path to the BAM file for analysis.
        region: Path to the regions of interest file.
        normal (optional): Path to the normal BAM file for tumor/normal mode.
        output: Path to the output VCF file.
        extra (optional): Additional parameters for Vardict.
        bed_columns (optional): BED file column format, defaults to '-c 1 -S 2 -E 3 -g 4'.
        ah_th (optional): Allele frequency threshold, defaults to 0.01.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_vardict(
        reference=reference,
        bam=bam,
        region=region,
        normal=normal,
        output=output,
        extra=extra,
        bed_columns=bed_columns,
        ah_th=ah_th,
         
    )
