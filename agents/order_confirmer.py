from autogen import AssistantAgent

def create_order_confirmer(llm_config):
    return AssistantAgent(
        name="OrderConfirmer",
        llm_config=llm_config,
        system_message="You confirm orders and provide estimated delivery times.",
        human_input_mode="NEVER"
    )
