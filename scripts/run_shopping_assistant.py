from agents.shopping_assistant import create_shopping_assistant

llm_config = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "api_key": "your_openai_api_key_here"
}

assistant = create_shopping_assistant(llm_config)

response = assistant.generate_reply(messages=[
    {"role": "user", "content": "Hi, I'm looking for a new pair of running shoes."}
])

print("Assistant:", response["content"])
