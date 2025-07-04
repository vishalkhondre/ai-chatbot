import sys
import os
import asyncio
from dotenv import load_dotenv
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

# Ensure compatibility with Windows event loop policy for asyncio
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class ChatBotAgent:
    """
    Encapsulates the Azure OpenAI chat agent using Semantic Kernel's agent-based API.
    Handles initialization and message interaction.
    """
    def __init__(self, endpoint, api_key, deployment_name, api_version, agent_name="SK-Assistant", instructions="You are a helpful assistant."):
        # Store configuration
        self.endpoint = endpoint
        self.api_key = api_key
        self.deployment_name = deployment_name
        self.api_version = api_version
        self.agent_name = agent_name
        self.instructions = instructions
        self.agent = None
        self._initialize_agent()

    def _initialize_agent(self):
        """
        Initializes the AzureChatCompletion service and the ChatCompletionAgent.
        """
        service = AzureChatCompletion(
            endpoint=self.endpoint,
            api_key=self.api_key,
            deployment_name=self.deployment_name,
            api_version=self.api_version
        )
        self.agent = ChatCompletionAgent(
            service=service,
            name=self.agent_name,
            instructions=self.instructions
        )

    async def get_response(self, message):
        """
        Sends a message to the assistant and returns the response content.
        """
        response = await self.agent.get_response(messages=message)
        return response.content

async def main():
    # Load environment variables from a .env file for secure configuration
    load_dotenv()

    # Retrieve Azure OpenAI configuration from environment variables
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")

    # Instantiate the chatbot agent with loaded configuration
    chatbot = ChatBotAgent(endpoint, api_key, deployment_name, api_version)

    # Send a prompt to the assistant and print the response
    response = await chatbot.get_response("Write a haiku about Semantic Kernel.")
    print(response)

# Run the main async function
asyncio.run(main())
