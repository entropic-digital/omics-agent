from typing import List, Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    sequence: List[str],
    output: List[str],
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create index files for `hisat2`.

    Args:
        sequence: List of FASTA files to index.
        output: List of output index file paths. The `hisat2-build` command generates
                8 files with `.ht2` extension for small genomes and `.ht2l` for large
                genomes (greater than ~4 Gbp). Use `.ht2l` as the output file extension
                if forcing the creation of a large index using the `--large-index` parameter.
        extra (optional): Additional parameters that will be passed to `hisat2-build`.
            
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/hisat2/index",
        inputs={"sequence": sequence},
        outputs={"output": output},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def index(
    *,
    sequence: List[str],
    output: List[str],
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create index files for `hisat2`.

    Args:
        sequence: List of FASTA files to index.
        output: List of output index file paths. The `hisat2-build` command generates
                8 files with `.ht2` extension for small genomes and `.ht2l` for large
                genomes (greater than ~4 Gbp). Use `.ht2l` as the output file extension
                if forcing the creation of a large index using the `--large-index` parameter.
        extra (optional): Additional parameters that will be passed to `hisat2-build`.
            
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(
        sequence=sequence,
        output=output,
        extra=extra,
         
    )
