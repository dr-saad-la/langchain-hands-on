from langchain.chat_models import init_chat_model

prompt = "Write a one-sentence slogan for a coffee shop."

for temperature in [0.0, 1.5]:
    model = init_chat_model(
        "qwen/qwen3.6-27b",
        model_provider="openai",
        base_url="http://localhost:1234/v1",
        api_key="lm-studio",
        reasoning_effort="none",
        temperature=temperature,
    )
    print(f"temperature {temperature}")
    for _ in range(3):
        print(f"  {model.invoke(prompt).text.strip()}")
