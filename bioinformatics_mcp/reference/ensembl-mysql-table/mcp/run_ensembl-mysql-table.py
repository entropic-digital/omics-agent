from typing import Optional, Dict, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_ensembl_mysql_table(
    *,
    species: str,
    build: str,
    release: str,
    main_tables: Dict[str, str],
    join_tables: Optional[Dict[str, Dict[str, str]]] = None,
    output_tsv: Optional[str] = None,
    output_parquet: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create a table of annotations available via the versioned Ensembl mysql databases.

    Args:
        species: Species available via the Ensembl mysql databases. For valid species names, see:
                 https://ftp.ensembl.org/pub/release-x/species_EnsemblVertebrates.txt
        build: Build available for the selected species, e.g., 'GRCh38'.
        release: Release from which the species and build are available, e.g., '112'.
        main_tables: A dictionary of wanted main tables in the format { table_name: database }.
                     See: https://mart.ensembl.org/info/docs/api/index.html
        join_tables (optional): A nested dictionary to specify join tables in the format:
                                { table_name: { "database": database, "join_column": join_column_name } }.
                                Used to add further annotation columns. Default is None.
        output_tsv (optional): Path to save the output in tab-separated values (.tsv) format.
                               Default is None.
        output_parquet (optional): Path to save the output in parquet (.parquet) format.
                                   Default is None.
  
    Returns:
        subprocess.CompletedProcess: Contains information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/reference/ensembl-mysql-table",
        params={
            "species": species,
            "build": build,
            "release": release,
            "main_tables": main_tables,
            "join_tables": join_tables or {},
        },
        outputs={
            "output_tsv": output_tsv,
            "output_parquet": output_parquet,
        },
         
    )


@collect_tool()
def ensembl_mysql_table(
    *,
    species: str,
    build: str,
    release: str,
    main_tables: Dict[str, str],
    join_tables: Optional[Dict[str, Dict[str, str]]] = None,
    output_tsv: Optional[str] = None,
    output_parquet: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create a table of annotations available via the versioned Ensembl mysql databases.

    Args:
        species: Species available via the Ensembl mysql databases. For valid species names, see:
                 https://ftp.ensembl.org/pub/release-x/species_EnsemblVertebrates.txt
        build: Build available for the selected species, e.g., 'GRCh38'.
        release: Release from which the species and build are available, e.g., '112'.
        main_tables: A dictionary of wanted main tables in the format { table_name: database }.
                     See: https://mart.ensembl.org/info/docs/api/index.html
        join_tables (optional): A nested dictionary to specify join tables in the format:
                                { table_name: { "database": database, "join_column": join_column_name } }.
                                Used to add further annotation columns. Default is None.
        output_tsv (optional): Path to save the output in tab-separated values (.tsv) format.
                               Default is None.
        output_parquet (optional): Path to save the output in parquet (.parquet) format.
                                   Default is None.
  
    Returns:
        subprocess.CompletedProcess: Contains information about the completed Snakemake process.
    """
    return run_ensembl_mysql_table(
        species=species,
        build=build,
        release=release,
        main_tables=main_tables,
        join_tables=join_tables,
        output_tsv=output_tsv,
        output_parquet=output_parquet,
         
    )
