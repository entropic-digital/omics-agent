from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_immunedeconv(
    *,
    expr: str,
    output: str,
    signature: Optional[str] = None,
    cibersort_bin: Optional[str] = None,
    cibersort_mat: Optional[str] = None,
    method: str = "deconvolute",
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Perform immune deconvolution from human or mouse gene expression using immunedeconv.

    Args:
        expr: Path to gene expression matrix (RDS, CSV, or TSV formatted).
        output: Path to deconvolution result (RDS, CSV, or TSV formatted).
        signature (optional): Path to custom cell-type signatures.
        cibersort_bin (optional): Path to CIBERSORT binary, required for CIBERSORT deconvolution.
        cibersort_mat (optional): Path to CIBERSORT signatures matrix, required for CIBERSORT deconvolution.
        method (optional): Immunedeconv method to use, default = "deconvolute".
        extra (optional): Optional parameters to provide to immunedeconv, besides `gene_expression_matrix` and `signature_matrix`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/immunedeconv",
        inputs=dict(
            expr=expr,
            signature=signature,
            cibersort_bin=cibersort_bin,
            cibersort_mat=cibersort_mat,
        ),
        outputs=dict(output=output),
        params={
            "method": method,
            "extra": extra,
        },
         
    )


@collect_tool()
def immunedeconv(
    *,
    expr: str,
    output: str,
    signature: Optional[str] = None,
    cibersort_bin: Optional[str] = None,
    cibersort_mat: Optional[str] = None,
    method: str = "deconvolute",
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Perform immune deconvolution from human or mouse gene expression using immunedeconv.

    Args:
        expr: Path to gene expression matrix (RDS, CSV, or TSV formatted).
        output: Path to deconvolution result (RDS, CSV, or TSV formatted).
        signature (optional): Path to custom cell-type signatures.
        cibersort_bin (optional): Path to CIBERSORT binary, required for CIBERSORT deconvolution.
        cibersort_mat (optional): Path to CIBERSORT signatures matrix, required for CIBERSORT deconvolution.
        method (optional): Immunedeconv method to use, default = "deconvolute".
        extra (optional): Optional parameters to provide to immunedeconv, besides `gene_expression_matrix` and `signature_matrix`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_immunedeconv(
        expr=expr,
        output=output,
        signature=signature,
        cibersort_bin=cibersort_bin,
        cibersort_mat=cibersort_mat,
        method=method,
        extra=extra,
         
    )
