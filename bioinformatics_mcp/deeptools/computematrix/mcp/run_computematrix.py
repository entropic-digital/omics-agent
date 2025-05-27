from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_computematrix(
    *,
    bed: str,
    bigwig: str,
    matrix_gz: Optional[str] = None,
    matrix_tab: Optional[str] = None,
    matrix_bed: Optional[str] = None,
    command: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the deepTools computeMatrix tool to calculate scores per genomic region.

    Args:
        bed: Path to BED or GTF file (.bed or .gtf) (required).
        bigwig: Path to bigWig files (.bw) (required).
        matrix_gz: Output gzipped matrix file (.gz) (optional).
        matrix_tab: Output tab-separated table of matrix file (.tab) (optional).
        matrix_bed: Output BED matrix file with sorted regions (.bed) (optional).
        command: ComputeMatrix mode, either `scale-regions` or `reference-point` (required).
        extra: Optional parameters passed to computeMatrix (optional).
 
    Returns:
        CompletedProcess: Subprocess executed with the results from computeMatrix.
    """
    outputs = {}
    if matrix_gz:
        outputs["matrix_gz"] = matrix_gz
    if matrix_tab:
        outputs["matrix_tab"] = matrix_tab
    if matrix_bed:
        outputs["matrix_bed"] = matrix_bed

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/deeptools/computematrix",
        inputs=dict(bed=bed, bigwig=bigwig),
        outputs=outputs,
        params={"command": command, "extra": extra} if extra else {"command": command},
         
    )


@collect_tool()
def computematrix(
    *,
    bed: str,
    bigwig: str,
    matrix_gz: Optional[str] = None,
    matrix_tab: Optional[str] = None,
    matrix_bed: Optional[str] = None,
    command: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Tool wrapper for deepTools computeMatrix to calculate scores per genomic region.

    Args:
        bed: Path to BED or GTF file (.bed or .gtf) (required).
        bigwig: Path to bigWig files (.bw) (required).
        matrix_gz: Output gzipped matrix file (.gz) (optional).
        matrix_tab: Output tab-separated table of matrix file (.tab) (optional).
        matrix_bed: Output BED matrix file with sorted regions (.bed) (optional).
        command: ComputeMatrix mode, either `scale-regions` or `reference-point` (required).
        extra: Optional parameters passed to computeMatrix (optional).
 
    Returns:
        CompletedProcess: Subprocess executed with the results from computeMatrix.
    """
    return run_computematrix(
        bed=bed,
        bigwig=bigwig,
        matrix_gz=matrix_gz,
        matrix_tab=matrix_tab,
        matrix_bed=matrix_bed,
        command=command,
        extra=extra,
         
    )
