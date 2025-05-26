from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_longorfs(
    *,
    transcripts: str,
    orfs_peptide_files: str,
    min_length: Optional[int] = 100,
     
) -> subprocess.CompletedProcess:
    """
    TransDecoder.LongOrfs will identify coding regions within transcript sequences (ORFs) that are at least
    100 amino acids long. You can lower this via the '-m' parameter, but know that the rate of false positive
    ORF predictions increases drastically with shorter minimum length criteria.

    Args:
        transcripts: Path to the input FASTA file containing transcript sequences.
        orfs_peptide_files: Path for the output ORFs peptide file(s).
        min_length (optional): Minimum ORF length in amino acids. Default is 100.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/transdecoder/longorfs",
        inputs=dict(transcripts=transcripts),
        outputs=dict(orfs_peptide_files=orfs_peptide_files),
        params={"min_length": min_length} if min_length else {},
         
    )


@collect_tool()
def longorfs(
    *,
    transcripts: str,
    orfs_peptide_files: str,
    min_length: Optional[int] = 100,
     
) -> subprocess.CompletedProcess:
    """
    TransDecoder.LongOrfs will identify coding regions within transcript sequences (ORFs) that are at least
    100 amino acids long. You can lower this via the '-m' parameter, but know that the rate of false positive
    ORF predictions increases drastically with shorter minimum length criteria.

    Args:
        transcripts: Path to the input FASTA file containing transcript sequences.
        orfs_peptide_files: Path for the output ORFs peptide file(s).
        min_length (optional): Minimum ORF length in amino acids. Default is 100.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_longorfs(
        transcripts=transcripts,
        orfs_peptide_files=orfs_peptide_files,
        min_length=min_length,
         
    )
