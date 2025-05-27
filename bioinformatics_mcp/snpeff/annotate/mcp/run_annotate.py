from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_annotate(
    *,
    calls: str,
    db: str,
    output_calls: str,
    output_genes: Optional[str] = None,
    output_stats: Optional[str] = None,
    output_csvstats: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Annotates the predicted effect of nucleotide changes using SnpEff.

    Args:
        calls: Input VCF/BCF file path.
        db: SnpEff database path.
        output_calls: Output file path for annotated VCF/BCF.
        output_genes (optional): Output file path for genes (if requested).
        output_stats (optional): Output file path for stats file (if requested).
        output_csvstats (optional): Output file path for stats CSV file (if requested).
        java_opts (optional): Additional Java options (e.g., "-XX:ParallelGCThreads=10").
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    outputs = {
        "calls": output_calls,
        "genes": output_genes,
        "stats": output_stats,
        "csvstats": output_csvstats,
    }
    params = {"java_opts": java_opts, "extra": extra}
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/snpeff/annotate",
        inputs=dict(calls=calls, db=db),
        outputs={k: v for k, v in outputs.items() if v is not None},
        params={k: v for k, v in params.items() if v is not None},
         
    )


@collect_tool()
def annotate(
    *,
    calls: str,
    db: str,
    output_calls: str,
    output_genes: Optional[str] = None,
    output_stats: Optional[str] = None,
    output_csvstats: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Annotates the predicted effect of nucleotide changes using SnpEff.

    Args:
        calls: Input VCF/BCF file path.
        db: SnpEff database path.
        output_calls: Output file path for annotated VCF/BCF.
        output_genes (optional): Output file path for genes (if requested).
        output_stats (optional): Output file path for stats file (if requested).
        output_csvstats (optional): Output file path for stats CSV file (if requested).
        java_opts (optional): Additional Java options (e.g., "-XX:ParallelGCThreads=10").
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_annotate(
        calls=calls,
        db=db,
        output_calls=output_calls,
        output_genes=output_genes,
        output_stats=output_stats,
        output_csvstats=output_csvstats,
        java_opts=java_opts,
        extra=extra,
         
    )
