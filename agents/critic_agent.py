from autogen import ConversableAgent

def create_critic_agent(llm_config):
    return ConversableAgent(
        name="CriticAgent",
        llm_config=llm_config,
        system_message="You evaluate agent responses and provide feedback for improvement.",
        human_input_mode="NEVER"
    )
