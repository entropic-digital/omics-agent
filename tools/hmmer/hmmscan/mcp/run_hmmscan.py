from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_hmmscan(
    *,
    protein_sequence_file: str,
    database_hmm_files: str,
    output_matches: str,
     
) -> subprocess.CompletedProcess:
    """
    Search protein sequence(s) against a protein profile database.

    Args:
        protein_sequence_file: Path to the input protein sequence file (FASTA format).
        database_hmm_files: Path to the HMM database files to search against.
        output_matches: Path to save the matches to HMM files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/hmmer/hmmscan",
        inputs=dict(
            protein_sequence_file=protein_sequence_file,
            database_hmm_files=database_hmm_files,
        ),
        outputs=dict(output_matches=output_matches),
         
    )


@collect_tool()
def hmmscan(
    *,
    protein_sequence_file: str,
    database_hmm_files: str,
    output_matches: str,
     
) -> subprocess.CompletedProcess:
    """
    Search protein sequence(s) against a protein profile database.

    Args:
        protein_sequence_file: Path to the input protein sequence file (FASTA format).
        database_hmm_files: Path to the HMM database files to search against.
        output_matches: Path to save the matches to HMM files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_hmmscan(
        protein_sequence_file=protein_sequence_file,
        database_hmm_files=database_hmm_files,
        output_matches=output_matches,
         
    )
