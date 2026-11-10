from langchain.chat_models import init_chat_model

model = init_chat_model(
    "qwen/qwen3.6-27b",
    model_provider="openai",
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    reasoning_effort="none",
)
response = model.invoke("What is the capital of Japan? Answer in one word.")

print(type(response).__name__)
print(response.text)
print(response.response_metadata["model_name"])
print(response.response_metadata["finish_reason"])
print(response.usage_metadata)
