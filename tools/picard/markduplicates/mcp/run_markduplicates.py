from typing import Optional, Union, List
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_markduplicates(
    *,
    input_files: Union[List[str], str],
    output_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
    embed_ref: Optional[bool] = False,
    withmatecigar: Optional[bool] = False,
     
) -> subprocess.CompletedProcess:
    """
    Mark PCR and optical duplicates with picard tools.

    Args:
        input_files: BAM/CRAM file(s) to process.
        output_file: BAM/CRAM file with marked duplicates.
        java_opts (optional): Additional arguments for the Java compiler.
        extra (optional): Additional program arguments for picard tools.
        embed_ref (optional): If True, embed the FASTA reference into the CRAM.
        withmatecigar (optional): If True, use MarkDuplicatesWithMateCigar instead.
  
    Returns:
        A CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/picard/markduplicates",
        inputs={"input_files": input_files},
        outputs={"output_file": output_file},
        params={
            "java_opts": java_opts,
            "extra": extra,
            "embed_ref": embed_ref,
            "withmatecigar": withmatecigar,
        },
         
    )


@collect_tool()
def markduplicates(
    *,
    input_files: Union[List[str], str],
    output_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
    embed_ref: Optional[bool] = False,
    withmatecigar: Optional[bool] = False,
     
) -> subprocess.CompletedProcess:
    """
    Mark PCR and optical duplicates with picard tools.

    Args:
        input_files: BAM/CRAM file(s) to process.
        output_file: BAM/CRAM file with marked duplicates.
        java_opts (optional): Additional arguments for the Java compiler.
        extra (optional): Additional program arguments for picard tools.
        embed_ref (optional): If True, embed the FASTA reference into the CRAM.
        withmatecigar (optional): If True, use MarkDuplicatesWithMateCigar instead.
  
    Returns:
        A CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_markduplicates(
        input_files=input_files,
        output_file=output_file,
        java_opts=java_opts,
        extra=extra,
        embed_ref=embed_ref,
        withmatecigar=withmatecigar,
         
    )
