from typing import Optional, Dict, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_ensembl_biomart_table(
    *,
    biomart: str,
    species: str,
    build: str,
    release: str,
    attributes: List[str],
    filters: Optional[Dict[str, List[str]]] = None,
    output_tsv: Optional[str] = None,
    output_parquet: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create a table of annotations available via the `bioconductor-biomart`.

    Args:
        biomart: Name of the database, e.g., 'genes'.
        species: Species available in the database, e.g., 'homo_sapiens'.
        build: Genome build for the selected species, e.g., 'GRCh38'.
        release: Ensembl release version, e.g., '112'.
        attributes: List of annotation columns (database attributes).
        filters (optional): Dictionary of filters to apply, e.g., {"chromosome_name": ["X", "Y"]}.
        output_tsv (optional): Filepath for saving output in TSV format.
        output_parquet (optional): Filepath for saving output in Parquet format.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/reference/ensembl-biomart-table",
        params=dict(
            biomart=biomart,
            species=species,
            build=build,
            release=release,
            attributes=attributes,
            filters=filters or {},
        ),
        outputs=dict(
            output_tsv=output_tsv,
            output_parquet=output_parquet,
        ),
         
    )


@collect_tool()
def ensembl_biomart_table(
    *,
    biomart: str,
    species: str,
    build: str,
    release: str,
    attributes: List[str],
    filters: Optional[Dict[str, List[str]]] = None,
    output_tsv: Optional[str] = None,
    output_parquet: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create a table of annotations available via the `bioconductor-biomart`.

    Args:
        biomart: Name of the database, e.g., 'genes'.
        species: Species available in the database, e.g., 'homo_sapiens'.
        build: Genome build for the selected species, e.g., 'GRCh38'.
        release: Ensembl release version, e.g., '112'.
        attributes: List of annotation columns (database attributes).
        filters (optional): Dictionary of filters to apply, e.g., {"chromosome_name": ["X", "Y"]}.
        output_tsv (optional): Filepath for saving output in TSV format.
        output_parquet (optional): Filepath for saving output in Parquet format.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_ensembl_biomart_table(
        biomart=biomart,
        species=species,
        build=build,
        release=release,
        attributes=attributes,
        filters=filters,
        output_tsv=output_tsv,
        output_parquet=output_parquet,
         
    )
