from agents.shopping_assistant import create_shopping_assistant
from agents.return_processor import create_return_processor
from agents.proxy_agent import create_user_proxy

llm_config = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "api_key": "your_openai_api_key_here"
}

assistant = create_shopping_assistant(llm_config)
return_agent = create_return_processor(llm_config)
proxy = create_user_proxy()

proxy.initiate_chat(
    assistant,
    message="I need help returning my order."
)

assistant.register_nested_chats(
    chat_queue=[{"recipient": return_agent, "message": "Customer wants to return order #98765"}],
    trigger="return",
    reply_func_from_nested_chats="summary_from_nested_chats"
)
