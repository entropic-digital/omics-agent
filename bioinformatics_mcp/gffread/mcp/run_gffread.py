from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_gffread(
    *,
    fasta: str,
    annotation: str,
    ids: Optional[str] = None,
    nids: Optional[str] = None,
    seq_info: Optional[str] = None,
    sort_by: Optional[str] = None,
    attr: Optional[str] = None,
    chr_replace: Optional[str] = None,
    records: Optional[str] = None,
    transcript_fasta: Optional[str] = None,
    cds_fasta: Optional[str] = None,
    protein_fasta: Optional[str] = None,
    dupinfo: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Validate, filter, convert and perform various operations on GFF/GTF files with Gffread.

    Args:
        fasta: Path to the FASTA genome file.
        annotation: Path to the GTF/GFF/BED genome annotation file.
        ids (optional): Path to a file containing records/transcripts to keep.
        nids (optional): Path to a file containing records/transcripts to discard.
        seq_info (optional): Path to a sequence information TSV file.
        sort_by (optional): Path to a file containing the ordered list of reference sequences.
        attr (optional): Path to a file containing annotation attributes to keep.
        chr_replace (optional): Path to a TSV file for chromosome/reference ID replacement.
        records (optional): Path to an output file for genome annotation.
        transcript_fasta (optional): Path to an output FASTA file for `-w` transcript sequences.
        cds_fasta (optional): Path to an output FASTA file for `-x` CDS sequences.
        protein_fasta (optional): Path to an output FASTA file for `-y` protein sequences.
        dupinfo (optional): Path to an output file for clustering/merging information.
        extra (optional): Additional arguments to pass to Gffread, excluding restricted options.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "fasta": fasta,
        "annotation": annotation,
        "ids": ids,
        "nids": nids,
        "seq_info": seq_info,
        "sort_by": sort_by,
        "attr": attr,
        "chr_replace": chr_replace,
    }
    outputs = {
        "records": records,
        "transcript_fasta": transcript_fasta,
        "cds_fasta": cds_fasta,
        "protein_fasta": protein_fasta,
        "dupinfo": dupinfo,
    }
    params = {"extra": extra} if extra else {}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gffread",
        inputs={k: v for k, v in inputs.items() if v is not None},
        outputs={k: v for k, v in outputs.items() if v is not None},
        params=params,
         
    )


@collect_tool()
def gffread(
    *,
    fasta: str,
    annotation: str,
    ids: Optional[str] = None,
    nids: Optional[str] = None,
    seq_info: Optional[str] = None,
    sort_by: Optional[str] = None,
    attr: Optional[str] = None,
    chr_replace: Optional[str] = None,
    records: Optional[str] = None,
    transcript_fasta: Optional[str] = None,
    cds_fasta: Optional[str] = None,
    protein_fasta: Optional[str] = None,
    dupinfo: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Validate, filter, convert and perform various operations on GFF/GTF files with Gffread.

    Args:
        fasta: Path to the FASTA genome file.
        annotation: Path to the GTF/GFF/BED genome annotation file.
        ids (optional): Path to a file containing records/transcripts to keep.
        nids (optional): Path to a file containing records/transcripts to discard.
        seq_info (optional): Path to a sequence information TSV file.
        sort_by (optional): Path to a file containing the ordered list of reference sequences.
        attr (optional): Path to a file containing annotation attributes to keep.
        chr_replace (optional): Path to a TSV file for chromosome/reference ID replacement.
        records (optional): Path to an output file for genome annotation.
        transcript_fasta (optional): Path to an output FASTA file for `-w` transcript sequences.
        cds_fasta (optional): Path to an output FASTA file for `-x` CDS sequences.
        protein_fasta (optional): Path to an output FASTA file for `-y` protein sequences.
        dupinfo (optional): Path to an output file for clustering/merging information.
        extra (optional): Additional arguments to pass to Gffread, excluding restricted options.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_gffread(
        fasta=fasta,
        annotation=annotation,
        ids=ids,
        nids=nids,
        seq_info=seq_info,
        sort_by=sort_by,
        attr=attr,
        chr_replace=chr_replace,
        records=records,
        transcript_fasta=transcript_fasta,
        cds_fasta=cds_fasta,
        protein_fasta=protein_fasta,
        dupinfo=dupinfo,
        extra=extra,
         
    )
