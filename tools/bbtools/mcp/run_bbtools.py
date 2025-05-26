from typing import Optional, List
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_bbtools(
    *,
    command: str,
    input: Optional[List[str]] = None,
    flag: Optional[str] = None,
    out: Optional[List[str]] = None,
    outm: Optional[List[str]] = None,
    outu: Optional[List[str]] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Wrapper for all tools in the BBmap suite.

    This function allows running any BBmap suite tool by dynamically constructing
    the required command with appropriate inputs, outputs, and parameters.

    Args:
        command: The BBtools command to run (e.g., 'bbmap.sh'). Required parameter.
        input (optional): Input files. If two are provided, they are treated as 'in1' and 'in2'.
        flag (optional): Ignored parameter used to specify auxiliary input files.
        out (optional): Output files. If two are provided, they are treated as 'out1' and 'out2'.
        outm (optional): Treated the same way as 'out'.
        outu (optional): Treated the same way as 'out'.
        extra (optional): Additional arguments to include in the command.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {}
    params = {}

    # Parse 'input' and map to 'in' or 'in1', 'in2'
    if input:
        if len(input) == 2:
            inputs.update({"in1": input[0], "in2": input[1]})
        else:
            inputs["in"] = ",".join(input)

    # Parse outputs: 'out', 'outm', 'outu'
    for output_key in ["out", "outm", "outu"]:
        output_value = locals()[output_key]
        if output_value:
            if len(output_value) == 2:
                params.update(
                    {
                        f"{output_key}1": output_value[0],
                        f"{output_key}2": output_value[1],
                    }
                )
            else:
                params[output_key] = ",".join(output_value)

    # Add extra parameters
    if extra:
        params["extra"] = extra

    # Filter out the 'flag' keyword (not passed to the tool)
    if "flag" in kwargs:
        kwargs.pop("flag")

    return run_snake_wrapper(
        wrapper="file:tools/bbtools",
        inputs=inputs,
        params=params,
        config={"command": command},
         
    )


@collect_tool()
def bbtools(
    *,
    command: str,
    input: Optional[List[str]] = None,
    flag: Optional[str] = None,
    out: Optional[List[str]] = None,
    outm: Optional[List[str]] = None,
    outu: Optional[List[str]] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Wrapper for all tools in the BBmap suite.

    This function allows running any BBmap suite tool by dynamically constructing
    the required command with appropriate inputs, outputs, and parameters.

    Args:
        command: The BBtools command to run (e.g., 'bbmap.sh'). Required parameter.
        input (optional): Input files. If two are provided, they are treated as 'in1' and 'in2'.
        flag (optional): Ignored parameter used to specify auxiliary input files.
        out (optional): Output files. If two are provided, they are treated as 'out1' and 'out2'.
        outm (optional): Treated the same way as 'out'.
        outu (optional): Treated the same way as 'out'.
        extra (optional): Additional arguments to include in the command.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bbtools(
        command=command,
        input=input,
        flag=flag,
        out=out,
        outm=outm,
        outu=outu,
        extra=extra,
         
    )
