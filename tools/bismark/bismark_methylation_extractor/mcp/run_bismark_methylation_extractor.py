from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_bismark_methylation_extractor(
    *,
    input_bam: str,
    output_dir: Optional[str] = None,
    ignore: Optional[int] = None,
    ignore_3prime: Optional[int] = None,
    ignore_r2: Optional[int] = None,
    ignore_3prime_r2: Optional[int] = None,
    extra: Optional[str] = None,
    mbias_report: Optional[str] = None,
    mbias_r1: Optional[str] = None,
    mbias_r2: Optional[str] = None,
    splitting_report: Optional[str] = None,
    methylome_CpG_cov: Optional[str] = None,
    methylome_CpG_mlevel_bedGraph: Optional[str] = None,
    read_base_meth_state_cpg: Optional[str] = None,
    read_base_meth_state_chg: Optional[str] = None,
    read_base_meth_state_chh: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call methylation counts from Bismark alignment results.

    Args:
        input_bam: Input BAM file aligned by Bismark.
        output_dir (optional): Output directory (current dir is used if not specified).
        ignore (optional): Number of bases to trim at 5' end in R1.
        ignore_3prime (optional): Number of bases to trim at 3' end in R1.
        ignore_r2 (optional): Number of bases to trim at 5' end in R2.
        ignore_3prime_r2 (optional): Number of bases to trim at 3' end in R2.
        extra (optional): Additional arguments for the bismark_methylation_extractor.
        mbias_report (optional): Output file for M-bias report.
        mbias_r1 (optional): Output file for M-Bias plot for R1.
        mbias_r2 (optional): Output file for M-Bias plot for R2.
        splitting_report (optional): Output file for Splitting report.
        methylome_CpG_cov (optional): Output file for Bismark CpG coverage.
        methylome_CpG_mlevel_bedGraph (optional): Output file for Bismark methylation level track.
        read_base_meth_state_cpg (optional): Output file for CpG context methylation state.
        read_base_meth_state_chg (optional): Output file for CHG context methylation state.
        read_base_meth_state_chh (optional): Output file for CHH context methylation state.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "output_dir": output_dir,
        "ignore": ignore,
        "ignore_3prime": ignore_3prime,
        "ignore_r2": ignore_r2,
        "ignore_3prime_r2": ignore_3prime_r2,
        "extra": extra,
    }
    outputs = {
        "mbias_report": mbias_report,
        "mbias_r1": mbias_r1,
        "mbias_r2": mbias_r2,
        "splitting_report": splitting_report,
        "methylome_CpG_cov": methylome_CpG_cov,
        "methylome_CpG_mlevel_bedGraph": methylome_CpG_mlevel_bedGraph,
        "read_base_meth_state_cpg": read_base_meth_state_cpg,
        "read_base_meth_state_chg": read_base_meth_state_chg,
        "read_base_meth_state_chh": read_base_meth_state_chh,
    }
    params = {k: v for k, v in params.items() if v is not None}
    outputs = {k: v for k, v in outputs.items() if v is not None}

    return run_snake_wrapper(
        wrapper="file:tools/bismark/bismark_methylation_extractor",
        inputs={"input_bam": input_bam},
        params=params,
        outputs=outputs,
         
    )


@collect_tool()
def bismark_methylation_extractor(
    *,
    input_bam: str,
    output_dir: Optional[str] = None,
    ignore: Optional[int] = None,
    ignore_3prime: Optional[int] = None,
    ignore_r2: Optional[int] = None,
    ignore_3prime_r2: Optional[int] = None,
    extra: Optional[str] = None,
    mbias_report: Optional[str] = None,
    mbias_r1: Optional[str] = None,
    mbias_r2: Optional[str] = None,
    splitting_report: Optional[str] = None,
    methylome_CpG_cov: Optional[str] = None,
    methylome_CpG_mlevel_bedGraph: Optional[str] = None,
    read_base_meth_state_cpg: Optional[str] = None,
    read_base_meth_state_chg: Optional[str] = None,
    read_base_meth_state_chh: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call methylation counts from Bismark alignment results.

    Args:
        input_bam: Input BAM file aligned by Bismark.
        output_dir (optional): Output directory (current dir is used if not specified).
        ignore (optional): Number of bases to trim at 5' end in R1.
        ignore_3prime (optional): Number of bases to trim at 3' end in R1.
        ignore_r2 (optional): Number of bases to trim at 5' end in R2.
        ignore_3prime_r2 (optional): Number of bases to trim at 3' end in R2.
        extra (optional): Additional arguments for the bismark_methylation_extractor.
        mbias_report (optional): Output file for M-bias report.
        mbias_r1 (optional): Output file for M-Bias plot for R1.
        mbias_r2 (optional): Output file for M-Bias plot for R2.
        splitting_report (optional): Output file for Splitting report.
        methylome_CpG_cov (optional): Output file for Bismark CpG coverage.
        methylome_CpG_mlevel_bedGraph (optional): Output file for Bismark methylation level track.
        read_base_meth_state_cpg (optional): Output file for CpG context methylation state.
        read_base_meth_state_chg (optional): Output file for CHG context methylation state.
        read_base_meth_state_chh (optional): Output file for CHH context methylation state.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bismark_methylation_extractor(
        input_bam=input_bam,
        output_dir=output_dir,
        ignore=ignore,
        ignore_3prime=ignore_3prime,
        ignore_r2=ignore_r2,
        ignore_3prime_r2=ignore_3prime_r2,
        extra=extra,
        mbias_report=mbias_report,
        mbias_r1=mbias_r1,
        mbias_r2=mbias_r2,
        splitting_report=splitting_report,
        methylome_CpG_cov=methylome_CpG_cov,
        methylome_CpG_mlevel_bedGraph=methylome_CpG_mlevel_bedGraph,
        read_base_meth_state_cpg=read_base_meth_state_cpg,
        read_base_meth_state_chg=read_base_meth_state_chg,
        read_base_meth_state_chh=read_base_meth_state_chh,
         
    )
