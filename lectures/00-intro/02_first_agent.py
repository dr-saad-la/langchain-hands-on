from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool


@tool
def count_letter(word: str, letter: str) -> int:
    """Count how many times a letter appears in a word."""
    return word.lower().count(letter.lower())


model = init_chat_model(
    "qwen/qwen3.6-27b",
    model_provider="openai",
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
)

agent = create_agent(
    model=model,
    tools=[count_letter],
    system_prompt="You are a careful assistant. Use a tool whenever you need to count.",
)

question = "How many times does the letter r appear in the word strawberry?"

for step in agent.stream(
    {"messages": [{"role": "user", "content": question}]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()
