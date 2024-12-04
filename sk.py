import os
from semantic_kernel import Kernel
from semantic_kernel.ai.open_ai import AzureOpenAI
from semantic_kernel.orchestration import SkContext

# Set your Azure OpenAI API key and endpoint
api_key = "your_azure_openai_api_key"
api_endpoint = "your_azure_openai_endpoint"

# Initialize the Semantic Kernel
kernel = Kernel()

# Set up Azure OpenAI connector with API Key and Endpoint
azure_openai = AzureOpenAI(
    api_key=api_key,
    endpoint=api_endpoint,
    model="gpt-3.5-turbo"  # You can use any available model like "gpt-4", "gpt-3.5-turbo"
)

# Add the Azure OpenAI to the kernel
kernel.add_ai_connector("azure_openai", azure_openai)

# Define a simple prompt to test
prompt = "What is the capital of France?"

# Execute the prompt using Azure OpenAI through the Semantic Kernel
context = SkContext()
response = kernel.run_async("azure_openai", prompt, context)

# Print the response
print(f"Response from Azure OpenAI: {response.result}")
