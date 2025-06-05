from autogen import ConversableAgent

def create_return_processor(llm_config):
    return ConversableAgent(
        name="ReturnProcessor",
        llm_config=llm_config,
        system_message="You handle product return requests by asking for order number, reason, and processing confirmation.",
        human_input_mode="NEVER"
    )
