from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureOpenAI
from semantic_kernel.orchestration.context_variables import ContextVariables

# Initialize Semantic Kernel
kernel = Kernel()

# Configure AzureOpenAI
deployment_name = "text-davinci-003"  # Replace with your Azure OpenAI deployment name
api_key = "<your-azure-openai-key>"  # Replace with your Azure OpenAI API key
endpoint = "https://<your-endpoint>.openai.azure.com/"  # Replace with your Azure OpenAI endpoint

# Add AzureOpenAI model to the kernel
azure_openai_model = AzureOpenAI(
    deployment_name=deployment_name,
    api_key=api_key,
    endpoint=endpoint
)

kernel.add_text_completion_service(
    service_id="openai-service",
    service=azure_openai_model
)

# Define Chat Functionality
def chatbot_response(user_input):
    """
    Process user input using AzureOpenAI and return the response.
    """
    try:
        # Use Semantic Kernel to invoke the model
        context_vars = ContextVariables()  # Initialize context variables
        context_vars["input"] = user_input  # Add user input to the context

        # Call the text completion service
        response = kernel.run("openai-service", input_vars=context_vars)
        return response

    except Exception as e:
        return f"Error: {str(e)}"

# Main Chat Loop
if __name__ == "__main__":
    print("Chatbot is running. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Get chatbot response
        bot_response = chatbot_response(user_input)
        print(f"Bot: {bot_response}")
