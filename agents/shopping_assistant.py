from autogen import ConversableAgent

def create_shopping_assistant(llm_config):
    return ConversableAgent(
        name="ShoppingAssistant",
        llm_config=llm_config,
        system_message="You are a helpful retail assistant. Greet the customer and ask what they are looking for.",
        human_input_mode="NEVER"
    )
