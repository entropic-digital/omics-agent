from typing import List, Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_featurecounts(
    *,
    sam_or_bam_files: List[str],
    annotation_file: str,
    output_counts_file: str,
    output_summary_file: str,
    output_junction_file: Optional[str] = None,
    sorting_order_file: Optional[str] = None,
    fasta_index_file: Optional[str] = None,
    strand: int = 0,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    FeatureCounts assign mapped reads or fragments (paired-end data) to genomic features such as genes, exons, and promoters.

    Args:
        sam_or_bam_files: A list of SAM or BAM files to be processed.
        annotation_file: A GTF, GFF, or SAF annotation file.
        output_counts_file: Path to store the feature counts file (tab-separated).
        output_summary_file: Path to store the summary file (tab-separated).
        output_junction_file (optional): Path to store the junction counts file (tab-separated).
        sorting_order_file (optional): A tab-separated file for sorting order with chromosome names in the first column.
        fasta_index_file (optional): A FASTA index file.
        strand: The strandness of the library (0: unstranded, 1: stranded, 2: reversely stranded).
        extra (optional): Additional program arguments for FeatureCounts.
  
    Returns:
        CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    inputs = {
        "sam_or_bam_files": sam_or_bam_files,
        "annotation_file": annotation_file,
        "sorting_order_file": sorting_order_file,
        "fasta_index_file": fasta_index_file,
    }

    outputs = {
        "output_counts_file": output_counts_file,
        "output_summary_file": output_summary_file,
        "output_junction_file": output_junction_file,
    }

    params = {
        "strand": strand,
        "extra": extra,
    }

    # Clean dictionary to remove None values
    inputs = {k: v for k, v in inputs.items() if v is not None}
    outputs = {k: v for k, v in outputs.items() if v is not None}
    params = {k: v for k, v in params.items() if v is not None}

    return run_snake_wrapper(
        wrapper="file:tools/subread/featurecounts",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def featurecounts(
    *,
    sam_or_bam_files: List[str],
    annotation_file: str,
    output_counts_file: str,
    output_summary_file: str,
    output_junction_file: Optional[str] = None,
    sorting_order_file: Optional[str] = None,
    fasta_index_file: Optional[str] = None,
    strand: int = 0,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    FeatureCounts assign mapped reads or fragments (paired-end data) to genomic features such as genes, exons, and promoters.

    Args:
        sam_or_bam_files: A list of SAM or BAM files to be processed.
        annotation_file: A GTF, GFF, or SAF annotation file.
        output_counts_file: Path to store the feature counts file (tab-separated).
        output_summary_file: Path to store the summary file (tab-separated).
        output_junction_file (optional): Path to store the junction counts file (tab-separated).
        sorting_order_file (optional): A tab-separated file for sorting order with chromosome names in the first column.
        fasta_index_file (optional): A FASTA index file.
        strand: The strandness of the library (0: unstranded, 1: stranded, 2: reversely stranded).
        extra (optional): Additional program arguments for FeatureCounts.
  
    Returns:
        CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_featurecounts(
        sam_or_bam_files=sam_or_bam_files,
        annotation_file=annotation_file,
        output_counts_file=output_counts_file,
        output_summary_file=output_summary_file,
        output_junction_file=output_junction_file,
        sorting_order_file=sorting_order_file,
        fasta_index_file=fasta_index_file,
        strand=strand,
        extra=extra,
         
    )
