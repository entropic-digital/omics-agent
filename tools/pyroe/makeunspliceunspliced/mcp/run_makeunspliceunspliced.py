from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_makeunspliceunspliced(
    *,
    gtf: str,
    fasta: str,
    spliced: Optional[str] = None,
    unspliced: Optional[str] = None,
    output_fasta: str,
    gene_id_to_name: str,
    t2g_3col: str,
    t2g: str,
    g2g: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Build spliceu reference files for Alevin-fry. The spliceu (the spliced + unspliced)
    transcriptome reference, where the unspliced transcripts of each gene represent the
    entire genomic interval of that gene.

    Args:
        gtf: Path to the genome annotation (GTF formatted)
        fasta: Path to the genome sequence (Fasta formatted)
        spliced (optional): Optional path to additional spliced sequences (Fasta formatted)
        unspliced (optional): Optional path to unspliced sequences (Fasta formatted)
        output_fasta: Path to spliced+unspliced sequences (Fasta formatted)
        gene_id_to_name: Path to a TSV formatted text file containing gene_id <-> gene_name correspondence
        t2g_3col: Path to a TSV formatted text file containing the transcript_id <-> gene_name <-> splicing status correspondence
        t2g: Path to a TSV formatted text file containing the transcript_id <-> gene_name
        g2g: Path to a TSV formatted text file containing the gene_id <-> gene_name
        extra (optional): Optional parameters to be passed to pyroe
           
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process
    """
    return run_snake_wrapper(
        wrapper="file:tools/pyroe/makeunspliceunspliced",
        inputs=dict(gtf=gtf, fasta=fasta, spliced=spliced, unspliced=unspliced),
        outputs=dict(
            fasta=output_fasta,
            gene_id_to_name=gene_id_to_name,
            t2g_3col=t2g_3col,
            t2g=t2g,
            g2g=g2g,
        ),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def makeunspliceunspliced(
    *,
    gtf: str,
    fasta: str,
    spliced: Optional[str] = None,
    unspliced: Optional[str] = None,
    output_fasta: str,
    gene_id_to_name: str,
    t2g_3col: str,
    t2g: str,
    g2g: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Build spliceu reference files for Alevin-fry. The spliceu (the spliced + unspliced)
    transcriptome reference, where the unspliced transcripts of each gene represent the
    entire genomic interval of that gene.

    Args:
        gtf: Path to the genome annotation (GTF formatted)
        fasta: Path to the genome sequence (Fasta formatted)
        spliced (optional): Optional path to additional spliced sequences (Fasta formatted)
        unspliced (optional): Optional path to unspliced sequences (Fasta formatted)
        output_fasta: Path to spliced+unspliced sequences (Fasta formatted)
        gene_id_to_name: Path to a TSV formatted text file containing gene_id <-> gene_name correspondence
        t2g_3col: Path to a TSV formatted text file containing the transcript_id <-> gene_name <-> splicing status correspondence
        t2g: Path to a TSV formatted text file containing the transcript_id <-> gene_name
        g2g: Path to a TSV formatted text file containing the gene_id <-> gene_name
        extra (optional): Optional parameters to be passed to pyroe
           
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process
    """
    return run_makeunspliceunspliced(
        gtf=gtf,
        fasta=fasta,
        spliced=spliced,
        unspliced=unspliced,
        output_fasta=output_fasta,
        gene_id_to_name=gene_id_to_name,
        t2g_3col=t2g_3col,
        t2g=t2g,
        g2g=g2g,
        extra=extra,
         
    )
