from typing import List, Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_samplesimilarity(
    *,
    samples: List[str],
    output: str,
    ref: Optional[str] = None,
    regions: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate several metrics that measure sample similarity.

    Args:
        samples: List of paths to VCF/VCF.GZ files, or list of paths to BAM/SAM/CRAM files.
        output: Path to output TSV results.
        ref (optional): Path to reference genome index file (FAI). Required for CRAM input.
        regions (optional): Path to regions of interest (BED).
        extra (optional): Additional parameters besides IO or `-mode`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/ngsbits/samplesimilarity",
        inputs={"samples": samples, "ref": ref, "regions": regions},
        params={"extra": extra} if extra else {},
        outputs={"output": output},
         
    )


@collect_tool()
def samplesimilarity(
    *,
    samples: List[str],
    output: str,
    ref: Optional[str] = None,
    regions: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate several metrics that measure sample similarity.

    Args:
        samples: List of paths to VCF/VCF.GZ files, or list of paths to BAM/SAM/CRAM files.
        output: Path to output TSV results.
        ref (optional): Path to reference genome index file (FAI). Required for CRAM input.
        regions (optional): Path to regions of interest (BED).
        extra (optional): Additional parameters besides IO or `-mode`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_samplesimilarity(
        samples=samples,
        output=output,
        ref=ref,
        regions=regions,
        extra=extra,
         
    )
