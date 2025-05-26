from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_callcopyratiosegments(
    *,
    copy_ratio_seg: str,
    copy_ratio_seg_out: str,
    igv_seg: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calls copy-ratio segments as amplified, deleted, or copy-number neutral using GATK's CallCopyRatioSegments tool.

    Args:
        copy_ratio_seg: Input cr.seq file from ModelSegments.
        copy_ratio_seg_out: Output file for called copy ratio segments.
        igv_seg (optional): CBS formatted igv.seg output file (optional).
        java_opts (optional): Additional arguments for the Java Virtual Machine, excluding memory and temp directory options.
        extra (optional): Additional program arguments for GATK CallCopyRatioSegments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk/callcopyratiosegments",
        inputs=dict(copy_ratio_seg=copy_ratio_seg),
        outputs=dict(
            copy_ratio_seg=copy_ratio_seg_out,
            igv_seg=igv_seg,
        ),
        params={
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def callcopyratiosegments(
    *,
    copy_ratio_seg: str,
    copy_ratio_seg_out: str,
    igv_seg: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calls copy-ratio segments as amplified, deleted, or copy-number neutral using GATK's CallCopyRatioSegments tool.

    Args:
        copy_ratio_seg: Input cr.seq file from ModelSegments.
        copy_ratio_seg_out: Output file for called copy ratio segments.
        igv_seg (optional): CBS formatted igv.seg output file, if required.
        java_opts (optional): Additional arguments for the Java Virtual Machine, excluding memory and temp directory options.
        extra (optional): Additional program arguments for GATK CallCopyRatioSegments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_callcopyratiosegments(
        copy_ratio_seg=copy_ratio_seg,
        copy_ratio_seg_out=copy_ratio_seg_out,
        igv_seg=igv_seg,
        java_opts=java_opts,
        extra=extra,
         
    )
