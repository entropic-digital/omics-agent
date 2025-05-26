from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_preprocess(
    *,
    input_bam: str,
    output_directory: str,
    reference_genome: str,
    tmp_dir: Optional[str] = None,
    additional_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GRIDSS preprocess pre-processes input BAM files for genomic rearrangement analysis.

    Args:
        input_bam: Path to the input BAM file.
        output_directory: Directory where the outputs will be saved.
        reference_genome: Path to the reference genome file.
        tmp_dir (optional): Path for temporary files directory. Defaults to None.
        additional_params (optional): Additional parameters to pass to the tool. Defaults to None.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {"tmp_dir": tmp_dir, "additional_params": additional_params}
    params = {k: v for k, v in params.items() if v is not None}

    return run_snake_wrapper(
        wrapper="file:tools/gridss/preprocess",
        inputs={"input_bam": input_bam},
        outputs={"output_directory": output_directory},
        params={"reference_genome": reference_genome, **params},
         
    )


@collect_tool()
def preprocess(
    *,
    input_bam: str,
    output_directory: str,
    reference_genome: str,
    tmp_dir: Optional[str] = None,
    additional_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GRIDSS preprocess pre-processes input BAM files for genomic rearrangement analysis.

    Args:
        input_bam: Path to the input BAM file.
        output_directory: Directory where the outputs will be saved.
        reference_genome: Path to the reference genome file.
        tmp_dir (optional): Path for temporary files directory. Defaults to None.
        additional_params (optional): Additional parameters to pass to the tool. Defaults to None.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_preprocess(
        input_bam=input_bam,
        output_directory=output_directory,
        reference_genome=reference_genome,
        tmp_dir=tmp_dir,
        additional_params=additional_params,
         
    )
