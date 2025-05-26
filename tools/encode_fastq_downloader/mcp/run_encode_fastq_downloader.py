from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_encode_fastq_downloader(
    *,
    encode_assay_accession: Optional[str] = None,
    encode_file_accession: Optional[str] = None,
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Download fastq files directly from the ENCODE project.

    Args:
        encode_assay_accession (optional): ENCODE assay accession (e.g., ENCSRXXXXX) to specify the dataset.
        encode_file_accession (optional): ENCODE file accession (e.g., ENCFFXXXXX) to specify a single file.
        output_file: Path to the output file or directory where the downloaded fastq files will be stored.
  
    Notes:
        - Either `encode_assay_accession` or `encode_file_accession` must be specified.
        - The `encode_file_accession` must refer to a fastq file.
        - For paired-end data, both files (R1 and R2) are downloaded when specifying a file accession.
        - For multiple runs under a single assay accession, files are concatenated.

    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    if not encode_assay_accession and not encode_file_accession:
        raise ValueError(
            "Either `encode_assay_accession` or `encode_file_accession` must be specified."
        )

    inputs = {}
    if encode_assay_accession:
        inputs["encode_assay_accession"] = encode_assay_accession
    if encode_file_accession:
        inputs["encode_file_accession"] = encode_file_accession

    return run_snake_wrapper(
        wrapper="file:tools/encode_fastq_downloader",
        inputs=inputs,
        outputs={"output_file": output_file},
         
    )


@collect_tool()
def encode_fastq_downloader(
    *,
    encode_assay_accession: Optional[str] = None,
    encode_file_accession: Optional[str] = None,
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Download fastq files directly from the ENCODE project.

    Args:
        encode_assay_accession (optional): ENCODE assay accession (e.g., ENCSRXXXXX) to specify the dataset.
        encode_file_accession (optional): ENCODE file accession (e.g., ENCFFXXXXX) to specify a single file.
        output_file: Path to the output file or directory where the downloaded fastq files will be stored.
  
    Notes:
        - Either `encode_assay_accession` or `encode_file_accession` must be specified.
        - The `encode_file_accession` must refer to a fastq file.
        - For paired-end data, both files (R1 and R2) are downloaded when specifying a file accession.
        - For multiple runs under a single assay accession, files are concatenated.

    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_encode_fastq_downloader(
        encode_assay_accession=encode_assay_accession,
        encode_file_accession=encode_file_accession,
        output_file=output_file,
         
    )
