import subprocess
from typing import Any, Dict, Optional


def _format_item(key: str, value: str) -> str:
    """Format a single key-value pair for the Snakefile."""
    return f'{key}=r"{value}",'


def run_snake_wrapper(
    *,
    wrapper: str,
    inputs: Dict[str, str],
    outputs: Dict[str, str],
    params: Optional[Dict[str, Any]] = None,
    threads: int = 1,
    wrapper_prefix: str = (
        "https://raw.githubusercontent.com/"
        "snakemake/snakemake-wrappers/refs/heads/master/bio/"
    ),
    snakefile_extra: str = "",
    print_only: bool = False,
) -> bool:
    """Render a Snakefile for the chosen wrapper and run Snakemake.

    Returns:
        bool: True if the Snakemake run was successful, False otherwise.
    """

    params = params or {}

    # Start building the Snakefile
    wrapper_name = wrapper.split("/")[-1]
    lines = [f"rule {wrapper_name}:"]

    # Add inputs
    lines.append("    input:")
    if not inputs:
        lines.append("        # (none)")
    else:
        for k, v in inputs.items():
            lines.append(f"        {_format_item(k, v)}")

    # Add outputs
    lines.append("    output:")
    if not outputs:
        lines.append("        # (none)")
    else:
        for k, v in outputs.items():
            lines.append(f"        {_format_item(k, v)}")

    # Add params
    lines.append("    params:")
    if not params:
        lines.append("        # (none)")
    else:
        for k, v in params.items():
            lines.append(f"        {_format_item(k, v)}")

    # Add remaining fields
    lines.append(f"    threads: {threads}")
    lines.append("    wrapper:")
    lines.append(f'        "{wrapper}"')

    snakefile_txt = (
        "\n".join(lines) + "\n" + (snakefile_extra if snakefile_extra else "")
    )

    # We initialize the run command and will add the temp Snakefile later
    cmd = [
        "snakemake",
        "--cores",
        str(threads),
        "--sdm",
        "conda",
        "--wrapper-prefix",
        wrapper_prefix,
    ]
    if print_only:
        print("# ---- Rendered Snakefile ----")
        print(snakefile_txt)
        print("# ---- Snakemake command ----")
        print(" ".join(cmd[:-1] + ["<temporary_snakefile>"]))
        return True

    print(snakefile_txt)

    # Write to a regular Snakefile
    with open("Snakefile", "w") as sf:
        sf.write(snakefile_txt)
        sf.flush()

        try:
            result = subprocess.run(cmd, check=True)
            return result
        except subprocess.CalledProcessError:
            return subprocess.CalledProcessError
