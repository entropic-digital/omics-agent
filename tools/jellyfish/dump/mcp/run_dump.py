from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_jellyfish_dump(
    *,
    kmer_count_jf_file: str,
    dump_output: str,
     
) -> subprocess.CompletedProcess:
    """
    Dump kmers from a Jellyfish database.

    Args:
        kmer_count_jf_file: Path to the Jellyfish .jf file containing kmer counts.
        dump_output: Path to the output file where kmer counts will be dumped.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/jellyfish/dump",
        inputs=dict(kmer_count_jf_file=kmer_count_jf_file),
        outputs=dict(dump_output=dump_output),
         
    )


@collect_tool()
def jellyfish_dump(
    *,
    kmer_count_jf_file: str,
    dump_output: str,
     
) -> subprocess.CompletedProcess:
    """
    Dump kmers from a Jellyfish database.

    Args:
        kmer_count_jf_file: Path to the Jellyfish .jf file containing kmer counts.
        dump_output: Path to the output file where kmer counts will be dumped.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_jellyfish_dump(
        kmer_count_jf_file=kmer_count_jf_file,
        dump_output=dump_output,
         
    )
