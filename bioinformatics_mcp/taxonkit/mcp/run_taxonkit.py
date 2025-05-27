from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_taxonkit(
    *,
    input_file: str,
    taxdump: str,
    output_taxdump: str,
    command: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run TaxonKit.

    Args:
        input_file: Input file(s) for TaxonKit.
        taxdump: Taxdump files required by TaxonKit.
        output_taxdump: Output taxdump files produced by TaxonKit.
        command: TaxonKit command to use.
        extra (optional): Additional optional parameters.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/taxonkit",
        inputs={"input": input_file, "taxdump": taxdump},
        outputs={"taxdump": output_taxdump},
        params={"command": command, "extra": extra} if extra else {"command": command},
         
    )


@collect_tool()
def taxonkit(
    *,
    input_file: str,
    taxdump: str,
    output_taxdump: str,
    command: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run TaxonKit.

    Args:
        input_file: Input file(s) for TaxonKit.
        taxdump: Taxdump files required by TaxonKit.
        output_taxdump: Output taxdump files produced by TaxonKit.
        command: TaxonKit command to use.
        extra (optional): Additional optional parameters.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_taxonkit(
        input_file=input_file,
        taxdump=taxdump,
        output_taxdump=output_taxdump,
        command=command,
        extra=extra,
         
    )
