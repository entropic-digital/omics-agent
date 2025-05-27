from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_fasterq_dump(
    *,
    sra_accession: str,
    output_dir: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Download FASTQ files from SRA using fasterq-dump.

    Args:
        sra_accession: The accession ID of the SRA dataset.
        output_dir (optional): The directory to store the output FASTQ files. Defaults to current directory.
        extra (optional): Additional arguments to pass to fasterq-dump.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/sra-tools/fasterq-dump",
        inputs=dict(sra_accession=sra_accession),
        outputs=dict(output_dir=output_dir or "."),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def fasterq_dump(
    *,
    sra_accession: str,
    output_dir: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Download FASTQ files from SRA using fasterq-dump.

    Args:
        sra_accession: The accession ID of the SRA dataset.
        output_dir (optional): The directory to store the output FASTQ files. Defaults to current directory.
        extra (optional): Additional arguments to pass to fasterq-dump.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_fasterq_dump(
        sra_accession=sra_accession, output_dir=output_dir, extra=extra,      
    )
