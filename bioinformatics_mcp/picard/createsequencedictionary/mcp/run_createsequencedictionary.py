from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_createsequencedictionary(
    *,
    fasta_file: str,
    dict_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create a .dict file for a given FASTA file using picard CreateSequenceDictionary.

    Args:
        fasta_file: Path to the input FASTA file.
        dict_file: Path to the output .dict file.
        java_opts (optional): Additional options to be passed to the Java compiler (excluding -XmX and -Djava.io.tmpdir).
        extra (optional): Additional program arguments for CreateSequenceDictionary.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/picard/createsequencedictionary",
        inputs=dict(fasta=fasta_file),
        outputs=dict(dict=dict_file),
        params={"java_opts": java_opts, "extra": extra} if java_opts or extra else {},
         
    )


@collect_tool()
def createsequencedictionary(
    *,
    fasta_file: str,
    dict_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create a .dict file for a given FASTA file using picard CreateSequenceDictionary.

    Args:
        fasta_file: Path to the input FASTA file.
        dict_file: Path to the output .dict file.
        java_opts (optional): Additional options to be passed to the Java compiler (excluding -XmX and -Djava.io.tmpdir).
        extra (optional): Additional program arguments for CreateSequenceDictionary.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_createsequencedictionary(
        fasta_file=fasta_file,
        dict_file=dict_file,
        java_opts=java_opts,
        extra=extra,
         
    )
