from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_bamtag(
    *,
    input_bam: str,
    output_bam: str,
    umi_tag: str,
    cell_tag: str,
    umi_sep: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert a BAM/SAM with fastqtransformed read names to have UMI and cell tags.

    Args:
        input_bam: Path to the input BAM file.
        output_bam: Path to the output BAM file.
        umi_tag: The tag to use for UMIs in the output BAM file.
        cell_tag: The tag to use for cell barcodes in the output BAM file.
        umi_sep (optional): Separator used to split UMI and cell in read names.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/umis/bamtag",
        inputs=dict(input_bam=input_bam),
        outputs=dict(output_bam=output_bam),
        params={
            "umi_tag": umi_tag,
            "cell_tag": cell_tag,
            "umi_sep": umi_sep,
        },
         
    )


@collect_tool()
def bamtag(
    *,
    input_bam: str,
    output_bam: str,
    umi_tag: str,
    cell_tag: str,
    umi_sep: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert a BAM/SAM with fastqtransformed read names to have UMI and cell tags.

    Args:
        input_bam: Path to the input BAM file.
        output_bam: Path to the output BAM file.
        umi_tag: The tag to use for UMIs in the output BAM file.
        cell_tag: The tag to use for cell barcodes in the output BAM file.
        umi_sep (optional): Separator used to split UMI and cell in read names.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bamtag(
        input_bam=input_bam,
        output_bam=output_bam,
        umi_tag=umi_tag,
        cell_tag=cell_tag,
        umi_sep=umi_sep,
         
    )
