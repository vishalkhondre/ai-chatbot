# 🤖 AI ChatBot — Semantic Kernel Agent Example

A simple yet powerful AI chatbot built with Microsoft Semantic Kernel, demonstrating how to create an intelligent conversational agent using Azure OpenAI services.

## ✨ Features

- **Azure OpenAI Integration**: Seamless connection to Azure OpenAI services
- **Semantic Kernel Agent**: Built on Microsoft's AI orchestration framework
- **Cross-Platform Support**: Works on Windows, macOS, and Linux
- **Environment-Based Configuration**: Secure API key management
- **Async/Await Support**: Modern Python async programming patterns
- **Customizable Instructions**: Configurable agent personality and behavior

## 🎯 What This Demonstrates

- **Semantic Kernel Agents**: How to create and use ChatCompletionAgent
- **Azure OpenAI Integration**: Connecting to Azure OpenAI services
- **Environment Configuration**: Secure handling of API credentials
- **Async Programming**: Proper async/await patterns for AI interactions
- **Cross-Platform Compatibility**: Windows event loop policy handling

## 🏗️ Architecture Overview

```
User Input → ChatBotAgent → AzureChatCompletion → Azure OpenAI → Response
```

The system works by:
1. User provides input to the ChatBotAgent
2. Agent processes the request through AzureChatCompletion service
3. Azure OpenAI generates a response based on the agent's instructions
4. Response is returned to the user through the agent

## 📁 Project Structure

```
aichatbot/
├── main.py           # Main application with ChatBotAgent implementation
├── requirements.txt  # Python dependencies
├── .env              # Environment variables (API keys, not committed)
└── README.md         # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Azure OpenAI service account
- Git (for cloning)

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/aichatbot.git
cd aichatbot
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name_here
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

**Note**: Replace the placeholder values with your actual Azure OpenAI credentials.

### 5. Run the Application

```bash
python main.py
```

## 💬 Usage Examples

The application currently demonstrates a simple interaction:

```python
# Example from main.py
response = await chatbot.get_response("Write a haiku about Semantic Kernel.")
print(response)
```

**Expected Output:**
```
[AI-generated haiku about Semantic Kernel]
```

## 🔧 Core Components

### ChatBotAgent Class

The main class that encapsulates the AI chatbot functionality:

```python
class ChatBotAgent:
    def __init__(self, endpoint, api_key, deployment_name, api_version, 
                 agent_name="SK-Assistant", instructions="You are a helpful assistant.")
```

**Parameters:**
- `endpoint`: Azure OpenAI endpoint URL
- `api_key`: Azure OpenAI API key
- `deployment_name`: Azure OpenAI deployment name
- `api_version`: API version (defaults to "2024-02-15-preview")
- `agent_name`: Custom name for the agent (defaults to "SK-Assistant")
- `instructions`: System instructions defining agent behavior

### Key Methods

#### `_initialize_agent()`
- **Purpose**: Sets up the AzureChatCompletion service and ChatCompletionAgent
- **Called**: Automatically during initialization
- **Functionality**: Creates the service connection and agent instance

#### `get_response(message)`
- **Purpose**: Sends a message to the AI agent and returns the response
- **Parameters**: `message` (str) - The user's input message
- **Returns**: `str` - The AI agent's response content
- **Usage**: `await chatbot.get_response("Your message here")`

## 🛠️ Technical Implementation

### Cross-Platform Compatibility

The application includes special handling for Windows systems:

```python
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```

This ensures proper async/await functionality on Windows platforms.

### Async Programming

The application uses modern Python async patterns:

- **Async functions**: All AI interactions are asynchronous
- **Event loop**: Proper event loop management for concurrent operations
- **Await patterns**: Clean async/await syntax for AI responses

### Security

- **Environment variables**: API keys stored securely in `.env` file
- **No hardcoding**: Sensitive information never appears in code
- **Dotenv integration**: Automatic loading of environment variables

## 🔄 Extending the Application

### Interactive Chat Loop

Add an interactive chat interface:

```python
async def interactive_chat():
    chatbot = ChatBotAgent(endpoint, api_key, deployment_name, api_version)
    
    print("🤖 AI ChatBot is ready! Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You > ")
        if user_input.lower() == 'exit':
            print("👋 Goodbye!")
            break
            
        response = await chatbot.get_response(user_input)
        print(f"Assistant > {response}\n")

# Run interactive chat
asyncio.run(interactive_chat())
```

### Custom Agent Instructions

Create specialized agents with custom instructions:

```python
# Technical Support Agent
tech_support_agent = ChatBotAgent(
    endpoint=endpoint,
    api_key=api_key,
    deployment_name=deployment_name,
    api_version=api_version,
    agent_name="Tech-Support",
    instructions="You are a technical support specialist. Help users with software issues."
)

# Creative Writing Agent
creative_agent = ChatBotAgent(
    endpoint=endpoint,
    api_key=api_key,
    deployment_name=deployment_name,
    api_version=api_version,
    agent_name="Creative-Writer",
    instructions="You are a creative writer. Help users with storytelling and creative content."
)
```

### Error Handling

Add robust error handling:

```python
async def get_response_with_error_handling(self, message):
    try:
        response = await self.agent.get_response(messages=message)
        return response.content
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"
```

## 🌟 Real-World Use Cases

This pattern can be extended for various applications:

- **Customer Support**: Automated customer service chatbots
- **Content Creation**: AI-powered writing assistants
- **Code Review**: Automated code analysis and suggestions
- **Data Analysis**: Natural language data querying
- **Learning**: Educational chatbots and tutors
- **Integration**: Embedding AI capabilities into existing applications

## 🔍 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed in your virtual environment
2. **API Key Issues**: Verify your Azure OpenAI credentials in the `.env` file
3. **Deployment Name**: Confirm your Azure OpenAI deployment name is correct
4. **API Version**: Check that your API version is supported
5. **Network Issues**: Check your internet connection and Azure service status

### Debug Mode

Add logging for debugging:

```python
import logging

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("semantic_kernel").setLevel(logging.DEBUG)
```

### Windows-Specific Issues

If you encounter event loop issues on Windows, the application already includes the necessary fix:

```python
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```

## 📚 Learning Resources

- [Microsoft Semantic Kernel Documentation](https://learn.microsoft.com/en-us/semantic-kernel/)
- [Semantic Kernel Agents Guide](https://learn.microsoft.com/en-us/semantic-kernel/agents/)
- [Azure OpenAI Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Python Async/Await Tutorial](https://docs.python.org/3/library/asyncio.html)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Microsoft Semantic Kernel team for the excellent framework
- Azure OpenAI for providing the language model capabilities
- The Python asyncio community for async programming patterns

---

**Happy Chatting! 🤖**

*Inspired by this example? Feel free to fork, remix, and build your own AI chatbot applications. If you write about it, please share your blog post - we'd love to see what you create!* 
