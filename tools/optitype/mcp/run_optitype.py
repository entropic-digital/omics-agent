from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_optitype(
    *,
    fastq1: str,
    fastq2: Optional[str] = None,
    configfile: Optional[str] = None,
    figsize: Optional[str] = None,
    img_format: Optional[str] = "pdf",
    nofig: Optional[bool] = False,
    outdir: str,
    prefix: str,
    dna: Optional[bool] = False,
    rna: Optional[bool] = False,
     
) -> subprocess.CompletedProcess:
    """
    Precision 4-digit HLA-I-typing from NGS data based on integer linear programming.

    Args:
        fastq1: Path to the first FastQ file.
        fastq2 (optional): Path to the second FastQ file.
        configfile (optional): Path to the OptiType configuration file.
        figsize (optional): Size of the figure, if generated.
        img_format (optional): Image format for figures, default is 'pdf'.
        nofig (optional): Whether to suppress figure generation.
        outdir: Path to the output directory.
        prefix: Prefix for output files.
        dna (optional): Indicates DNA input.
        rna (optional): Indicates RNA input.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "configfile": configfile,
        "figsize": figsize,
        "img_format": img_format,
        "nofig": nofig,
        "dna": dna,
        "rna": rna,
    }
    # Only pass non-None params to the Snakemake wrapper
    params = {k: v for k, v in params.items() if v is not None}

    return run_snake_wrapper(
        wrapper="file:tools/optitype",
        inputs={"fastq1": fastq1, "fastq2": fastq2} if fastq2 else {"fastq1": fastq1},
        outputs={"outdir": outdir},
        params={"prefix": prefix, **params},
         
    )


@collect_tool()
def optitype(
    *,
    fastq1: str,
    fastq2: Optional[str] = None,
    configfile: Optional[str] = None,
    figsize: Optional[str] = None,
    img_format: Optional[str] = "pdf",
    nofig: Optional[bool] = False,
    outdir: str,
    prefix: str,
    dna: Optional[bool] = False,
    rna: Optional[bool] = False,
     
) -> subprocess.CompletedProcess:
    """
    Precision 4-digit HLA-I-typing from NGS data based on integer linear programming.

    Args:
        fastq1: Path to the first FastQ file.
        fastq2 (optional): Path to the second FastQ file.
        configfile (optional): Path to the OptiType configuration file.
        figsize (optional): Size of the figure, if generated.
        img_format (optional): Image format for figures, default is 'pdf'.
        nofig (optional): Whether to suppress figure generation.
        outdir: Path to the output directory.
        prefix: Prefix for output files.
        dna (optional): Indicates DNA input.
        rna (optional): Indicates RNA input.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_optitype(
        fastq1=fastq1,
        fastq2=fastq2,
        configfile=configfile,
        figsize=figsize,
        img_format=img_format,
        nofig=nofig,
        outdir=outdir,
        prefix=prefix,
        dna=dna,
        rna=rna,
         
    )
