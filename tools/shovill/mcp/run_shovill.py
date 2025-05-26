from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_shovill(
    *,
    input_reads: str,
    output_dir: str,
    assembler: Optional[str] = None,
    min_length: Optional[int] = None,
    cpus: int = 1,
     
) -> subprocess.CompletedProcess:
    """
    Assemble bacterial isolate genomes from Illumina paired-end reads.

    Args:
        input_reads: Path to the paired-end reads in FASTQ format.
        output_dir: Path to the output directory for assembly results.
        assembler (optional): Assembly tool to use (e.g., SPAdes, SKESA). Default is Shovill's default.
        min_length (optional): Minimum contig length to report in the assembly. Default is tool's default.
        cpus: Number of CPU threads to use. Default is 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/shovill",
        inputs=dict(input_reads=input_reads),
        outputs=dict(output_dir=output_dir),
        params={
            "assembler": assembler,
            "min_length": min_length,
            "cpus": cpus,
        },
         
    )


@collect_tool()
def shovill(
    *,
    input_reads: str,
    output_dir: str,
    assembler: Optional[str] = None,
    min_length: Optional[int] = None,
    cpus: int = 1,
     
) -> subprocess.CompletedProcess:
    """
    Assemble bacterial isolate genomes from Illumina paired-end reads.

    Args:
        input_reads: Path to the paired-end reads in FASTQ format.
        output_dir: Path to the output directory for assembly results.
        assembler (optional): Assembly tool to use (e.g., SPAdes, SKESA). Default is Shovill's default.
        min_length (optional): Minimum contig length to report in the assembly. Default is tool's default.
        cpus: Number of CPU threads to use. Default is 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_shovill(
        input_reads=input_reads,
        output_dir=output_dir,
        assembler=assembler,
        min_length=min_length,
        cpus=cpus,
         
    )
