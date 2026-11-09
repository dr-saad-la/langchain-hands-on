# Lecture 01 · Project setup: LM Studio, uv, and the first call

Run these in your terminal, in order (the video shows each one):

```zsh
lms ls
lms load qwen/qwen3.6-27b --context-length 32768
lms ps
lms server start
curl -s http://localhost:1234/v1/models
mkdir -p ~/projects
cd ~/projects
uv init --no-package --python 3.12 langchain-hands-on
cd langchain-hands-on
ls -A
cat pyproject.toml
uv run main.py
uv add langchain langchain-openai
cat pyproject.toml
# now edit main.py: its code is 01_main_qwen.py in this folder
uv run main.py
lms load google/gemma-4-e4b
# now edit main.py: its code is 02_main_gemma.py in this folder
uv run main.py
```

`output/terminal.txt` is the real terminal output, as recorded for the video.

Model: Qwen3.6 27B in LM Studio. With another model, the answers differ in wording.
