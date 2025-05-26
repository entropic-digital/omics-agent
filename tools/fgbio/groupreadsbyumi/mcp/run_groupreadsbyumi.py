from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_groupreadsbyumi(
    *,
    input_bam: str,
    output_bam: str,
    umi_tag: str,
    strategy: str,
    family_size_threshold: Optional[int] = None,
    min_map_qual: Optional[int] = 0,
    annotate_family_size: Optional[bool] = False,
    allow_missing_umis: Optional[bool] = False,
    raw_tag: Optional[str] = None,
    output_stats: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Groups reads together that appear to have come from the same original molecule.

    Args:
        input_bam: Path to the input BAM file.
        output_bam: Path to the output BAM file containing grouped reads.
        umi_tag: The tag used in the input BAM to encode UMI sequences.
        strategy: The method used to group reads by UMI (e.g., "adjacency", "edit", etc.).
        family_size_threshold (optional): Minimum family size to output reads (default is None).
        min_map_qual (optional): Minimum mapping quality of reads considered (default is 0).
        annotate_family_size (optional): Annotate reads with the number of reads in the family (default is False).
        allow_missing_umis (optional): Allow processing reads without UMIs (default is False).
        raw_tag (optional): Tag to use for raw (unaligned) UMI sequences if different from umi_tag (default is None).
        output_stats (optional): Path to output statistics file (default is None).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/fgbio/groupreadsbyumi",
        inputs=dict(input_bam=input_bam),
        outputs=dict(output_bam=output_bam, output_stats=output_stats)
        if output_stats
        else dict(output_bam=output_bam),
        params={
            "umi_tag": umi_tag,
            "strategy": strategy,
            "family_size_threshold": family_size_threshold,
            "min_map_qual": min_map_qual,
            "annotate_family_size": annotate_family_size,
            "allow_missing_umis": allow_missing_umis,
            "raw_tag": raw_tag,
        },
        **{key: value for key, value in kwargs.items() if value is not None},
    )


@collect_tool()
def groupreadsbyumi(
    *,
    input_bam: str,
    output_bam: str,
    umi_tag: str,
    strategy: str,
    family_size_threshold: Optional[int] = None,
    min_map_qual: Optional[int] = 0,
    annotate_family_size: Optional[bool] = False,
    allow_missing_umis: Optional[bool] = False,
    raw_tag: Optional[str] = None,
    output_stats: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Groups reads together that appear to have come from the same original molecule.

    Args:
        input_bam: Path to the input BAM file.
        output_bam: Path to the output BAM file containing grouped reads.
        umi_tag: The tag used in the input BAM to encode UMI sequences.
        strategy: The method used to group reads by UMI (e.g., "adjacency", "edit", etc.).
        family_size_threshold (optional): Minimum family size to output reads (default is None).
        min_map_qual (optional): Minimum mapping quality of reads considered (default is 0).
        annotate_family_size (optional): Annotate reads with the number of reads in the family (default is False).
        allow_missing_umis (optional): Allow processing reads without UMIs (default is False).
        raw_tag (optional): Tag to use for raw (unaligned) UMI sequences if different from umi_tag (default is None).
        output_stats (optional): Path to output statistics file (default is None).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_groupreadsbyumi(
        input_bam=input_bam,
        output_bam=output_bam,
        umi_tag=umi_tag,
        strategy=strategy,
        family_size_threshold=family_size_threshold,
        min_map_qual=min_map_qual,
        annotate_family_size=annotate_family_size,
        allow_missing_umis=allow_missing_umis,
        raw_tag=raw_tag,
        output_stats=output_stats,
         
    )
