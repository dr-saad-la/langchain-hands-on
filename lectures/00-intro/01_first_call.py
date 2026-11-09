from langchain.chat_models import init_chat_model

model = init_chat_model(
    "qwen/qwen3.6-27b",
    model_provider="openai",
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
)
response = model.invoke("Explain what LangChain is in one sentence.")
print(response.text)
