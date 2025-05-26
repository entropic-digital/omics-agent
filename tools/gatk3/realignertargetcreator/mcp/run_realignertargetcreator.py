from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_realignertargetcreator(
    *,
    bam_file: str,
    reference_genome: str,
    target_intervals: str,
    bed_file: Optional[str] = None,
    vcf_files_known_variation: Optional[str] = None,
    temp_dir: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk3 RealignerTargetCreator.

    Args:
        bam_file: Path to the input BAM file.
        reference_genome: Path to the reference genome file.
        target_intervals: Path to the output target intervals file.
        bed_file (optional): Path to the optional BED file.
        vcf_files_known_variation (optional): Path to the optional VCF files with known variations.
        temp_dir (optional): Path to the optional temporary directory.
        java_opts (optional): Additional arguments for the Java compiler, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "java_opts": java_opts,
        "extra": extra,
    }
    params = {key: value for key, value in params.items() if value is not None}

    inputs = {
        "bam_file": bam_file,
        "reference_genome": reference_genome,
        "bed_file": bed_file,
        "vcf_files_known_variation": vcf_files_known_variation,
    }
    inputs = {key: value for key, value in inputs.items() if value is not None}

    outputs = {
        "target_intervals": target_intervals,
        "temp_dir": temp_dir,
    }
    outputs = {key: value for key, value in outputs.items() if value is not None}

    return run_snake_wrapper(
        wrapper="file:tools/gatk3/realignertargetcreator",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def realignertargetcreator(
    *,
    bam_file: str,
    reference_genome: str,
    target_intervals: str,
    bed_file: Optional[str] = None,
    vcf_files_known_variation: Optional[str] = None,
    temp_dir: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk3 RealignerTargetCreator.

    Args:
        bam_file: Path to the input BAM file.
        reference_genome: Path to the reference genome file.
        target_intervals: Path to the output target intervals file.
        bed_file (optional): Path to the optional BED file.
        vcf_files_known_variation (optional): Path to the optional VCF files with known variations.
        temp_dir (optional): Path to the optional temporary directory.
        java_opts (optional): Additional arguments for the Java compiler, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_realignertargetcreator(
        bam_file=bam_file,
        reference_genome=reference_genome,
        target_intervals=target_intervals,
        bed_file=bed_file,
        vcf_files_known_variation=vcf_files_known_variation,
        temp_dir=temp_dir,
        java_opts=java_opts,
        extra=extra,
         
    )
