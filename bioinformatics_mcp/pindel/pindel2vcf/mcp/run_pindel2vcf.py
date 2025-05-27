from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_pindel2vcf(
    *,
    pindel_output: str,
    reference: str,
    vcf_output: str,
    reference_index: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert pindel output to vcf.

    Args:
        pindel_output: Path to the pindel output file.
        reference: Path to the reference genome file.
        vcf_output: Path to the output VCF file.
        reference_index (optional): Path to the reference index file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/pindel/pindel2vcf",
        inputs=dict(pindel_output=pindel_output, reference=reference),
        outputs=dict(vcf_output=vcf_output),
        params={"reference_index": reference_index} if reference_index else {},
         
    )


@collect_tool()
def pindel2vcf(
    *,
    pindel_output: str,
    reference: str,
    vcf_output: str,
    reference_index: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert pindel output to vcf.

    Args:
        pindel_output: Path to the pindel output file.
        reference: Path to the reference genome file.
        vcf_output: Path to the output VCF file.
        reference_index (optional): Path to the reference index file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_pindel2vcf(
        pindel_output=pindel_output,
        reference=reference,
        vcf_output=vcf_output,
        reference_index=reference_index,
         
    )
