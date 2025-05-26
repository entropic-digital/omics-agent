from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_gtfToGenePred(
    *,
    gtf_file: str,
    gene_pred_table: str,
    extra: Optional[str] = None,
    convert_out: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert a GTF file to genePred format.

    Args:
        gtf_file: Input GTF file to be converted.
        gene_pred_table: Output file in genePred table format.
        extra (optional): Additional program arguments.
        convert_out (optional): Conversion type to apply to the `refFlat` output.
                                For example: 'PicardCollectRnaSeqMetrics'.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = (
        {"extra": extra, "convert_out": convert_out} if extra or convert_out else {}
    )
    return run_snake_wrapper(
        wrapper="file:tools/ucsc/gtfToGenePred",
        inputs=dict(gtf_file=gtf_file),
        outputs=dict(gene_pred_table=gene_pred_table),
        params=params,
         
    )


@collect_tool()
def gtfToGenePred(
    *,
    gtf_file: str,
    gene_pred_table: str,
    extra: Optional[str] = None,
    convert_out: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert a GTF file to genePred format.

    Args:
        gtf_file: Input GTF file to be converted.
        gene_pred_table: Output file in genePred table format.
        extra (optional): Additional program arguments.
        convert_out (optional): Conversion type to apply to the `refFlat` output.
                                For example: 'PicardCollectRnaSeqMetrics'.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_gtfToGenePred(
        gtf_file=gtf_file,
        gene_pred_table=gene_pred_table,
        extra=extra,
        convert_out=convert_out,
         
    )
