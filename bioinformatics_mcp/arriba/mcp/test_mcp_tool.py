import os
from smolagents import CodeAgent, Tool
from smolagents.models import LiteLLMModel
from run_arriba import arriba
from smolagents.models import AzureOpenAIServerModel
import dotenv

dotenv.load_dotenv()

# Configure the LiteLLMModel for Azure OpenAI
model = AzureOpenAIServerModel(
    model_id="gpt-4o-mini",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
)


# Initialize the CodeAgent with the tool and model
agent = CodeAgent(
    tools=[arriba],
    model=model,
    add_base_tools=True
)

# Define the prompt
prompt = """
Run the Arriba tool with the following parameters:
- BAM file: /Users/brunopandza/Documents/bioinfo-mcp/bioinformatics-mcp/tools/arriba/test/A.bam
- Genome FASTA: /Users/brunopandza/Documents/bioinfo-mcp/bioinformatics-mcp/tools/arriba/test/genome.fasta
- GTF annotation: /Users/brunopandza/Documents/bioinfo-mcp/bioinformatics-mcp/tools/arriba/test/annotation.gtf
- Output fusions: /Users/brunopandza/Documents/bioinfo-mcp/bioinformatics-mcp/tools/arriba/test/fusions.tsv
Include the extra argument: --discard-overlapping-reads
"""

# Execute the agent with the prompt
response = agent.run(prompt)

# Print the response
print("Agent Response:", response)
