from langchain.chat_models import init_chat_model

model = init_chat_model("claude-haiku-5-5", model_provider="anthropic")
response = model.invoke("What is the capital of Japan? Answer in one word.")

print(type(response).__name__)
print(response.text)
print(response.response_metadata.get("model_name"))
print(response.usage_metadata)
