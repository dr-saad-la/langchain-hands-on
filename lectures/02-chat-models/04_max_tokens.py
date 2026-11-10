from langchain.chat_models import init_chat_model

settings = dict(
    model_provider="openai",
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    max_tokens=20,
)
thinking_off = init_chat_model("qwen/qwen3.6-27b", reasoning_effort="none", **settings)
thinking_on = init_chat_model("qwen/qwen3.6-27b", **settings)

question = "Explain what a large language model is."

for name, model in [("thinking off", thinking_off), ("thinking on", thinking_on)]:
    response = model.invoke(question)
    print(name)
    print(f"  text: {response.text.strip()!r}")
    print(f"  finish_reason: {response.response_metadata['finish_reason']}")
    print(f"  tokens: {response.usage_metadata['output_token_details']}")
