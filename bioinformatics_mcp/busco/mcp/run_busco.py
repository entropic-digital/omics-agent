from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_busco(
    *,
    input_fasta: str,
    out_dir: str,
    lineage: Optional[str] = None,
    mode: str,
    dataset_dir: Optional[str] = None,
    short_txt: Optional[str] = None,
    short_json: Optional[str] = None,
    full_table: Optional[str] = None,
    miss_list: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Assess assembly and annotation completeness with BUSCO.

    Args:
        input_fasta: Path to assembly fasta.
        out_dir: Path to output directory with annotation quality files.
        lineage (optional): Assembly lineage.
        mode: Analysis mode, either `genome`, `transcriptome`, or `proteins`.
        dataset_dir (optional): Path to dataset directory.
        short_txt (optional): Path to plain text results summary. Requires `lineage` parameter.
        short_json (optional): Path to JSON formatted results summary. Requires `lineage` parameter.
        full_table (optional): Path to TSV formatted results. Requires `lineage` parameter.
        miss_list (optional): Path to file listing missing BUSCOs. Requires `lineage` parameter.
        extra (optional): Additional parameters besides `mode`, `--lineage`, `--cpu`, and IO files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {"input_fasta": input_fasta}
    outputs = {
        "out_dir": out_dir,
        "dataset_dir": dataset_dir,
        "short_txt": short_txt,
        "short_json": short_json,
        "full_table": full_table,
        "miss_list": miss_list,
    }
    params = {"lineage": lineage, "mode": mode, "extra": extra}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/busco",
        inputs=inputs,
        outputs={key: value for key, value in outputs.items() if value is not None},
        params={key: value for key, value in params.items() if value is not None},
         
    )


@collect_tool()
def busco(
    *,
    input_fasta: str,
    out_dir: str,
    lineage: Optional[str] = None,
    mode: str,
    dataset_dir: Optional[str] = None,
    short_txt: Optional[str] = None,
    short_json: Optional[str] = None,
    full_table: Optional[str] = None,
    miss_list: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Assess assembly and annotation completeness with BUSCO.

    Args:
        input_fasta: Path to assembly fasta.
        out_dir: Path to output directory with annotation quality files.
        lineage (optional): Assembly lineage.
        mode: Analysis mode, either `genome`, `transcriptome`, or `proteins`.
        dataset_dir (optional): Path to dataset directory.
        short_txt (optional): Path to plain text results summary. Requires `lineage` parameter.
        short_json (optional): Path to JSON formatted results summary. Requires `lineage` parameter.
        full_table (optional): Path to TSV formatted results. Requires `lineage` parameter.
        miss_list (optional): Path to file listing missing BUSCOs. Requires `lineage` parameter.
        extra (optional): Additional parameters besides `mode`, `--lineage`, `--cpu`, and IO files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_busco(
        input_fasta=input_fasta,
        out_dir=out_dir,
        lineage=lineage,
        mode=mode,
        dataset_dir=dataset_dir,
        short_txt=short_txt,
        short_json=short_json,
        full_table=full_table,
        miss_list=miss_list,
        extra=extra,
         
    )
