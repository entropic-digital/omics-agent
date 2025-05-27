from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_abundance(
    *,
    reads: str,
    db: Optional[str] = None,
    abundances: str,
    alignments: Optional[str] = None,
    unclassified: Optional[str] = None,
    unmapped: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate relative abundance estimates from ONT, PacBio, or short 16S reads using emu.

    Args:
        reads: Single FASTA file or paired FASTQ files (required).
        db (optional): Emu database. If not provided, see emu's documentation for how to build one.
        abundances: Output TSV file for relative (and optionally, absolute) abundances.
        alignments (optional): Output SAM file containing the alignments.
        unclassified (optional): Output FASTA/Q file with unclassified sequences.
        unmapped (optional): Output FASTA/Q file with unmapped sequences.
        extra (optional): Additional parameters such as '--type' (sequencer) or '--min-abundance'.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    outputs = {"abundances": abundances}
    if alignments:
        outputs["alignments"] = alignments
    if unclassified:
        outputs["unclassified"] = unclassified
    if unmapped:
        outputs["unmapped"] = unmapped

    params = {"db": db} if db else {}
    if extra:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/emu/abundance",
        inputs={"reads": reads},
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def abundance(
    *,
    reads: str,
    db: Optional[str] = None,
    abundances: str,
    alignments: Optional[str] = None,
    unclassified: Optional[str] = None,
    unmapped: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate relative abundance estimates from ONT, PacBio, or short 16S reads using emu.

    Args:
        reads: Single FASTA file or paired FASTQ files (required).
        db (optional): Emu database. If not provided, see emu's documentation for how to build one.
        abundances: Output TSV file for relative (and optionally, absolute) abundances.
        alignments (optional): Output SAM file containing the alignments.
        unclassified (optional): Output FASTA/Q file with unclassified sequences.
        unmapped (optional): Output FASTA/Q file with unmapped sequences.
        extra (optional): Additional parameters such as '--type' (sequencer) or '--min-abundance'.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_abundance(
        reads=reads,
        db=db,
        abundances=abundances,
        alignments=alignments,
        unclassified=unclassified,
        unmapped=unmapped,
        extra=extra,
         
    )
