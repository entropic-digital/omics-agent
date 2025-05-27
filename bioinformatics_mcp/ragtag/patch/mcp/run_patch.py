from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_patch(
    *,
    ref: str,
    query: str,
    fasta: str,
    agp: str,
    rename_agp: Optional[str] = None,
    rename_fasta: Optional[str] = None,
    comps_fasta: Optional[str] = None,
    ctg_agp: Optional[str] = None,
    ctg_fasta: Optional[str] = None,
    asm_dir: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Homology-based assembly patching using RagTag.

    Args:
        ref: Reference FASTA file (uncompressed or bgzipped).
        query: Query FASTA file (uncompressed or bgzipped).
        fasta: The final FASTA file containing the patched assembly output.
        agp: The final AGP file defining how the FASTA file is built.
        rename_agp (optional): An AGP file defining new names for query sequences.
        rename_fasta (optional): A FASTA file with renamed query sequences.
        comps_fasta (optional): A combined FASTA file of split target and renamed query assemblies.
        ctg_agp (optional): AGP file defining how the target assembly was split.
        ctg_fasta (optional): FASTA file of the target assembly split at gaps.
        asm_dir (optional): Directory for Assembly alignment files.
        extra (optional): Additional parameters for the tool.
            
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "ref": ref,
        "query": query,
    }
    outputs = {
        "fasta": fasta,
        "agp": agp,
        "rename_agp": rename_agp,
        "rename_fasta": rename_fasta,
        "comps_fasta": comps_fasta,
        "ctg_agp": ctg_agp,
        "ctg_fasta": ctg_fasta,
        "asm_dir": asm_dir,
    }
    params = {"extra": extra} if extra else {}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/ragtag/patch",
        inputs=inputs,
        outputs={k: v for k, v in outputs.items() if v is not None},
        params=params,
         
    )


@collect_tool()
def ragtag_patch(
    *,
    ref: str,
    query: str,
    fasta: str,
    agp: str,
    rename_agp: Optional[str] = None,
    rename_fasta: Optional[str] = None,
    comps_fasta: Optional[str] = None,
    ctg_agp: Optional[str] = None,
    ctg_fasta: Optional[str] = None,
    asm_dir: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Homology-based assembly patching using RagTag.

    Args:
        ref: Reference FASTA file (uncompressed or bgzipped).
        query: Query FASTA file (uncompressed or bgzipped).
        fasta: The final FASTA file containing the patched assembly output.
        agp: The final AGP file defining how the FASTA file is built.
        rename_agp (optional): An AGP file defining new names for query sequences.
        rename_fasta (optional): A FASTA file with renamed query sequences.
        comps_fasta (optional): A combined FASTA file of split target and renamed query assemblies.
        ctg_agp (optional): AGP file defining how the target assembly was split.
        ctg_fasta (optional): FASTA file of the target assembly split at gaps.
        asm_dir (optional): Directory for Assembly alignment files.
        extra (optional): Additional parameters for the tool.
            
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_patch(
        ref=ref,
        query=query,
        fasta=fasta,
        agp=agp,
        rename_agp=rename_agp,
        rename_fasta=rename_fasta,
        comps_fasta=comps_fasta,
        ctg_agp=ctg_agp,
        ctg_fasta=ctg_fasta,
        asm_dir=asm_dir,
        extra=extra,
         
    )
