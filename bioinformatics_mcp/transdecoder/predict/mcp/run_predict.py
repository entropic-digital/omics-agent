from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_predict(
    *,
    fasta_assembly: str,
    candidate_coding_regions: str,
     
) -> subprocess.CompletedProcess:
    """
    Predict the likely coding regions from the ORFs identified by Transdecoder.LongOrfs.

    Args:
        fasta_assembly: Path to the input FASTA assembly file.
        candidate_coding_regions: Path to the output directory (pep, cds, gff3, bed formats will be generated).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/transdecoder/predict",
        inputs={"fasta_assembly": fasta_assembly},
        outputs={"candidate_coding_regions": candidate_coding_regions},
         
    )


@collect_tool()
def predict(
    *,
    fasta_assembly: str,
    candidate_coding_regions: str,
     
) -> subprocess.CompletedProcess:
    """
    Predict the likely coding regions from the ORFs identified by Transdecoder.LongOrfs.

    Args:
        fasta_assembly: Path to the input FASTA assembly file.
        candidate_coding_regions: Path to the output directory (pep, cds, gff3, bed formats will be generated).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_predict(
        fasta_assembly=fasta_assembly,
        candidate_coding_regions=candidate_coding_regions,
         
    )
