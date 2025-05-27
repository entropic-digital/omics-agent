from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_quast(
    *,
    sequences: str,
    assessment_summary: str,
    tab_summary: str,
    latex_summary: str,
    icarus_menu: str,
    pdf_report: str,
    html_report: str,
    misassemblies_report: str,
    unaligned_contigs_report: str,
    kmer_metrics_report: str,
    mapped_reads_stats_report: str,
    reference_genome: Optional[str] = None,
    gff: Optional[str] = None,
    paired_end_read: Optional[str] = None,
    mate_pair_reads: Optional[str] = None,
    unpaired_reads: Optional[str] = None,
    pacbio_smrt_reads: Optional[str] = None,
    nanopore_reads: Optional[str] = None,
    mapped_reads_against_ref: Optional[str] = None,
    mapped_reads_assemblies: Optional[str] = None,
    structural_variants: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Quality Assessment Tool for Genome Assemblies.

    Args:
        sequences: Sequences in FASTA format.
        assessment_summary: Path to save the assessment summary in plain text format.
        tab_summary: Path to save the tab-separated version of the summary.
        latex_summary: Path to save the LaTeX version of the summary.
        icarus_menu: Path to save the Icarus main menu with links to interactive viewers.
        pdf_report: Path to save the PDF report of all plots combined with all tables.
        html_report: Path to save the HTML version of the report with interactive plots inside.
        misassemblies_report: Path to save the report on misassemblies.
        unaligned_contigs_report: Path to save the report on unaligned and partially unaligned contigs.
        kmer_metrics_report: Path to save the report on k-mer-based metrics.
        mapped_reads_stats_report: Path to save the report on mapped reads statistics.
        reference_genome (optional): Reference genome.
        gff (optional): GFF file.
        paired_end_read (optional): Paired-end reads.
        mate_pair_reads (optional): Mate-pair reads.
        unpaired_reads (optional): Unpaired reads.
        pacbio_smrt_reads (optional): PacBio SMRT reads.
        nanopore_reads (optional): Oxford Nanopore reads.
        mapped_reads_against_ref (optional): Mapped reads against the reference in SAM/BAM format.
        mapped_reads_assemblies (optional): Mapped reads against each of the assemblies in SAM/BAM format (same order).
        structural_variants (optional): Structural variants in BEDPE format.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = dict(
        sequences=sequences,
        reference_genome=reference_genome,
        gff=gff,
        paired_end_read=paired_end_read,
        mate_pair_reads=mate_pair_reads,
        unpaired_reads=unpaired_reads,
        pacbio_smrt_reads=pacbio_smrt_reads,
        nanopore_reads=nanopore_reads,
        mapped_reads_against_ref=mapped_reads_against_ref,
        mapped_reads_assemblies=mapped_reads_assemblies,
        structural_variants=structural_variants,
    )
    outputs = dict(
        assessment_summary=assessment_summary,
        tab_summary=tab_summary,
        latex_summary=latex_summary,
        icarus_menu=icarus_menu,
        pdf_report=pdf_report,
        html_report=html_report,
        misassemblies_report=misassemblies_report,
        unaligned_contigs_report=unaligned_contigs_report,
        kmer_metrics_report=kmer_metrics_report,
        mapped_reads_stats_report=mapped_reads_stats_report,
    )
    params = {"extra": extra} if extra else {}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/quast",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def quast(
    *,
    sequences: str,
    assessment_summary: str,
    tab_summary: str,
    latex_summary: str,
    icarus_menu: str,
    pdf_report: str,
    html_report: str,
    misassemblies_report: str,
    unaligned_contigs_report: str,
    kmer_metrics_report: str,
    mapped_reads_stats_report: str,
    reference_genome: Optional[str] = None,
    gff: Optional[str] = None,
    paired_end_read: Optional[str] = None,
    mate_pair_reads: Optional[str] = None,
    unpaired_reads: Optional[str] = None,
    pacbio_smrt_reads: Optional[str] = None,
    nanopore_reads: Optional[str] = None,
    mapped_reads_against_ref: Optional[str] = None,
    mapped_reads_assemblies: Optional[str] = None,
    structural_variants: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Quality Assessment Tool for Genome Assemblies.

    Args:
        sequences: Sequences in FASTA format.
        assessment_summary: Path to save the assessment summary in plain text format.
        tab_summary: Path to save the tab-separated version of the summary.
        latex_summary: Path to save the LaTeX version of the summary.
        icarus_menu: Path to save the Icarus main menu with links to interactive viewers.
        pdf_report: Path to save the PDF report of all plots combined with all tables.
        html_report: Path to save the HTML version of the report with interactive plots inside.
        misassemblies_report: Path to save the report on misassemblies.
        unaligned_contigs_report: Path to save the report on unaligned and partially unaligned contigs.
        kmer_metrics_report: Path to save the report on k-mer-based metrics.
        mapped_reads_stats_report: Path to save the report on mapped reads statistics.
        reference_genome (optional): Reference genome.
        gff (optional): GFF file.
        paired_end_read (optional): Paired-end reads.
        mate_pair_reads (optional): Mate-pair reads.
        unpaired_reads (optional): Unpaired reads.
        pacbio_smrt_reads (optional): PacBio SMRT reads.
        nanopore_reads (optional): Oxford Nanopore reads.
        mapped_reads_against_ref (optional): Mapped reads against the reference in SAM/BAM format.
        mapped_reads_assemblies (optional): Mapped reads against each of the assemblies in SAM/BAM format (same order).
        structural_variants (optional): Structural variants in BEDPE format.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_quast(
        sequences=sequences,
        assessment_summary=assessment_summary,
        tab_summary=tab_summary,
        latex_summary=latex_summary,
        icarus_menu=icarus_menu,
        pdf_report=pdf_report,
        html_report=html_report,
        misassemblies_report=misassemblies_report,
        unaligned_contigs_report=unaligned_contigs_report,
        kmer_metrics_report=kmer_metrics_report,
        mapped_reads_stats_report=mapped_reads_stats_report,
        reference_genome=reference_genome,
        gff=gff,
        paired_end_read=paired_end_read,
        mate_pair_reads=mate_pair_reads,
        unpaired_reads=unpaired_reads,
        pacbio_smrt_reads=pacbio_smrt_reads,
        nanopore_reads=nanopore_reads,
        mapped_reads_against_ref=mapped_reads_against_ref,
        mapped_reads_assemblies=mapped_reads_assemblies,
        structural_variants=structural_variants,
        extra=extra,
         
    )
