from agents.shopping_assistant import create_shopping_assistant
from agents.product_recommender import create_product_recommender
from agents.order_confirmer import create_order_confirmer
from autogen import initiate_chats

llm_config = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "api_key": "your_openai_api_key_here"
}

assistant = create_shopping_assistant(llm_config)
recommender = create_product_recommender(llm_config)
confirmer = create_order_confirmer(llm_config)

initiate_chats(
    agents=[assistant, recommender, confirmer],
    message="Hi, I want to buy noise-cancelling headphones.",
    max_turns=3
)
