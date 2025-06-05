# 🛍️ AutoGen Retail Agent Demo

This repository demonstrates how to use [Microsoft AutoGen](https://github.com/microsoft/autogen) to build a retail customer experience powered by intelligent, multi-agent LLM workflows.

## 🧠 Agent Overview

| Agent Name          | Role Description                                 |
|---------------------|--------------------------------------------------|
| ShoppingAssistant   | Greets customer, collects preferences            |
| ProductRecommender  | Suggests products based on input                 |
| CartManager         | Manages the shopping cart                        |
| PaymentProcessor    | Handles payment securely                         |
| OrderConfirmer      | Confirms the order and delivery details          |
| PostPurchaseCritic  | Reviews the experience and interaction quality   |
| ReturnProcessor     | Handles product returns                          |
| UserProxy           | Interfaces between customer and agents           |

## 📂 Repo Structure

- `agents/`: Agent definitions (LLM configs, behavior logic)
- `scripts/`: Examples of conversations, orchestration flows
- `diagrams/`: Visual diagrams to support understanding

## 🧪 How to Run

1. Clone the repo
2. Set up your Python environment
3. Add your OpenAI API key
4. Run any sample in `scripts/`

## 🖼️ Retail Workflow Diagram

See `diagrams/Retail_Workflow_with_AutoGen_A.png` for a high-level visual of the agent workflow.

## 📌 Requirements

- Python 3.9+
- OpenAI API key
- Microsoft AutoGen (`pip install pyautogen`)
