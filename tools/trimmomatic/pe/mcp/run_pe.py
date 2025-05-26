from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_pe(
    *,
    input1: str,
    input2: str,
    output1: str,
    output2: str,
    output_unpaired1: str,
    output_unpaired2: str,
    threads: int,
    phred: str = "33",
    adapter: Optional[str] = None,
    slidingwindow: Optional[str] = None,
    leading: Optional[int] = None,
    trailing: Optional[int] = None,
    crop: Optional[int] = None,
    headcrop: Optional[int] = None,
    minlen: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Trim paired-end reads using trimmomatic.

    Args:
        input1: Path to the first paired-end input file.
        input2: Path to the second paired-end input file.
        output1: Path to the trimmed output file for the first read pair.
        output2: Path to the trimmed output file for the second read pair.
        output_unpaired1: Path to the output file for unpaired reads from the first input.
        output_unpaired2: Path to the output file for unpaired reads from the second input.
        threads: Number of threads to use for processing.
        phred: Phred encoding of the input files ('33' or '64'). Default is '33'.
        adapter (optional): Adapter file or string for trimming. Default is None.
        slidingwindow (optional): Sliding window trimming parameter (e.g., '4:20'). Default is None.
        leading (optional): Quality threshold for leading bases trimming. Default is None.
        trailing (optional): Quality threshold for trailing bases trimming. Default is None.
        crop (optional): Number of bases to retain starting from the 5' end. Default is None.
        headcrop (optional): Number of bases to exclude starting from the 5' end. Default is None.
        minlen (optional): Minimum read length to retain. Default is None.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/trimmomatic/pe",
        inputs=dict(input1=input1, input2=input2),
        outputs=dict(
            output1=output1,
            output2=output2,
            output_unpaired1=output_unpaired1,
            output_unpaired2=output_unpaired2,
        ),
        params={
            "adapter": adapter,
            "slidingwindow": slidingwindow,
            "leading": leading,
            "trailing": trailing,
            "crop": crop,
            "headcrop": headcrop,
            "minlen": minlen,
            "threads": threads,
            "phred": phred,
        },
         
    )


@collect_tool()
def pe(
    *,
    input1: str,
    input2: str,
    output1: str,
    output2: str,
    output_unpaired1: str,
    output_unpaired2: str,
    threads: int,
    phred: str = "33",
    adapter: Optional[str] = None,
    slidingwindow: Optional[str] = None,
    leading: Optional[int] = None,
    trailing: Optional[int] = None,
    crop: Optional[int] = None,
    headcrop: Optional[int] = None,
    minlen: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Trim paired-end reads using trimmomatic.

    Args:
        input1: Path to the first paired-end input file.
        input2: Path to the second paired-end input file.
        output1: Path to the trimmed output file for the first read pair.
        output2: Path to the trimmed output file for the second read pair.
        output_unpaired1: Path to the output file for unpaired reads from the first input.
        output_unpaired2: Path to the output file for unpaired reads from the second input.
        threads: Number of threads to use for processing.
        phred: Phred encoding of the input files ('33' or '64'). Default is '33'.
        adapter (optional): Adapter file or string for trimming. Default is None.
        slidingwindow (optional): Sliding window trimming parameter (e.g., '4:20'). Default is None.
        leading (optional): Quality threshold for leading bases trimming. Default is None.
        trailing (optional): Quality threshold for trailing bases trimming. Default is None.
        crop (optional): Number of bases to retain starting from the 5' end. Default is None.
        headcrop (optional): Number of bases to exclude starting from the 5' end. Default is None.
        minlen (optional): Minimum read length to retain. Default is None.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_pe(
        input1=input1,
        input2=input2,
        output1=output1,
        output2=output2,
        output_unpaired1=output_unpaired1,
        output_unpaired2=output_unpaired2,
        threads=threads,
        phred=phred,
        adapter=adapter,
        slidingwindow=slidingwindow,
        leading=leading,
        trailing=trailing,
        crop=crop,
        headcrop=headcrop,
        minlen=minlen,
         
    )
