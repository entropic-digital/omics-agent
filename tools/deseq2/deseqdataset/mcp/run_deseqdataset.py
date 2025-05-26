from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_deseqdataset(
    *,
    colData: Optional[str] = None,
    dds: Optional[str] = None,
    txi: Optional[str] = None,
    se: Optional[str] = None,
    matrix: Optional[str] = None,
    counts: Optional[str] = None,
    htseq_dir: Optional[str] = None,
    sample_table: Optional[str] = None,
    output: str,
    formula: str,
    reference_level: Optional[str] = None,
    tested_level: Optional[str] = None,
    factor: Optional[str] = None,
    min_count: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create a DESeqDataSet object and optionally run DESeq2 pre-filtering.

    Args:
        colData: Path to the TSV file describing the experiment design. First column contains sample names.
        dds: Path to the DESeqDataSet object (RDS format).
        txi: Path to the tximport/tximeta SummarizedExperiment object (RDS format).
        se: Path to the RangedSummarizedExperiment object (RDS format).
        matrix: Path to the R matrix object containing counts (RDS format). Sample names must be in rownames.
        counts: Path to the text matrix containing counts (TSV format). Sample names should be in the first column.
        htseq_dir: Path to the directory containing HTSeq/FeatureCount count matrices.
        sample_table: Path to the TSV table containing sample names and paths to HTSeq/FeatureCount count matrices.
        output: Path where the created DESeqDataSet object will be saved (RDS format).
        formula: The design formula for DESeq2.
        reference_level: Optional reference level name, in case releveling is needed.
        tested_level: Optional tested level name, in case releveling is needed.
        factor: Factor of interest, in case releveling is needed.
        min_count: Minimum number of counted/estimated reads threshold (default is no filtering).
        extra: Optional additional argument to customize DESeq2 behavior.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "colData": colData,
        "dds": dds,
        "txi": txi,
        "se": se,
        "matrix": matrix,
        "counts": counts,
        "htseq_dir": htseq_dir,
        "sample_table": sample_table,
    }
    inputs = {k: v for k, v in inputs.items() if v is not None}

    params = {
        "formula": formula,
        "reference_level": reference_level,
        "tested_level": tested_level,
        "factor": factor,
        "min_count": min_count,
        "extra": extra,
    }
    params = {k: v for k, v in params.items() if v is not None}

    return run_snake_wrapper(
        wrapper="file:tools/deseq2/deseqdataset",
        inputs=inputs,
        outputs={"output": output},
        params=params,
         
    )


@collect_tool()
def deseqdataset(
    *,
    colData: Optional[str] = None,
    dds: Optional[str] = None,
    txi: Optional[str] = None,
    se: Optional[str] = None,
    matrix: Optional[str] = None,
    counts: Optional[str] = None,
    htseq_dir: Optional[str] = None,
    sample_table: Optional[str] = None,
    output: str,
    formula: str,
    reference_level: Optional[str] = None,
    tested_level: Optional[str] = None,
    factor: Optional[str] = None,
    min_count: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create a DESeqDataSet object and optionally run DESeq2 pre-filtering.

    Args:
        colData: Path to the TSV file describing the experiment design. First column contains sample names.
        dds: Path to the DESeqDataSet object (RDS format).
        txi: Path to the tximport/tximeta SummarizedExperiment object (RDS format).
        se: Path to the RangedSummarizedExperiment object (RDS format).
        matrix: Path to the R matrix object containing counts (RDS format). Sample names must be in rownames.
        counts: Path to the text matrix containing counts (TSV format). Sample names should be in the first column.
        htseq_dir: Path to the directory containing HTSeq/FeatureCount count matrices.
        sample_table: Path to the TSV table containing sample names and paths to HTSeq/FeatureCount count matrices.
        output: Path where the created DESeqDataSet object will be saved (RDS format).
        formula: The design formula for DESeq2.
        reference_level: Optional reference level name, in case releveling is needed.
        tested_level: Optional tested level name, in case releveling is needed.
        factor: Factor of interest, in case releveling is needed.
        min_count: Minimum number of counted/estimated reads threshold (default is no filtering).
        extra: Optional additional argument to customize DESeq2 behavior.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_deseqdataset(
        colData=colData,
        dds=dds,
        txi=txi,
        se=se,
        matrix=matrix,
        counts=counts,
        htseq_dir=htseq_dir,
        sample_table=sample_table,
        output=output,
        formula=formula,
        reference_level=reference_level,
        tested_level=tested_level,
        factor=factor,
        min_count=min_count,
        extra=extra,
         
    )
