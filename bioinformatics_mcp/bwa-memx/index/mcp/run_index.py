from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    fasta_file: str,
    output_prefix: str,
    bwa: str,
    num_models: Optional[int] = 268435456,
     
) -> subprocess.CompletedProcess:
    """
    Creates a BWA index.

    Args:
        fasta_file: Path to the input FASTA file.
        output_prefix: Prefix for the BWA index files, which may include an output directory.
        bwa: Type of BWA index to build ("bwa-mem", "bwa-mem2", or "bwa-meme").
        num_models (optional): For BWA-MEME, the number of models for the P-RMI training step (default: 268435456).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bwa-memx/index",
        inputs=dict(fasta_file=fasta_file),
        outputs=dict(output_prefix=output_prefix),
        params={"bwa": bwa, "num_models": num_models}
        if bwa == "bwa-meme"
        else {"bwa": bwa},
         
    )


@collect_tool()
def index_bwa_memx(
    *,
    fasta_file: str,
    output_prefix: str,
    bwa: str,
    num_models: Optional[int] = 268435456,
     
) -> subprocess.CompletedProcess:
    """
    Creates a BWA index for bwa-mem, bwa-mem2, or bwa-meme.

    Args:
        fasta_file: Path to the input FASTA file.
        output_prefix: Prefix for the BWA index files, which may include an output directory.
        bwa: Type of BWA index to build ("bwa-mem", "bwa-mem2", or "bwa-meme").
        num_models (optional): For BWA-MEME, the number of models for the P-RMI training step (default: 268435456).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(
        fasta_file=fasta_file,
        output_prefix=output_prefix,
        bwa=bwa,
        num_models=num_models,
         
    )
