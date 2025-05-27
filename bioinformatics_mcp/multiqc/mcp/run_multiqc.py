from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_multiqc(
    *,
    input_dir: str,
    qc_report: str,
    multiqc_data: Optional[str] = None,
    extra: Optional[str] = None,
    use_input_files_only: bool = False,
     
) -> subprocess.CompletedProcess:
    """
    Generate QC report using MultiQC.

    Args:
        input_dir: Input directory containing QC files. Default behavior is to extract folder path from the provided files or parent folder if a folder is provided.
        qc_report: QC report (HTML).
        multiqc_data (optional): MultiQC data folder or ZIP (optional).
        extra (optional): Additional program arguments.
        use_input_files_only (optional): If set to True, input will be used as provided, i.e., no folder will be extracted from file names.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/multiqc",
        inputs={"input_dir": input_dir},
        outputs={"qc_report": qc_report, "multiqc_data": multiqc_data}
        if multiqc_data
        else {"qc_report": qc_report},
        params={"extra": extra, "use_input_files_only": use_input_files_only},
         
    )


@collect_tool()
def multiqc(
    *,
    input_dir: str,
    qc_report: str,
    multiqc_data: Optional[str] = None,
    extra: Optional[str] = None,
    use_input_files_only: bool = False,
     
) -> subprocess.CompletedProcess:
    """
    Generate QC report using MultiQC.

    Args:
        input_dir: Input directory containing QC files. Default behavior is to extract folder path from the provided files or parent folder if a folder is provided.
        qc_report: QC report (HTML).
        multiqc_data (optional): MultiQC data folder or ZIP (optional).
        extra (optional): Additional program arguments.
        use_input_files_only (optional): If set to True, input will be used as provided, i.e., no folder will be extracted from file names.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_multiqc(
        input_dir=input_dir,
        qc_report=qc_report,
        multiqc_data=multiqc_data,
        extra=extra,
        use_input_files_only=use_input_files_only,
         
    )
