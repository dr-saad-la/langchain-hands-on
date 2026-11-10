import time

from langchain.chat_models import init_chat_model

settings = dict(
    model_provider="openai",
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
)
thinking_off = init_chat_model("qwen/qwen3.6-27b", reasoning_effort="none", **settings)
thinking_on = init_chat_model("qwen/qwen3.6-27b", **settings)

question = (
    "A bat and a ball cost $1.10 in total. "
    "The bat costs $1.00 more than the ball. "
    "How much does the ball cost? Answer with the amount only."
)

for name, model in [("thinking off", thinking_off), ("thinking on", thinking_on)]:
    start = time.perf_counter()
    response = model.invoke(question)
    seconds = time.perf_counter() - start
    reasoning = response.usage_metadata["output_token_details"]["reasoning"]
    print(f"{name}: {seconds:.1f} s, {reasoning} reasoning tokens")
    print(response.text.strip())
