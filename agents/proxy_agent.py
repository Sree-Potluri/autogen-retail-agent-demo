from autogen import UserProxyAgent

def create_user_proxy():
    return UserProxyAgent(
        name="UserProxy",
        human_input_mode="ALWAYS",
        max_consecutive_auto_reply=1,
        code_execution_config={"use_docker": False}
    )
