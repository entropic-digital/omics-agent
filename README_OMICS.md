# Omics Agent

Approximate dev instructions
1. Complete the uv stuff
if first time
```uv init
```
```uv venv```
after update if needed
```uv sync```

2. Download bioinformatics-mcp repo
```uv add --editable <path-to-bioinformatics-mcp>```
```uv pip install -e <path-to-bioinformatics-mcp>```

3. Start the omics_runner to use Jupyter execution
```bash
backend/omics_runner/start_runner.sh
```
