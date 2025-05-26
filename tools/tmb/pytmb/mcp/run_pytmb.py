from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_pytmb(
    *,
    vcf: str,
    db_config: str,
    var_config: str,
    bed: str,
    res: str,
    vcf_output: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate a Tumor Mutational Burden (TMB) score from a VCF file.

    Args:
        vcf: Path to input variants (`vcf`, `vcf.gz`, or `bcf` formatted).
        db_config: Path to database config file (`yaml` formatted).
        var_config: Path to variant config file (`yaml` formatted).
        bed: Path to intervals file to compute effective genome size (`bed` formatted).
        res: Path to TMB results.
        vcf_output (optional): Optional path to variants considered for TMB calculation.
        extra (optional): Optional parameters provided to `pyTMB.py`, besides
                          `-i`, `--dbConfig`, `--varConfig`, `--bed`, or `--export`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/tmb/pytmb",
        inputs=dict(vcf=vcf, db_config=db_config, var_config=var_config, bed=bed),
        outputs=dict(res=res, vcf=vcf_output),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def pytmb(
    *,
    vcf: str,
    db_config: str,
    var_config: str,
    bed: str,
    res: str,
    vcf_output: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate a Tumor Mutational Burden (TMB) score from a VCF file.

    Args:
        vcf: Path to input variants (`vcf`, `vcf.gz`, or `bcf` formatted).
        db_config: Path to database config file (`yaml` formatted).
        var_config: Path to variant config file (`yaml` formatted).
        bed: Path to intervals file to compute effective genome size (`bed` formatted).
        res: Path to TMB results.
        vcf_output (optional): Optional path to variants considered for TMB calculation.
        extra (optional): Optional parameters provided to `pyTMB.py`, besides
                          `-i`, `--dbConfig`, `--varConfig`, `--bed`, or `--export`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_pytmb(
        vcf=vcf,
        db_config=db_config,
        var_config=var_config,
        bed=bed,
        res=res,
        vcf_output=vcf_output,
        extra=extra,
         
    )
