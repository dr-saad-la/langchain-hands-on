# LangChain, Hands-On

The code for **LangChain, Hands-On**, a 20-lecture, beginner-friendly course on
building applications with language models in Python, from your first call to
a working research assistant. A new lecture every Monday.

Everything runs on your own machine, with a local model: free, no API key.

## Setup

1. Install [LM Studio](https://lmstudio.ai), download **Qwen3.6 27B** from its
   Discover tab (on a smaller machine: **Gemma 4 E4B**), then:
   ```zsh
   lms load qwen/qwen3.6-27b
   lms server start
   ```
2. Install [uv](https://docs.astral.sh/uv/), then in this folder:
   ```zsh
   uv sync
   uv run lectures/00-intro/01_first_call.py
   ```

## Lectures

| # | Lecture | Video |
|---|---|---|
| 00 | [Introduction: what LangChain is, and the road ahead](lectures/00-intro/) |  |
| 01 | [Project setup: LM Studio, uv, and the first call](lectures/01-setup/) |  |

Each lecture's folder has its code, a README with what to run, and `output/`:
the real output recorded for the video.

---
QuantCodingVersity · Dr. Saad Laouadi · [@DrSaadLaouadi](https://x.com/DrSaadLaouadi) · [youtube.com/@QuantCodingVersity](https://youtube.com/@QuantCodingVersity)
