from typing import Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_wald(
    *,
    dds: str,
    wald_rds: Optional[str] = None,
    wald_tsv: Optional[str] = None,
    deseq2_result_dir: Optional[str] = None,
    normalized_counts_table: Optional[str] = None,
    normalized_counts_rds: Optional[str] = None,
    deseq_extra: Optional[str] = None,
    schrink_extra: Optional[str] = None,
    results_extra: Optional[str] = None,
    contrast: Optional[List[str]] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call differentially expressed genes with DESeq2.

    Args:
        dds: Path to RDS-formatted DESeq2-object.
        wald_rds (optional): Optional path to wald test results (RDS formatted).
        wald_tsv (optional): Optional path to wald test results (TSV formatted).
                             Requires the `contrast` parameter (see notes below).
        deseq2_result_dir (optional): Optional path to a directory containing
                                      all DESeq2 results (each file TSV formatted).
        normalized_counts_table (optional): Optional path to normalized counts (TSV formatted).
        normalized_counts_rds (optional): Optional path to normalized counts (RDS formatted).
        deseq_extra (optional): Additional parameters for the `DESeq()` function.
        schrink_extra (optional): Additional parameters for the `lfSchrink()` function.
        results_extra (optional): Additional parameters for the `result()` function.
        contrast (optional): List of characters specifying the comparison to extract.
                             Refer to documentation for `DESeq2` contrast parameter.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {"dds": dds}
    outputs = {
        "wald_rds": wald_rds,
        "wald_tsv": wald_tsv,
        "deseq2_result_dir": deseq2_result_dir,
        "normalized_counts_table": normalized_counts_table,
        "normalized_counts_rds": normalized_counts_rds,
    }
    params = {
        "deseq_extra": deseq_extra,
        "schrink_extra": schrink_extra,
        "results_extra": results_extra,
        "contrast": contrast,
    }

    # Remove None values from inputs, outputs, and params
    outputs = {key: value for key, value in outputs.items() if value is not None}
    params = {key: value for key, value in params.items() if value is not None}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/deseq2/wald",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def wald(
    *,
    dds: str,
    wald_rds: Optional[str] = None,
    wald_tsv: Optional[str] = None,
    deseq2_result_dir: Optional[str] = None,
    normalized_counts_table: Optional[str] = None,
    normalized_counts_rds: Optional[str] = None,
    deseq_extra: Optional[str] = None,
    schrink_extra: Optional[str] = None,
    results_extra: Optional[str] = None,
    contrast: Optional[List[str]] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call differentially expressed genes with DESeq2.

    Args:
        dds: Path to RDS-formatted DESeq2-object.
        wald_rds (optional): Optional path to wald test results (RDS formatted).
        wald_tsv (optional): Optional path to wald test results (TSV formatted).
                             Requires the `contrast` parameter (see notes below).
        deseq2_result_dir (optional): Optional path to a directory containing
                                      all DESeq2 results (each file TSV formatted).
        normalized_counts_table (optional): Optional path to normalized counts (TSV formatted).
        normalized_counts_rds (optional): Optional path to normalized counts (RDS formatted).
        deseq_extra (optional): Additional parameters for the `DESeq()` function.
        schrink_extra (optional): Additional parameters for the `lfSchrink()` function.
        results_extra (optional): Additional parameters for the `result()` function.
        contrast (optional): List of characters specifying the comparison to extract.
                             Refer to documentation for `DESeq2` contrast parameter.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_wald(
        dds=dds,
        wald_rds=wald_rds,
        wald_tsv=wald_tsv,
        deseq2_result_dir=deseq2_result_dir,
        normalized_counts_table=normalized_counts_table,
        normalized_counts_rds=normalized_counts_rds,
        deseq_extra=deseq_extra,
        schrink_extra=schrink_extra,
        results_extra=results_extra,
        contrast=contrast,
         
    )
