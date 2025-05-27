from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_msi(
    *,
    microsatellite_list: str,
    normal_bam: str,
    tumor_bam: str,
    msi_score_output: str,
    read_count_distribution_output: str,
    somatic_sites_output: str,
    germline_sites_output: str,
    additional_params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    Score your MSI with MSIsensor.

    Args:
        microsatellite_list: Path to the microsatellite and homopolymer list from MSIsensor Scan.
        normal_bam: Path to the normal BAM file.
        tumor_bam: Path to the tumoral BAM file.
        msi_score_output: Path to the output text file containing MSI scores.
        read_count_distribution_output: Path to the output TSV file with read count distribution.
        somatic_sites_output: Path to the output TSV file containing somatic sites.
        germline_sites_output: Path to the output TSV file containing germline sites.
        additional_params (optional): Additional parameters for configuration.
  
    Returns:
        subprocess.CompletedProcess: CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "microsatellite_list": microsatellite_list,
        "normal_bam": normal_bam,
        "tumor_bam": tumor_bam,
    }
    outputs = {
        "msi_score_output": msi_score_output,
        "read_count_distribution_output": read_count_distribution_output,
        "somatic_sites_output": somatic_sites_output,
        "germline_sites_output": germline_sites_output,
    }
    params = additional_params if additional_params else {}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/msisensor/msi",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def msi(
    *,
    microsatellite_list: str,
    normal_bam: str,
    tumor_bam: str,
    msi_score_output: str,
    read_count_distribution_output: str,
    somatic_sites_output: str,
    germline_sites_output: str,
    additional_params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    Score your MSI with MSIsensor.

    Args:
        microsatellite_list: Path to the microsatellite and homopolymer list from MSIsensor Scan.
        normal_bam: Path to the normal BAM file.
        tumor_bam: Path to the tumoral BAM file.
        msi_score_output: Path to the output text file containing MSI scores.
        read_count_distribution_output: Path to the output TSV file with read count distribution.
        somatic_sites_output: Path to the output TSV file containing somatic sites.
        germline_sites_output: Path to the output TSV file containing germline sites.
        additional_params (optional): Additional parameters for configuration.
  
    Returns:
        subprocess.CompletedProcess: CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_msi(
        microsatellite_list=microsatellite_list,
        normal_bam=normal_bam,
        tumor_bam=tumor_bam,
        msi_score_output=msi_score_output,
        read_count_distribution_output=read_count_distribution_output,
        somatic_sites_output=somatic_sites_output,
        germline_sites_output=germline_sites_output,
        additional_params=additional_params,
         
    )
