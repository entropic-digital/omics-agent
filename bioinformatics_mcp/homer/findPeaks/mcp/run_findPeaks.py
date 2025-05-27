from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_findPeaks(
    *,
    input_bam: str,
    output_dir: str,
    genome: str,
    style: Optional[str] = None,
    fragLength: Optional[str] = None,
    size: Optional[str] = None,
    input_control: Optional[str] = None,
    minDist: Optional[str] = None,
    region: Optional[str] = None,
    fdr: Optional[str] = None,
    fold_enrichment: Optional[str] = None,
    gsize: Optional[str] = None,
    nolambda: Optional[bool] = False,
    local_size: Optional[str] = None,
    num_processors: Optional[int] = None,
    tage_directory: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Find ChIP- or ATAC-Seq peaks with the HOMER suite.

    Args:
        input_bam: Path to the input BAM file.
        output_dir: Directory for the output results.
        genome: Reference genome to analyze.
        style (optional): Specify a data style to use with HOMER (e.g., "factor", "histone").
        fragLength (optional): Fragment length for peak finding.
        size (optional): Window size for peak widths.
        input_control (optional): Path to a control/input file for peak normalization.
        minDist (optional): Minimum distance between valid peaks.
        region (optional): Restrict peak finding to a particular region.
        fdr (optional): False Discovery Rate (FDR) cutoff value.
        fold_enrichment (optional): Minimum fold enrichment for peaks.
        gsize (optional): Genome size hint.
        nolambda (optional): Disable local lambda step in HOMER algorithm (default: False).
        local_size (optional): Size for local peak statistics.
        num_processors (optional): Number of processors to use.
        tage_directory (optional): Path to input HOMER tage directory.
  
    Returns:
        subprocess.CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/homer/findPeaks",
        inputs={
            "bam": input_bam,
        },
        outputs={
            "output_dir": output_dir,
        },
        params={
            "genome": genome,
            "style": style,
            "fragLength": fragLength,
            "size": size,
            "input_control": input_control,
            "minDist": minDist,
            "region": region,
            "fdr": fdr,
            "fold_enrichment": fold_enrichment,
            "gsize": gsize,
            "nolambda": nolambda,
            "local_size": local_size,
            "num_processors": num_processors,
            "tage_directory": tage_directory,
        },
         
    )


@collect_tool()
def findPeaks(
    *,
    input_bam: str,
    output_dir: str,
    genome: str,
    style: Optional[str] = None,
    fragLength: Optional[str] = None,
    size: Optional[str] = None,
    input_control: Optional[str] = None,
    minDist: Optional[str] = None,
    region: Optional[str] = None,
    fdr: Optional[str] = None,
    fold_enrichment: Optional[str] = None,
    gsize: Optional[str] = None,
    nolambda: Optional[bool] = False,
    local_size: Optional[str] = None,
    num_processors: Optional[int] = None,
    tage_directory: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Find ChIP- or ATAC-Seq peaks with the HOMER suite.

    Args:
        input_bam: Path to the input BAM file.
        output_dir: Directory for the output results.
        genome: Reference genome to analyze.
        style (optional): Specify a data style to use with HOMER (e.g., "factor", "histone").
        fragLength (optional): Fragment length for peak finding.
        size (optional): Window size for peak widths.
        input_control (optional): Path to a control/input file for peak normalization.
        minDist (optional): Minimum distance between valid peaks.
        region (optional): Restrict peak finding to a particular region.
        fdr (optional): False Discovery Rate (FDR) cutoff value.
        fold_enrichment (optional): Minimum fold enrichment for peaks.
        gsize (optional): Genome size hint.
        nolambda (optional): Disable local lambda step in HOMER algorithm (default: False).
        local_size (optional): Size for local peak statistics.
        num_processors (optional): Number of processors to use.
        tage_directory (optional): Path to input HOMER tage directory.
  
    Returns:
        subprocess.CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_findPeaks(
        input_bam=input_bam,
        output_dir=output_dir,
        genome=genome,
        style=style,
        fragLength=fragLength,
        size=size,
        input_control=input_control,
        minDist=minDist,
        region=region,
        fdr=fdr,
        fold_enrichment=fold_enrichment,
        gsize=gsize,
        nolambda=nolambda,
        local_size=local_size,
        num_processors=num_processors,
        tage_directory=tage_directory,
         
    )
