from autogen import AssistantAgent

def create_product_recommender(llm_config):
    return AssistantAgent(
        name="ProductRecommender",
        llm_config=llm_config,
        system_message="You recommend products based on customer preferences. Be concise and helpful.",
        human_input_mode="NEVER"
    )
