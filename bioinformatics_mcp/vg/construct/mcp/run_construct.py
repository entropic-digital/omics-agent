from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_construct(
    *,
    reference: str,
    variant_calls: str,
    output_graph: str,
    region: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Construct variation graphs from a reference and variant calls.

    Args:
        reference: Path to the reference genome in FASTA format.
        variant_calls: Path to the variant calls in VCF format.
        output_graph: Path to output the constructed variation graph.
        region (optional): Genomic region to restrict the graph construction.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/vg/construct",
        inputs=dict(reference=reference, variant_calls=variant_calls),
        outputs=dict(output_graph=output_graph),
        params={"region": region} if region else {},
         
    )


@collect_tool()
def construct(
    *,
    reference: str,
    variant_calls: str,
    output_graph: str,
    region: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Construct variation graphs from a reference and variant calls.

    Args:
        reference: Path to the reference genome in FASTA format.
        variant_calls: Path to the variant calls in VCF format.
        output_graph: Path to output the constructed variation graph.
        region (optional): Genomic region to restrict the graph construction.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_construct(
        reference=reference,
        variant_calls=variant_calls,
        output_graph=output_graph,
        region=region,
         
    )
