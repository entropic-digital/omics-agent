from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_csvreport(
    *,
    csv_file: str,
    output_folder: str,
     
) -> subprocess.CompletedProcess:
    """
    Creates an HTML report of QC data stored in a CSV file.

    Args:
        csv_file: Path to the input CSV file containing the QC report.
        output_folder: Path to the output folder to store the HTML document and .xlsx file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/rbt/csvreport",
        inputs={"csv_file": csv_file},
        outputs={"output_folder": output_folder},
         
    )


@collect_tool()
def csvreport(
    *,
    csv_file: str,
    output_folder: str,
     
) -> subprocess.CompletedProcess:
    """
    Creates an HTML report of QC data stored in a CSV file.

    Args:
        csv_file: Path to the input CSV file containing the QC report.
        output_folder: Path to the output folder to store the HTML document and .xlsx file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_csvreport(
        csv_file=csv_file,
        output_folder=output_folder,
         
    )
