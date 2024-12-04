import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

# Step 1: Setup Azure OpenAI
AZURE_OPENAI_ENDPOINT = "https://<your-endpoint>.openai.azure.com/"
AZURE_OPENAI_API_KEY = "<your-api-key>"
AZURE_OPENAI_DEPLOYMENT_NAME = "gpt-35-turbo"

# Initialize Azure OpenAI connector
azure_openai = AzureChatCompletion(
    deployment_name=AZURE_OPENAI_DEPLOYMENT_NAME,
    api_key=AZURE_OPENAI_API_KEY,
    endpoint=AZURE_OPENAI_ENDPOINT,
)

# Step 2: Initialize the Kernel
kernel = sk.Kernel()
kernel.add_chat_service("azure_openai", azure_openai)

# Step 3: Create a Semantic Function
# This function summarizes text into a concise summary
summary_prompt = """
Summarize the following text into a concise summary in one sentence:

{{text}}

Summary:
"""
summary_function = kernel.create_semantic_function(
    prompt=summary_prompt,
    max_tokens=100,  # Limit response length
    temperature=0.7,  # Creativity level
)

# Step 4: Execute the Semantic Function
input_text = """
Semantic Kernel is an open-source framework that simplifies the integration of AI models into applications. 
It helps developers manage prompts, execute AI plugins, and orchestrate workflows using natural language inputs.
"""

print("Input Text:")
print(input_text)

result = summary_function.invoke_async(text=input_text)
summary = result.result  # Extract the result

# Display the summary
print("\nGenerated Summary:")
print(summary)
