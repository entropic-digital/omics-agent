from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_autoindex(
    *,
    ref: str,
    vcf: Optional[str] = None,
    gbz: str,
    dist: str,
    min_idx: str,
    zipcodes: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Creates index files for mapping reads via `vg giraffe`.

    Args:
        ref: FASTA reference file.
        vcf (optional): Haplotypes in VCF format.
        gbz: Output GBZ graph file (.giraffe.gbz).
        dist: Output Distance index file (.dist).
        min_idx: Output Minimizer index file (.shortread.withzip.min).
        zipcodes: Output Zipcodes file (.shortread.zipcodes).
        extra (optional): Additional arguments for `vg autoindex`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/vg/autoindex",
        inputs={"ref": ref, "vcf": vcf} if vcf else {"ref": ref},
        outputs={"gbz": gbz, "dist": dist, "min_idx": min_idx, "zipcodes": zipcodes},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def autoindex(
    *,
    ref: str,
    vcf: Optional[str] = None,
    gbz: str,
    dist: str,
    min_idx: str,
    zipcodes: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Creates index files for mapping reads via `vg giraffe`.

    Args:
        ref: FASTA reference file.
        vcf (optional): Haplotypes in VCF format.
        gbz: Output GBZ graph file (.giraffe.gbz).
        dist: Output Distance index file (.dist).
        min_idx: Output Minimizer index file (.shortread.withzip.min).
        zipcodes: Output Zipcodes file (.shortread.zipcodes).
        extra (optional): Additional arguments for `vg autoindex`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_autoindex(
        ref=ref,
        vcf=vcf,
        gbz=gbz,
        dist=dist,
        min_idx=min_idx,
        zipcodes=zipcodes,
        extra=extra,
         
    )
