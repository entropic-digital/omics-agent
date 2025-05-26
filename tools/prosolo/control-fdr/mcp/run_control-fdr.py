from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_control_fdr(
    *,
    input_vcf: str,
    output_bcf: str,
    event_specification: Optional[str] = None,
    fdr_threshold: Optional[float] = None,
     
) -> subprocess.CompletedProcess:
    """
    ProSolo FDR control.

    ProSolo can control the false discovery rate of any combination of its defined single cell events,
    such as the presence of an alternative allele or the dropout of an allele.

    Args:
        input_vcf: Variants called with ProSolo in VCF or BCF format, including the fine-grained
            posterior probabilities for single cell events.
        output_bcf: Output BCF file with all variants that satisfy the chosen false discovery rate
            threshold with regard to the specified events.
        event_specification (optional): Specification of events to control FDR for.
        fdr_threshold (optional): The false discovery rate threshold to apply.
         
    Returns:
        A CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {}
    if event_specification:
        params["event_specification"] = event_specification
    if fdr_threshold:
        params["fdr_threshold"] = fdr_threshold

    return run_snake_wrapper(
        wrapper="file:tools/prosolo/control-fdr",
        inputs=dict(input_vcf=input_vcf),
        outputs=dict(output_bcf=output_bcf),
        params=params,
         
    )


@collect_tool()
def control_fdr(
    *,
    input_vcf: str,
    output_bcf: str,
    event_specification: Optional[str] = None,
    fdr_threshold: Optional[float] = None,
     
) -> subprocess.CompletedProcess:
    """
    ProSolo FDR control.

    ProSolo can control the false discovery rate of any combination of its defined single cell events,
    such as the presence of an alternative allele or the dropout of an allele.

    Args:
        input_vcf: Variants called with ProSolo in VCF or BCF format, including the fine-grained
            posterior probabilities for single cell events.
        output_bcf: Output BCF file with all variants that satisfy the chosen false discovery rate
            threshold with regard to the specified events.
        event_specification (optional): Specification of events to control FDR for.
        fdr_threshold (optional): The false discovery rate threshold to apply.
         
    Returns:
        A CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_control_fdr(
        input_vcf=input_vcf,
        output_bcf=output_bcf,
        event_specification=event_specification,
        fdr_threshold=fdr_threshold,
         
    )
